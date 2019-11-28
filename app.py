from flask import Flask, render_template, request, jsonify
import pickle
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def front_end():
    return render_template('index.html')


@app.route('/notebook', methods=['POST'])
def prediction():
    data = request.get_json()
    pred = model_saved.predict(data)
    return jsonify(str(pred))


if __name__ == '__main__':
    MODEL_PATH = './models/model_saved.pkl'
    with open(MODEL_PATH, 'rb') as fid:
        model_saved = pickle.load(fid)
    app.run(debug=True)
