class CLI:
    def get_part_info(self) -> dict:
        name = input('Enter part name: ')
        count = int(input('Enter part count: '))
        price = float(input('Enter price: '))
        manufacturer = input('Enter manufacturer: ')
        category = input('Enter category: ')

        return {
            'name': name,
            'count': count,
            'price': price,
            'manufacturer': manufacturer,
            'category': category,
        }

    def get_updated_info(self, part_to_update) -> dict:
        name = input(
            'Enter new part name or Enter for no change: ') or part_to_update.name
        count = int(
            input('Enter new part count or Enter for no change: ') or part_to_update.count)
        price = float(
            input('Enter new price or Enter for no change: ') or part_to_update.price)
        manufacturer = input(
            'Enter new manufacturer or Enter for no change: ') or part_to_update.manufacturer
        category = input(
            'Enter new category or Enter for no change: ') or part_to_update.category
        return {
            'name': name,
            'count': count,
            'price': price,
            'manufacturer': manufacturer,
            'category': category,
        }

    def get_part_to_delete(self) -> int:
        id_to_delete = int(input('Enter id to delete: '))

        return id_to_delete

    def get_part_to_update(self) -> int:
        id_to_update = int(input('Enter id to update: '))

        return id_to_update
