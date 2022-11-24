from flask import Flask
from sqlite_inventory_database import SQLiteInventoryDatabase
import json
import sqlite3

app = Flask(__name__)


@app.route('/parts', methods=['GET'])
def get_parts():
    connection = sqlite3.connect('CarParts.db')
    inventory_database = SQLiteInventoryDatabase(connection)

    car_parts = inventory_database.get_all_data().values()
    car_parts_json = []

    for part in car_parts:
        car_parts_json.append(part.__dict__)

    connection.close()
    return json.dumps(car_parts_json)
