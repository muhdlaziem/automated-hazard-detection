import base64
import numpy as np
import io
import keras
from keras import Sequential
from keras.models import load_model
from flask import request
from flask import jsonify
from flask import Flask, render_template

app = Flask(__name__)
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 999999999999

@app.route('/')
def home():
    return render_template('index.html')

def get_model():
    global model
    model = load_model('./assets/model.h5')
    print(" * Model loaded!")



print(' * Loading Keras model...')
get_model()

@app.route('/predict', methods = ['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    print(int_features)
    prediction = model.predict(np.expand_dims(np.array(int_features), axis=0))
    return render_template('index.html', prediction_text='PM2.5 readings should be {0:.2f}'.format(prediction[0][0]))

if __name__ == "__main__":
    app.run(debug=True)