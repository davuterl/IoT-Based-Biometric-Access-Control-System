graph LR
    subgraph "💻 Ana Sistem"
        A1[Python Ana Program]
        A2[OpenCV Görüntü İşleme]
        A3[Face Recognition]
        A4[Tkinter GUI]
    end
    
    subgraph "📱 Telegram Sistemi"
        B1[Bot Token Doğrulama]
        B2[Kullanıcı ID Kontrolü]
        B3[Kod Üretimi]
        B4[Mesaj Gönderimi]
    end
    
    subgraph "🔧 Arduino Sistemi"
        C1[Seri Port Bağlantısı]
        C2[Komut Alma]
        C3[Servo 1 Kontrolü]
        C4[Servo 2 Kontrolü]
        C5[Servo 3 Kontrolü]
    end
    
    subgraph "📷 Kamera Sistemi"
        D1[USB Kamera]
        D2[Görüntü Yakalama]
        D3[Yüz Tespiti]
        D4[Yüz Kodlaması]
    end
    
    A1 --> A2
    A2 --> A3
    A3 --> A4
    A1 --> B1
    B1 --> B2
    B2 --> B3
    B3 --> B4
    A1 --> C1
    C1 --> C2
    C2 --> C3
    C2 --> C4
    C2 --> C5
    D1 --> D2
    D2 --> D3
    D3 --> D4
    D4 --> A3