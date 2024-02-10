from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# SQLite veritabanı bağlantısı oluştur
conn = sqlite3.connect('kayit.db')
cursor = conn.cursor()

# Kullanıcıları veritabanından çek
def kullaniciyi_al(email, sifre):
    cursor.execute("SELECT * FROM kullanicilar WHERE email=? AND sifre=?", (email, sifre))
    return cursor.fetchone()

@app.route('/', methods=['GET', 'POST'])
def giris():
    if request.method == 'POST':
        email = request.form['email']
        sifre = request.form['sifre']

        # Kullanıcıyı veritabanından çek
        kullanici = kullaniciyi_al(email, sifre)

        if kullanici:
            # Giriş başarılı ise ana sayfaya yönlendir
            return redirect(url_for('anasayfa'))
        else:
            # Giriş başarısız ise hata mesajı göster
            return "Geçersiz email veya şifre. Lütfen tekrar deneyin."

    return render_template('index.html')

@app.route('/anasayfa')
def anasayfa():
    return "Giriş başarılı! Ana sayfaya hoş geldiniz."

if __name__ == '__main__':
    app.run(debug=True)
