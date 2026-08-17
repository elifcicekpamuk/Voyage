# Voya - Architecture & Development Roadmap

## Proje Geliştirme Yaklaşımı
Bu proje hem full-stack (React + FastAPI) hem de veri tabanı (PostGIS) ve yapay zeka (RAG, Vector DB) içerdiği için modüler ilerlemek çok önemlidir. Arkadaşınla iş bölümü yaparken biriniz Frontend/UI, diğeriniz Backend/Database tarafına odaklanabilir.

---

## 🗄️ Veritabanı Şeması (PostgreSQL + PostGIS)

```sql
-- Ana Tabloların Mantıksal Tasarımı

Table User {
  id UUID [primary key]
  email VARCHAR
  name VARCHAR
  created_at TIMESTAMP
}

Table Location {
  id UUID [primary key]
  user_id UUID [ref: > User.id]
  geom GEOMETRY(Point, 4326) -- PostGIS için lat/lng tutan özel veri tipi
  title VARCHAR
  city VARCHAR
  category VARCHAR
}

Table JournalEntry {
  id UUID [primary key]
  user_id UUID [ref: > User.id]
  location_id UUID [ref: > Location.id]
  content TEXT
  date TIMESTAMP
  mood VARCHAR      -- AI tarafından doldurulabilir
  rating INT
}

Table Tags {
  id UUID [primary key]
  entry_id UUID [ref: > JournalEntry.id]
  tag_name VARCHAR  -- AI tarafından otomatik eklenebilir
}
```

---

## 🚀 Geliştirme Aşamaları (Phases)

### Phase 1: MVP ve Temel Full-Stack Altyapısı (AI Yok)
**Odak:** Projenin iskeletini ayağa kaldırmak.
- **Backend:** FastAPI kurulumu, SQLAlchemy ile PostgreSQL bağlantısı. Kullanıcı oluşturma, konum ve günlük ekleme (CRUD) endpoint'leri.
- **Frontend:** React + TypeScript kurulumu. Mapbox veya Leaflet ile haritanın ekranda gösterilmesi.
- **Test:** Haritaya tıklayıp manuel olarak bir lokasyon ve not ekleyebilmek.

### Phase 2: Harita Deneyimi ve Timeline (Günlük)
**Odak:** Kullanıcı deneyimini Voya'nın vizyonuna yaklaştırmak.
- **Frontend:** Eklenen pinlerin haritada gösterilmesi. Pinlere tıklandığında açılan detay kartları (başlık, tarih, not).
- **Frontend:** "Timeline" sayfasının yapılması (Zaman çizelgesi şeklinde aşağı kaydırarak anıları okuma).
- **Backend:** PostGIS kullanılarak "şu sınırlar (bounding box) içindeki pinleri getir" API'sinin yazılması.

### Phase 3: AI Otomasyonu (Akıllı Günlük)
**Odak:** Yazılan metinlerden anlam çıkarmak.
- **Nasıl Çalışacak:** Kullanıcı "Bugün çok yorucuydu ama sonunda arkadaşlarla güzel vakit geçirdik" yazdığında, FastAPI bu metni bir LLM API'sine (örn. OpenAI) gönderecek.
- **Çıktı:** LLM'den JSON formatında veri dönecek: `{"mood": "😊", "tags": ["friends", "tired", "good_day"]}`.
- **Sonuç:** Bu veriler otomatik olarak veritabanına kaydedilecek. Kullanıcı etiket girmekle uğraşmayacak.

### Phase 4: İstatistikler ve "Year in Review"
**Odak:** Veri görselleştirme.
- Ziyaret edilen şehir sayısı, en çok gidilen mekanlar, aylara göre duygu durumu (mood) grafikleri.
- Veritabanından aggregate (gruplama) sorguları ile bu istatistiklerin çekilip frontend'de grafik kütüphaneleri (Recharts vb.) ile çizilmesi.

### Phase 5: Voya Memory Search (RAG Entegrasyonu)
**Odak:** "2025 yazında arkadaşlarımla gittiğim yerleri bul" özelliğini yapmak.
1. **Embedding İşlemi:** Kullanıcı her günlük kaydı girdiğinde, bu metin bir embedding modelinden (örn. text-embedding-3-small) geçirilip vektöre dönüştürülecek.
2. **Vektör Veritabanı:** Bu vektörler ChromaDB veya FAISS içine (Journal ID'si ile birlikte) kaydedilecek.
3. **Arama (Retrieval):** Kullanıcı bir soru sorduğunda, soru da vektöre dönüştürülüp ChromaDB'de vektörel benzerlik araması yapılacak.
4. **Cevap (Generation):** En benzer 5 günlük kaydı bulunup LLM'e verilecek: "Kullanıcının geçmiş kayıtları şunlar: [Kayıtlar]. Şimdi kullanıcının sorusuna cevap ver."

---

## 🛠️ İş Bölümü Tavsiyesi
Projenin mimarisi mühendislik açısından dolu dolu. 
- **Kişi 1 (Backend & AI):** FastAPI, PostgreSQL/PostGIS, SQLAlchemy, ChromaDB ve Prompt Engineering süreçlerini üstlenebilir.
- **Kişi 2 (Frontend & UI/UX):** React, Map entegrasyonu, State Management, Timeline tasarımı ve veri görselleştirme (Charts) süreçlerini üstlenebilir.
