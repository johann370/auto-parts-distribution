class CLI:
    def get_part_info(self) -> dict:
        name = input('Enter part name: ')
        count = self.get_input_int('Enter part count: ')
        price = self.get_input_float('Enter price: ')
        manufacturer = input('Enter manufacturer: ')
        category = input('Enter category: ')

        if not name or not count or not price or not manufacturer or not category:
            raise ValueError("Input can't be empty")

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
        return self.get_input_int('Enter id to delete: ')

    def get_part_to_update(self) -> int:
        return self.get_input_int('Enter id to update: ')

    def get_input_int(self, prompt) -> int:
        input_int = input(prompt)

        if input_int == '':
            return input_int

        if not isinstance(input_int, int):
            raise TypeError('That value is not an integer')

        if input_int < 0:
            raise ValueError('Negative values are not allowed')

        return int(input_int)

    def get_input_float(self, prompt) -> float:
        input_float = input(prompt)

        if input_float == '':
            return input_float

        if not isinstance(input_float, float):
            raise TypeError('That value is not a float')

        if input_float < 0.0:
            raise ValueError('Negative values are not allowed')

        return float(input_float)
