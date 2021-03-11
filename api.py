import flask
from flask import request, jsonify
import os
from flask import Flask, render_template
import pyqrcode
import base64
from base64 import b64encode
import json
from flask_cors import CORS
import time
# Open Command prompt and run this file as "python api.py"
# API URL: http://127.0.0.1:5002/api/v1/resources/qrimage?id=balaji


MY_FOLDER = os.path.join('static', 'qrCodes')
app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = MY_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
CORS(app)

@app.route('/api/v1/resources/qrimage', methods=['GET'])
def qr_image():
    if 'id' in request.args:
        qr_id=str(request.args['id'])
    else:
        return('Error: no id field provided')
    url = pyqrcode.create(qr_id)    
    url.png('static/qrCodes/tempQR.png',scale=8)
    with open(r"static/qrCodes/tempQR.png", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    a=str(my_string)
    return jsonify(a)

@app.route('/')
def home():
   return render_template('index.html')
    

app.run(host='0.0.0.0',port=5002)
