from flask import Flask, render_template, request, redirect, flash, url_for
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    answers = {
        'q1': int(request.form.get('q1') or 0), 'q2': int(request.form.get('q2') or 0), 'q3': int(request.form.get('q3') or 0), 'q4': int(request.form.get('q4') or 0),
        'q5': int(request.form.get('q5') or 0), 'q6': int(request.form.get('q6') or 0), 'q7': int(request.form.get('q7') or 0), 'q8': int(request.form.get('q8') or 0),
        'q9': int(request.form.get('q9') or 0), 'q10': int(request.form.get('q10') or 0), 'q11': int(request.form.get('q11') or 0), 'q12': int(request.form.get('q12') or 0),
        'q13': int(request.form.get('q13') or 0), 'q14': int(request.form.get('q14') or 0), 'q15': int(request.form.get('q15') or 0), 'q16': int(request.form.get('q16') or 0),
        'q17': int(request.form.get('q17') or 0), 'q18': int(request.form.get('q18') or 0), 'q19': int(request.form.get('q19') or 0),'q20': int(request.form.get('q20') or 0)
    }

    total = sum(answers.values())

    # menambahkan rule
    if 80 <= total <= 100:
        status_psikopat =  "Anda Psikopat Ekstrim, karena anda memiliki sifat seperti tidak adanya rasa bersalah, manipulasi ekstrem, dan pengabaian hak-hak orang lain dengan kecenderungan kekerasan atau perilaku predator. Segera konsultasikan dengan tenaga ahli untuk penanganan lebih lanjut."
    elif 60 <= total <= 79:
        status_psikopat =  "Anda Psikopat Tinggi, karena anda memiliki sifat suka memanipulasi, kurang memiliki empati, dan sering bertindak secara licik untuk mencapai tujuan pribadi. Konsultasi dengan tenaga ahli sangat direkomendasikan untuk mendapatkan pemahaman lebih dalam. "
    elif 40 <= total <= 59:
        status_psikopat =  "Anda Psikopat Sedang, Karena berdasarkan tes, anda memiliki perilaku seperti manipulatif dan minim empati dalam situasi tertentu, meskipun mungkin belum ekstrem. Disarankan untuk berkonsultasi dengan tenaga ahli untuk mendapatkan pemahaman lebih dalam."
    elif 20 <= total <= 39:
        status_psikopat =  "Anda psikopat rendah, karena anda memiliki sifat seperti sesekali berbohong atau kurang bertanggung jawab, tetapi masih baik dalam interaksi sosial. Konsultasi dengan tenaga ahli untuk mendapatkan pemahaman lebih dalam."
    else:
        status_psikopat =  "Anda Tidak Menunjukkan Tanda-tanda Psikopat, anda menunjukkan empati yang baik dan rasa tanggung jawab dalam tindakan sehari-hari. Meski demikian, konsultasi dengan tenaga ahli untuk mendapatkan pemahaman lebih dalam."

    return render_template('result.html', answers=answers, total=total, status_psikopat=status_psikopat)


