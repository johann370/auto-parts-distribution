from CLI import CLI
from InventoryManager import InventoryManager
from SQLiteInventoryDatabase import SQLiteInventoryDatabase


def main():
    ui = CLI()
    database = SQLiteInventoryDatabase(database='CarParts.db')
    im = InventoryManager(ui, database)
    im.display_parts()
    im.delete_part()


if __name__ == '__main__':
    main()
