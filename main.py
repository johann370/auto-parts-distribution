from CLI import CLI
from InventoryManager import InventoryManager
from SQLiteDatabase import SQLiteDatabase
from TestDatabase import TestDatabase


def main():
    ui = CLI()
    database = SQLiteDatabase(database='CarParts.db')
    im = InventoryManager(ui, database)
    im.display_parts()
    im.delete_part()


if __name__ == '__main__':
    main()
