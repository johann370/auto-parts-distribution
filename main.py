from cli import CLI
from inventory_manager import InventoryManager
from sqlite_inventory_database import SQLiteInventoryDatabase
import sqlite3


def main():
    ui = CLI()
    connection = sqlite3.connect('CarParts.db')
    database = SQLiteInventoryDatabase(connection)
    im = InventoryManager(ui, database)


if __name__ == '__main__':
    main()
