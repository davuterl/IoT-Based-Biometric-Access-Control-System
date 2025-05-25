sequenceDiagram
    participant K as 👤 Kullanıcı
    participant Kam as 📷 Kamera
    participant Py as 🐍 Python
    participant TG as 📱 Telegram
    participant Ard as 🔧 Arduino
    participant Servo as ⚙️ Servo Motor
    
    K->>Kam: Yüzünü göster
    Kam->>Py: Görüntü verisi
    Py->>Py: Yüz tespiti (OpenCV)
    Py->>Py: Yüz tanıma (face_recognition)
    
    alt Kullanıcı tanındı
        Py->>Py: 6 haneli kod üret
        Py->>TG: Kod gönder
        TG->>K: Telegram mesajı
        K->>Py: Kodu gir
        
        alt Kod doğru
            Py->>Ard: Servo komutunu gönder
            Ard->>Servo: Motor hareketi
            Servo->>Servo: Kapı aç (3 saniye)
            Servo->>Servo: Kapı kapat
            Py->>TG: Başarı bildirimi
            TG->>K: Erişim onaylandı
        else Kod yanlış
            Py->>K: Hata mesajı
        end
    else Kullanıcı tanınmadı
        Py->>K: Erişim reddedildi
    end