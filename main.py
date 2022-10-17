from CLI import CLI
from InventoryManager import InventoryManager
from TestDatabase import TestDatabase


def main():
    ui = CLI()
    database = TestDatabase()
    im = InventoryManager(ui, database)
    im.add_part()
    im.display_parts()
    im.update_part()
    im.display_parts()
    im.delete_part()
    im.display_parts()


if __name__ == '__main__':
    main()
