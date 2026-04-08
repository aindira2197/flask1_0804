from flask import Flask, render_template

app = Flask(__name__)

mahsulotlar = ["Noutbuk", "Telefon", "Planshet", "Qulaqchin", "Kamera"]

@app.route("/")
def home():
    return render_template("index.html", mahsulotlar=mahsulotlar)

@app.route('/roy/<int:indeks>')
def element(indeks):
    el = mahsulotlar[indeks]
    return render_template('mah.html', el=el)

@app.route('/roy/qidiruv/<nomi>')
def qidiruv(nomi):
    if nomi.lower() in list(map(lambda m: m.lower(), mahsulotlar)):
        res = nomi
    else:
        res = "None"
    return render_template('qidiruv.html', res=res)


if __name__ == '__main__':
    app.run(debug=True)
