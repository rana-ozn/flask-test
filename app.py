# app.py
from flask import Flask, render_template
import os
from . import quote_provider  # Aynı dizindeki quote_provider.py'yi içe aktar

# Flask uygulaması oluşturulurken, import_name'in (__name__) bir Python paketi
# gibi davranması için uygulamanın bir modül içinde olması gerekir.
# Eğer app.py'yi direkt çalıştırıyorsanız, import_name için basitçe __name__ kullanın.
app = Flask(__name__)

# --- Context Processor Kaydı ---
# Context Processor, her render_template çağrıldığında çalışır ve
# döndürdüğü sözlükteki değişkenler otomatik olarak şablona eklenir.

# get_random_quote fonksiyonunu, uygulamanın (None) şablon bağlamı işlemcilerine ekliyoruz.
app.context_processor(quote_provider.get_random_quote)

# --- Görünüm Fonksiyonları ---

@app.route("/")
def index():
    """Ana sayfa görünümü."""
    # Dikkat: Bu görünüm fonksiyonunda 'quote_of_the_day' değişkenini
    # kendimiz şablona İLETMİYORUZ. Context Processor bunu otomatik yapıyor!
    return render_template("index.html")

# --- Uygulamayı Çalıştırma ---

if __name__ == "__main__":
    # Bu satır, Flask uygulamasını geliştirme sunucusunda başlatır.
    # Flask CLI kullanılıyorsa (önerilen yöntem), bu bloğa gerek kalmaz.
    # Terminalde 'flask run' komutunu kullanmak daha iyidir.
    app.run(debug=True)