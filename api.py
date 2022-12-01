from flask import Flask, request
from sqlite_inventory_database import SQLiteInventoryDatabase
from sqlite_order_database import SQLiteOrderDatabase
import json
import sqlite3
from my_order import Order

app = Flask(__name__)


@app.route('/parts', methods=['GET'])
def get_parts():
    connection = sqlite3.connect(
        '/home/jmdragon370/auto-parts-distribution/AutoPartsDistribution.db')
    inventory_database = SQLiteInventoryDatabase(connection)

    car_parts = inventory_database.get_all_data().values()
    car_parts_json = []

    for part in car_parts:
        car_parts_json.append(part.__dict__)

    connection.close()
    return json.dumps(car_parts_json)


@app.route('/order', methods=['POST'])
def save_order():
    connection = sqlite3.connect(
        '/home/jmdragon370/auto-parts-distribution/AutoPartsDistribution.db')
    order_database = SQLiteOrderDatabase(connection)
    inventory_database = SQLiteInventoryDatabase(connection)

    data = request.json
    new_order = Order(order_id=0, first_name=data['first_name'], last_name=data['last_name'],
                      address=data['address'], car_parts=json.dumps(data['car_parts']), card_number=data['card_number'], total=data['total'])

    order_database.add_order(new_order)

    for part in data['car_parts']:
        inventory_database.lower_count(part['id'], part['count'])

    return 'processed order'


if __name__ == '__main__':
    app.run()
