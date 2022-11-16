from cli import CLI
from inventory_manager import InventoryManager
from sqlite_inventory_database import SQLiteInventoryDatabase


def main():
    ui = CLI()
    database = SQLiteInventoryDatabase(database='CarParts.db')
    im = InventoryManager(ui, database)
    im.display_parts()
    im.delete_part()


if __name__ == '__main__':
    main()
