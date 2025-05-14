import threading
import queue
import time
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import face_recognition
import serial
from telebot import TeleBot

# --- Telegram Bot Ayarları ---
TELEGRAM_BOT_TOKEN = "8150520543:AAF5bAGwb6P7oCqZDPEcbHhnLRWo6Ju3V5A"
bot = TeleBot(TELEGRAM_BOT_TOKEN)

# Kayıtlı kullanıcı bilgileri
registered_users = {
    "Davut Erol": {"telegram_id": 8166383651, "group": 1, "last_sent_time": 0, "current_code": None},
    "Ufuk Karan Soyoral": {"telegram_id": 1523773552, "group": 2, "last_sent_time": 0, "current_code": None},
    "Anonim": {"telegram_id": 8166383651, "group": 3, "last_sent_time": 0, "current_code": None}
}

# --- Arduino ile Seri İletişim ---
try:
    ser = serial.Serial('COM7', 9600)
    time.sleep(2)
    print("Arduino ile bağlantı kuruldu.")
except serial.SerialException:
    print("Arduino seri portu bulunamadı! Lütfen bağlantıyı kontrol edin.")
    ser = None

# --- Eğitim için yüzler ve gruplar ---
known_face_encodings = []
known_face_names = []
known_face_groups = []

# --- Eğitim Verisini Yükleme ---
def load_training_data():
    base_path = "training_images"
    group_folders = os.listdir(base_path)

    for group_folder in group_folders:
        group_path = os.path.join(base_path, group_folder)
        if os.path.isdir(group_path):
            for img_name in os.listdir(group_path):
                img_path = os.path.join(group_path, img_name)
                image = face_recognition.load_image_file(img_path)
                encodings = face_recognition.face_encodings(image)
                if encodings:
                    known_face_encodings.append(encodings[0])
                    known_face_names.append(img_name.split('.')[0])
                    known_face_groups.append(group_folder)

# --- Rastgele Kod Oluşturma ---
def generate_code():
    return str(random.randint(100000, 999999))

# --- Telegram Mesaj Kuyruğu ---
message_queue = queue.Queue()

def telegram_worker():
    while True:
        user_name = message_queue.get()
        send_code_to_user(user_name)
        message_queue.task_done()

threading.Thread(target=telegram_worker, daemon=True).start()

def send_code_to_user(user_name):
    current_time = time.time()
    if user_name in registered_users:
        user_data = registered_users[user_name]
        time_elapsed = current_time - user_data["last_sent_time"]

        if time_elapsed >= 120:  # 2 dakika kontrolü
            telegram_id = user_data["telegram_id"]
            new_code = generate_code()
            user_data["current_code"] = new_code
            user_data["last_sent_time"] = current_time
            bot.send_message(telegram_id, f"Merhaba {user_name}, doğrulama kodunuz: {new_code}")

# --- Kapı Açma Fonksiyonu ---
def unlock_door(user_name, code):
    if user_name in registered_users:
        user_data = registered_users[user_name]
        group = user_data["group"]
        if code == user_data["current_code"]:
            try:
                if ser:
                    ser.write(f"DOOR:{group}\n".encode())
                    messagebox.showinfo("Başarılı", f"Grup {group} için kapı açıldı!")
                    user_data["current_code"] = None
                else:
                    messagebox.showerror("Hata", "Arduino bağlantısı bulunamadı!")
            except serial.SerialException:
                messagebox.showerror("Hata", "Arduino'ya sinyal gönderilemedi!")
        else:
            messagebox.showerror("Hata", "Hatalı doğrulama kodu!")

# --- Tkinter GUI ve Kamera Görüntüsü ---
frame_count = 0  # Kare sayacı

def create_gui():
    def update_frame():
        global frame_count
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (640, 480))  # Çözünürlüğü düşür
            frame = cv2.flip(frame, 1)

            if frame_count % 10 == 0:  # Her 10 karede bir yüz tanıma
                threading.Thread(target=process_face_recognition, args=(frame,)).start()

            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            imgtk = ImageTk.PhotoImage(image=img)
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)

            frame_count += 1

        root.after(30, update_frame)

    def process_face_recognition(frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        name_to_display = "Bilinmeyen Kişi"
        text_color = "red"
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            if True in matches:
                first_match_index = matches.index(True)
                name_to_display = known_face_names[first_match_index]
                text_color = "green"
                message_queue.put(name_to_display)  # Telegram mesajını kuyruğa ekle

        name_label.config(text=name_to_display, fg=text_color)

    def submit_code():
        entered_code = code_entry.get()
        unlock_door(name_label.cget("text"), entered_code)

    # Ana pencere
    root = tk.Tk()
    root.title("Kamera Görüntüsü ve Yüz Tanıma")

    # Kamera görüntüsü için etiket
    global video_label
    video_label = tk.Label(root)
    video_label.pack()

    # Tanınan kişi bilgisi için etiket
    global name_label
    name_label = tk.Label(root, text="Bilinmeyen Kişi", font=("Arial", 14), fg="red")
    name_label.pack(pady=10)

    # Doğrulama kodu giriş alanı
    tk.Label(root, text="Doğrulama Kodunu Girin:").pack(pady=10)
    code_entry = tk.Entry(root, font=("Arial", 14))
    code_entry.pack(pady=10)

    # Gönder butonu
    tk.Button(root, text="Gönder", command=submit_code, font=("Arial", 12)).pack(pady=10)

    update_frame()
    root.mainloop()

# --- Kamera Başlatma ---
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()

# Eğitim verilerini yükle
print("Eğitim verileri yükleniyor...")
load_training_data()
print("Eğitim verileri başarıyla yüklendi!")

# --- Yüz Tanıma ve Kamera Görüntüsü ---
create_gui()

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
if ser:
    ser.close()