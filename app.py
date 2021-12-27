from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import pickle
import sys
import logging

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":

        model = pickle.load(open('model_asma.pkl', 'rb'))

        test = [{
            'Penanganan Pernapasan': int(request.form.get('penangananPernapasan')),
            'Asma Kambuh': int(request.form.get('asmaKambuh')),
            'Gejala Malam Hari': int(request.form.get('gejalaMalamHari')),
            'Sesak Napas Lambuh': int(request.form.get('sesakNafasLambuh')),
            'Tingkat Kontrol Asma': int(request.form.get('tingkatKontrolAsma')),
            'Usia': int(request.form.get('usia')),
            'Jenis Kelamin': int(request.form.get('jenisKelamin')),
        }]

        print(test)

        predict = model.predict(pd.DataFrame(test))
        response = jsonify({
            'perdict': str(predict[0]),
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


if __name__ == '__main__':
    app.run(debug=True)
