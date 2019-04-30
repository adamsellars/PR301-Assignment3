import unittest
import coverage
import os
import io
import sys
cov = coverage.Coverage()
cov.start()
from view.file_handler import FileHandler
from model.class_maker import NewClass


class FileHandlerTests(unittest.TestCase):
    # FileHandler tests
    # read_file_from_path
    def setUp(self):
        # be executed before each test
        self.test = FileHandler()

    def tearDown(self):
        # be executed after each test case
        print('down')

    # test case 1 read_file_from_path returns a String from a valid file path
    def test_read_file_from_path_valid(self):
        result = self.test.read_file_from_path("valid.txt")
        self.assertTrue(isinstance(result, str), "When given a valid file path a string should be returned")

    def test_write_file_to_path(self):
        # arrange
        path = ""
        content = "class Controller:" \
                  "    def __init__(self):" \
                  "        data = \"\""
        a_plant_class = NewClass("Controller")
        # act
        result = self.test.write_file_to_path(path, content, a_plant_class)
        expected = None
        # assert
        self.assertEqual(result, expected)

    def test_write_file_to_path_no_directory(self):
        # arrange
        captured_output = io.StringIO()
        sys.stdout = captured_output
        path = ""
        content = "class Controller:" \
                  "    def __init__(self):" \
                  "        data = \"\""
        a_plant_class = NewClass("Controller")
        expected = "File successfully written\n\n"
        # act
        self.test.write_file_to_path(path, content, a_plant_class)
        sys.stdout = sys.__stdout__
        actual = captured_output.getvalue()
        # assert
        self.assertEqual(expected, actual)

    def test_write_file_to_path_wrong_input(self):
        # arrange
        captured_output = io.StringIO()
        sys.stdout = captured_output
        path = 1
        content = "class Controller:" \
                  "    def __init__(self):" \
                  "        data = \"\""
        a_plant_class = NewClass("Controller")
        expected = "File successfully written\n\n"
        # act
        self.test.write_file_to_path(path, content, a_plant_class)
        sys.stdout = sys.__stdout__
        # assert
        self.assertRaises(TypeError)

    def test_write_file_to_path_protected(self):
        # arrange
        path = "protected_folder/controller.py"
        content = "class Controller:" \
                  "    def __init__(self):" \
                  "        data = \"\""
        a_plant_class = NewClass("Controller")
        expected = PermissionError
        # act
        actual = self.test.write_file_to_path(path, content, a_plant_class)
        # assert
        self.assertEqual(expected, actual)

    def test_read_file_from_path_protected(self):
        # arrange
        test = FileHandler()
        path = "protected_folder/controller.py"
        # act
        test.read_file_from_path(path)
        # assert
        self.assertRaises(PermissionError)

    # test case 2 read_file_from_path exception handling prevents file not found error from invalid file path
    def test_02(self):
        try:
            self.test.read_file_from_path("doesnt_exist.txt")
        except FileNotFoundError:
            self.fail("Exception handling failed to handle file not found error")


    # test case 3 read_file_from_path prevents a permission exception from an file with no read permission
    def test_03(self):
        try:
            self.test.read_file_from_path("protected_folder")
        except PermissionError:
            self.fail("Exception handling failed to handle permission error")
        cov.stop()
        cov.save()
        cov.html_report()
        cov.report()

if __name__ == "__main__":
    from view.file_handler import FileHandler
    from model.class_maker import NewClass
    unittest.main(verbosity=2)  # with more details
