from flask import render_template, request, jsonify
from app import app
from .models import get_all_logs, insert_log
import json
from datetime import datetime

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/dash')
def dashboard():
    logs = get_all_logs()
    return render_template('dash.html', logs=logs)

@app.route('/ping', methods=['GET'])
def ping():
    with open('db.json', 'a') as f:
        json.dump({"endpoint": "/ping", "time": str(datetime.now())}, f)
        f.write('\n')
    return jsonify({"message": "pong"})

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    with open('db.json', 'a') as f:
        json.dump({"endpoint": "/echo", "time": str(datetime.now())}, f)
        f.write('\n')
    if data and 'dados' in data:
        return jsonify({'resposta': data['dados']})
    else:
        return jsonify({'resposta': 'No data provided.'})