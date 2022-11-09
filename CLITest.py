import unittest
from unittest import mock
from CLI import CLI
from CarPart import CarPart


class TestCLI(unittest.TestCase):
    @mock.patch('builtins.input')
    def test_positive_number_input(self, mock_input):
        cli = CLI()
        mock_input.side_effect = [1, 1000,
                                  100000, 5.0, 20.50, 1000.25]

        user_int = cli.get_input_int('')
        self.assertEqual(user_int, 1)

        user_int = cli.get_input_int('')
        self.assertEqual(user_int, 1000)

        user_int = cli.get_input_int('')
        self.assertEqual(user_int, 100000)

        user_float = cli.get_input_float('')
        self.assertEqual(user_float, 5.0)

        user_float = cli.get_input_float('')
        self.assertEqual(user_float, 20.50)

        user_float = cli.get_input_float('')
        self.assertEqual(user_float, 1000.25)

    @mock.patch('builtins.input')
    def test_negative_number_input(self, mock_input):
        cli = CLI()
        mock_input.side_effect = [-10, -1000,
                                  -100000, -20.00, -100.25, -30.33]
        self.assertRaises(ValueError, cli.get_input_int, [''])
        self.assertRaises(ValueError, cli.get_input_int, [''])
        self.assertRaises(ValueError, cli.get_input_int, [''])
        self.assertRaises(ValueError, cli.get_input_float, [''])
        self.assertRaises(ValueError, cli.get_input_float, [''])
        self.assertRaises(ValueError, cli.get_input_float, [''])

    @mock.patch('builtins.input')
    def test_non_number_input(self, mock_input):
        cli = CLI()
        mock_input.side_effect = [
            'abcdef', 'jklfda', '#U$)%)(', 'text', '%*)$@', 'fdsaf']
        self.assertRaises(TypeError, cli.get_input_int, [''])
        self.assertRaises(TypeError, cli.get_input_int, [''])
        self.assertRaises(TypeError, cli.get_input_int, [''])
        self.assertRaises(TypeError, cli.get_input_float, [''])
        self.assertRaises(TypeError, cli.get_input_float, [''])
        self.assertRaises(TypeError, cli.get_input_float, [''])

    @mock.patch('builtins.input')
    def test_get_part_info(self, mock_input):
        cli = CLI()
        mock_input.side_effect = [
            'test name', 200, 50.50, 'test manufacturer', 'test category']

        part_info = cli.get_part_info()

        self.assertEqual(part_info, {'name': 'test name', 'count': 200, 'price': 50.50,
                         'manufacturer': 'test manufacturer', 'category': 'test category'})

    @mock.patch('builtins.input')
    def test_empty_get_part_info(self, mock_input):
        cli = CLI()
        mock_input.side_effect = [
            '', '', '', '', '']

        self.assertRaises(ValueError, cli.get_part_info)

    @mock.patch('builtins.input')
    def test_get_updated_info(self, mock_input):
        cli = CLI()
        mock_input.side_effect = [
            'test name', 200, 50.50, 'test manufacturer', 'test category']

        test_car_part = CarPart(id=1, name='random name', count=20,
                                price=100.00, manufacturer='manu', category='a random category')

        updated_part_info = cli.get_updated_info(test_car_part)

        self.assertEqual(updated_part_info, {'name': 'test name', 'count': 200, 'price': 50.50,
                         'manufacturer': 'test manufacturer', 'category': 'test category'})

    @mock.patch('builtins.input')
    def test_empty_get_updated_info(self, mock_input):
        cli = CLI()
        mock_input.side_effect = [
            '', '', '', '', '']

        test_car_part = CarPart(id=1, name='random name', count=20,
                                price=100.00, manufacturer='manu', category='a random category')

        updated_part_info = cli.get_updated_info(test_car_part)

        self.assertEqual(updated_part_info, {'name': 'random name', 'count': 20,
                         'price': 100.00, 'manufacturer': 'manu', 'category': 'a random category'})
