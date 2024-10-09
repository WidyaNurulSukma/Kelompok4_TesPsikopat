from flask import Flask, render_template, request, redirect, flash, url_for
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/hasil', methods=['POST'])
def hasil():
   # Mengambil data dari form pertama
    print(request.method)  # Ini akan mencetak metode yang diterima
    q1 = request.form.get('q1', 0)
    q2 = request.form.get('q2', 0)
    q3 = request.form.get('q3', 0)
    q4 = request.form.get('q4', 0)
    q5 = request.form.get('q5', 0)
    q6 = request.form.get('q6', 0)
    q7 = request.form.get('q7', 0)
    q8 = request.form.get('q8', 0)
    q9 = request.form.get('q9', 0)
    q10 = request.form.get('q10', 0)
    q11 = request.form.get('q11', 0)
    q12 = request.form.get('q12', 0)
    q13 = request.form.get('q13', 0)
    q14 = request.form.get('q14', 0)
    q15 = request.form.get('q15', 0)
    q16 = request.form.get('q16', 0)
    q17 = request.form.get('q17', 0)
    q18 = request.form.get('q18', 0)
    q19 = request.form.get('q19', 0)
    q20 = request.form.get('q20', 0)

    # Menampilkan form kedua dengan jawaban dari form pertama disimpan dalam hidden input
    return render_template('hasil.html', q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, q9=q9, q10=q10)

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    # Mengambil semua jawaban dari form pertama dan kedua
    answers = {
        'q1': int(request.form.get('q1', 0)),
        'q2': int(request.form.get('q2', 0)),
        'q3': int(request.form.get('q3', 0)),
        'q4': int(request.form.get('q4', 0)),
        'q5': int(request.form.get('q5', 0)),
        'q6': int(request.form.get('q6', 0)),
        'q7': int(request.form.get('q7', 0)),
        'q8': int(request.form.get('q8', 0)),
        'q9': int(request.form.get('q9', 0)),
        'q10': int(request.form.get('q10', 0)),
        'q11': int(request.form.get('q11', 0)),
        'q12': int(request.form.get('q12', 0)),
        'q13': int(request.form.get('q13', 0)),
        'q14': int(request.form.get('q14', 0)),
        'q15': int(request.form.get('q15', 0)),
        'q16': int(request.form.get('q16', 0)),
        'q17': int(request.form.get('q17', 0)),
        'q18': int(request.form.get('q18', 0)),
        'q19': int(request.form.get('q19', 0)),
        'q20': int(request.form.get('q20', 0))
    }
   
        
        # Lanjutkan untuk semua pertanyaan hingga q20
    

    total = sum(answers.values())

    # Logika untuk menghitung status psikopat berdasarkan total nilai
    if 80 <= total <= 100:
        status_psikopat = "Anda Psikopat Ekstrim, karena Anda memiliki sifat seperti tidak adanya rasa bersalah, manipulasi ekstrem, dan pengabaian hak-hak orang lain dengan kecenderungan kekerasan atau perilaku predator. Segera konsultasikan dengan Tenaga Ahli untuk penanganan lebih lanjut."
    elif 60 <= total <= 79:
        status_psikopat = "Anda Psikopat Tinggi, karena Anda memiliki sifat suka memanipulasi, kurang memiliki empati, dan sering bertindak secara licik untuk mencapai tujuan pribadi. Konsultasi dengan Tenaga Ahli sangat direkomendasikan untuk mendapatkan pemahaman lebih dalam. "
    elif 40 <= total <= 59:
        status_psikopat = "Anda Psikopat Sedang, Karena berdasarkan tes, Anda memiliki perilaku seperti manipulatif dan minim empati dalam situasi tertentu, meskipun mungkin belum ekstrem. Disarankan untuk berkonsultasi dengan Tenaga Ahli untuk mendapatkan pemahaman lebih dalam."
    elif 20 <= total <= 39:
        status_psikopat = "Anda Psikopat Rendah, karena Anda memiliki sifat seperti sesekali berbohong atau kurang bertanggung jawab, tetapi masih baik dalam interaksi sosial. Konsultasi dengan Tenaga Ahli untuk mendapatkan pemahaman lebih dalam."
    else:
        status_psikopat = "Anda Tidak Menunjukkan Tanda-tanda Psikopat, Anda menunjukkan empati yang baik dan rasa tanggung jawab dalam tindakan sehari-hari. Meski demikian, konsultasi dengan Tenaga Ahli untuk mendapatkan pemahaman lebih dalam."

    # Menampilkan hasil
    return render_template('result.html', answers=answers, total=total, status_psikopat=status_psikopat)

if __name__ == '__main__':
    app.run(debug=True)


