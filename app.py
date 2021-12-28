from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import pickle
# from jcopml.utils import save_model, load_model
from flask_cors import CORS

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['DEBUG'] = True
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":

        model = pickle.load(open('model_asma.pkl', 'rb'))
        # model = load_model('model_asma.pkl')

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

        # predict = model.predict(pd.DataFrame(test))
        # response = jsonify(result={
        #     'perdict': str(predict[0]),
        # })
        # response.headers.add('Access-Control-Allow-Origin', '*')
        # return response
        return jsonify(test)
    elif request.method == "GET":
        return '<h1>get</h1>'


if __name__ == '__main__':
    app.run(debug=True)
