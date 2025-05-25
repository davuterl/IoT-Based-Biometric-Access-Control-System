flowchart TD
    A[🚨 Hata Tespit Edildi] --> B{🔍 Hata Türü Analizi}
    
    B -->|Kamera Hatası| C[📷 Kamera Kontrolü]
    B -->|Arduino Hatası| D[🔧 Seri Port Kontrolü]
    B -->|Telegram Hatası| E[📱 Bot Token Kontrolü]
    B -->|Yüz Tanıma Hatası| F[🧠 Model Kontrolü]
    
    C --> C1{📹 Kamera Bağlı mı?}
    C1 -->|Hayır| C2[🔌 USB Bağlantısı Kontrol Et]
    C1 -->|Evet| C3[📷 Kamera Yeniden Başlat]
    C2 --> G[🔄 Sistem Yeniden Başlat]
    C3 --> G
    
    D --> D1{🔌 COM Port Açık mı?}
    D1 -->|Hayır| D2[🔧 Port Yeniden Aç]
    D1 -->|Evet| D3[📡 Bağlantı Test Et]
    D2 --> G
    D3 --> G
    
    E --> E1{🌐 İnternet Bağlantısı?}
    E1 -->|Hayır| E2[📶 Ağ Bağlantısı Kontrol Et]
    E1 -->|Evet| E3[🤖 Bot Token Doğrula]
    E2 --> G
    E3 --> G
    
    F --> F1{📚 Eğitim Verisi Mevcut?}
    F1 -->|Hayır| F2[📁 Dosya Yolunu Kontrol Et]
    F1 -->|Evet| F3[🔄 Model Yeniden Yükle]
    F2 --> G
    F3 --> G
    
    G --> H[✅ Sistem Hazır]