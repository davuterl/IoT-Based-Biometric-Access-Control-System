flowchart TD
    A[🚀 Sistem Başlatma] --> B[📷 Kamera Başlatma]
    B --> C[🔧 Arduino Bağlantı Kontrolü]
    C --> D[📚 Eğitim Verilerini Yükleme]
    D --> E[🤖 Telegram Bot Başlatma]
    
    E --> F[👁️ Görüntü Yakalama]
    F --> G{🔍 Yüz Tespit Edildi mi?}
    
    G -->|Hayır| F
    G -->|Evet| H[🧠 Yüz Tanıma İşlemi]
    
    H --> I{👤 Kullanıcı Tanındı mı?}
    I -->|Hayır| J[❌ Erişim Reddedildi]
    J --> K[📝 Başarısız Giriş Kaydı]
    K --> F
    
    I -->|Evet| L[✅ Kullanıcı Doğrulandı]
    L --> M{⏰ Son Kod Gönderim Zamanı?}
    
    M -->|120s geçmedi| N[⚠️ Çok Erken Deneme]
    N --> F
    
    M -->|120s geçti| O[🎲 6 Haneli Kod Üretme]
    O --> P[📱 Telegram'a Kod Gönderimi]
    
    P --> Q{📨 Mesaj Gönderildi mi?}
    Q -->|Hayır| R[❌ Telegram Hatası]
    R --> F
    
    Q -->|Evet| S[⌨️ Kullanıcıdan Kod Girişi Bekleme]
    S --> T{🔐 Kod Doğru mu?}
    
    T -->|Hayır| U[❌ Yanlış Kod]
    U --> V{🔄 3 Deneme Hakkı Kaldı mı?}
    V -->|Evet| S
    V -->|Hayır| W[🚫 Hesap Geçici Bloke]
    W --> F
    
    T -->|Evet| X[🎯 İki Faktörlü Doğrulama Başarılı]
    X --> Y{👥 Kullanıcı Grubu?}
    
    Y -->|Grup 1| Z1[🔧 Servo 1 Kontrolü]
    Y -->|Grup 2| Z2[🔧 Servo 2 Kontrolü]
    Y -->|Grup 3| Z3[🔧 Servo 3 Kontrolü]
    
    Z1 --> AA[📡 Arduino'ya Komut Gönderimi]
    Z2 --> AA
    Z3 --> AA
    
    AA --> BB{🔌 Arduino Bağlantısı OK?}
    BB -->|Hayır| CC[❌ Arduino Bağlantı Hatası]
    CC --> F
    
    BB -->|Evet| DD[⚙️ Servo Motor Hareketi]
    DD --> EE[🚪 Kapı Açma İşlemi]
    EE --> FF[⏱️ 3 Saniye Bekleme]
    FF --> GG[🔒 Kapı Kapama İşlemi]
    
    GG --> HH[📊 Başarılı Erişim Kaydı]
    HH --> II[📱 Başarı Bildirimi]
    II --> JJ[🔄 Sistem Hazır Duruma Dönüş]
    JJ --> F
    
    %% Hata Durumları
    KK[⚠️ Sistem Hataları] --> LL{🔍 Hata Türü?}
    LL -->|Kamera Hatası| MM[📷 Kamera Yeniden Başlatma]
    LL -->|Arduino Hatası| NN[🔧 Seri Port Yeniden Bağlama]
    LL -->|Telegram Hatası| OO[🤖 Bot Yeniden Başlatma]
    LL -->|Yüz Tanıma Hatası| PP[🧠 Model Yeniden Yükleme]
    
    MM --> F
    NN --> F
    OO --> F
    PP --> F
    
    %% Stil Tanımlamaları
    classDef startEnd fill:#e1f5fe,stroke:#01579b,stroke-width:3px,color:#000
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:2px,color:#000
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#000
    classDef success fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px,color:#000
    classDef error fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#000
    classDef telegram fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#000
    classDef arduino fill:#fff8e1,stroke:#f57c00,stroke-width:2px,color:#000
    
    class A,JJ startEnd
    class B,C,D,E,H,L,O,P,S,X,AA,DD,EE,FF,GG,HH,II process
    class G,I,M,Q,T,V,Y,BB,LL decision
    class Z1,Z2,Z3,MM,NN,OO,PP success
    class J,K,N,R,U,W,CC error
    class P,II telegram
    class AA,DD,EE,GG arduino