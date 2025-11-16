📘 Reddit Yorum Kazıyıcı (Scraper)

Belirlediğin Reddit gönderilerinin altındaki tüm yorumları otomatik olarak çeken bir Python aracıdır.
Reddit API kullanmaz — doğrudan Reddit’in halka açık .json endpointlerini kullanır.

💬 Özellikler

✔ Sadece URL vererek yorumları çekme
✔ Her seviyedeki (nested) yorumları yakalama
✔ Kullanıcı adı / yorum / skor / permalink toplama
✔ JSON formatında temiz çıktı
✔ NLP, duygu analizi, veri madenciliği ve model eğitimine uygun

📥 Girdi Yapısı

Aşağıdaki listeye, yorumlarını almak istediğiniz Reddit gönderilerini eklemeniz yeterlidir:

POST_URLS = [
    "https://www.reddit.com/r/gold/comments/xxxxxx/example/",
    "https://www.reddit.com/r/investing/comments/yyyyyy/example2/",
]

🛠 Kurulum

Gerekli bağımlılık tek satırda yüklenir:

pip install requests

▶️ Kodun Çalışma Mantığı

Her URL'nin sonuna otomatik olarak .json eklenir

Reddit'in public JSON endpoint'i response döndürür

Tüm yorumlar iç içe yapılar dahil taranır

JSON dosyasına kaydedilir

📂 Çıktı Örneği

reddit_yorumlari.json:

{
    "author": "reddit_user",
    "comment": "Gold prices are going crazy today!",
    "score": 42,
    "permalink": "https://www.reddit.com/r/gold/comments/.../abc123/"
}

🎯 Kullanım Alanları

🔹 Duygu analizi (sentiment analysis)
🔹 Topluluk davranışı araştırmaları
🔹 Ekonomi / finans temelli sosyal medya analizleri
🔹 Trend tespiti
🔹 Makine öğrenimi / NLP veri seti oluşturma

📝 Notlar

Reddit API gerektirmez

Public JSON endpoint’i kullanıldığı için bot-authentication sorunları yoktur

Tamamen ücretsizdir

Çok büyük gönderilerde (20k+ yorum) zaman yönetimi için delay eklemeniz önerilir
