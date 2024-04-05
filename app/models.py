from app import db
from tinydb import TinyDB
from datetime import datetime

def insert_ping_log():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.insert({'endpoint': '/ping', 'timestamp': timestamp})

def insert_echo_log(data):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.insert({'endpoint': '/echo', 'data': data, 'timestamp': timestamp})

def get_all_logs():
    return db.all()

def insert_log(command):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.insert({'command': command, 'timestamp': timestamp})