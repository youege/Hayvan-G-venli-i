from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# SQLite veritabanı bağlantısı oluştur
conn = sqlite3.connect('kayit.db')
cursor = conn.cursor()

# Kullanıcılar tablosunu oluştur
cursor.execute('''CREATE TABLE IF NOT EXISTS kullanicilar
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   kullanici_adi TEXT,
                   email TEXT,
                   sifre TEXT)''')
conn.commit()

def kullanici_ekle(kullanici_adi, email, sifre):
    # Kullanıcıyı veritabanına ekle
    cursor.execute("INSERT INTO kullanicilar (kullanici_adi, email, sifre) VALUES (?, ?, ?)",
                   (kullanici_adi, email, sifre))
    conn.commit()

def kullaniciyi_al(kullanici_adi):
    # Kullanıcıyı kullanıcı adına göre al
    cursor.execute("SELECT * FROM kullanicilar WHERE kullanici_adi=?", (kullanici_adi,))
    return cursor.fetchone()

@app.route('/kayit', methods=['GET', 'POST'])
def kayit():
    if request.method == 'POST':
        kullanici_adi = request.form['kullanici_adi']
        email = request.form['email']
        sifre = request.form['sifre']
        sifre_onay = request.form['sifre_onay']

        # Şifrelerin eşleşip eşleşmediğini kontrol et
        if sifre != sifre_onay:
            return "Şifreler eşleşmiyor, lütfen tekrar deneyin."

        # Kullanıcıyı veritabanına ekle
        kullanici_ekle(kullanici_adi, email, sifre)

        # Kayıt başarılı mesajını göster
        return f"Kayıt başarılı! Hoş geldiniz, {kullanici_adi}!"

    return render_template('kayit.html')

if __name__ == '__main__':
    app.run(debug=True)
