import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        base = Base(id=1)
        self.assertEqual(base.id, 1)

    def test_init_without_id(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_to_json_string_with_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_with_list(self):
        base1 = Base(id=1)
        base2 = Base(id=2)
        json_string = Base.to_json_string([base1.to_dictionary(), base2.to_dictionary()])
        self.assertEqual(json_string, '[{"id": 1}, {"id": 2}]')

    def test_from_json_string_with_empty_string(self):
        dict_list = Base.from_json_string("")
        self.assertEqual(dict_list, [])

    def test_from_json_string_with_json_string(self):
        json_string = '[{"id": 1}, {"id": 2}]'
        dict_list = Base.from_json_string(json_string)
        self.assertEqual(dict_list, [{"id": 1}, {"id": 2}])

    def test_create_rectangle(self):
        rectangle_dict = {"id": 1, "width": 10, "height": 5}
        rectangle = Base.create(**rectangle_dict)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 5)

    def test_create_square(self):
        square_dict = {"id": 1, "size": 5}
        square = Base.create(**square_dict)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 5)

    def test_load_from_file_with_existing_file(self):
        # Assuming Rectangle.json file exists and contains valid JSON data
        rectangles = Base.load_from_file()
        self.assertIsInstance(rectangles, list)
        for rectangle in rectangles:
            self.assertIsInstance(rectangle, Base)

    def test_load_from_file_with_non_existing_file(self):
        # Assuming NonExistingFile.json does not exist
        non_existing_file_instances = Base.load_from_file()
        self.assertEqual(non_existing_file_instances, [])


if __name__ == '__main__':
    unittest.main()
