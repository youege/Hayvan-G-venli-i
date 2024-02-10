from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_complaint', methods=['POST'])
def submit_complaint():
    data = request.json
    email = data['email']
    complaint = data['complaint']
    
    # Burada şikayet bilgilerini işleyebilirsiniz, örneğin veritabanına kaydedebilirsiniz
    
    # İşlem başarılı olduğunu varsayalım, JSON yanıtı döndürelim
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
