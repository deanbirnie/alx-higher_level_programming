import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init_with_valid_arguments(self):
        square = Square(5, 1, 2, 123)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 123)

    def test_init_with_invalid_size(self):
        with self.assertRaises(ValueError) as cm:
            Square(-5, 1, 2, 123)
        self.assertEqual(str(cm.exception), "size must be > 0")

    def test_init_with_invalid_x(self):
        with self.assertRaises(ValueError) as cm:
            Square(5, -1, 2, 123)
        self.assertEqual(str(cm.exception), "x must be >= 0")

    def test_init_with_invalid_y(self):
        with self.assertRaises(ValueError) as cm:
            Square(5, 1, -2, 123)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_display(self):
        square = Square(3)
        expected_output = "###\n###\n###\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            square.display()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_str_representation(self):
        square = Square(5, 1, 2, 123)
        self.assertEqual(str(square), "[Square] (123) 1/2 - 5")

    def test_update_with_no_keyword_arguments(self):
        square = Square(5)
        square.update(1, 10, 3, 4)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_update_with_keyword_arguments(self):
        square = Square(5)
        square.update(id=1, size=10, x=3, y=4)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_to_dictionary(self):
        square = Square(5, 1, 2, 123)
        expected_dict = {'id': 123, 'size': 5, 'x': 1, 'y': 2}
        self.assertEqual(square.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
