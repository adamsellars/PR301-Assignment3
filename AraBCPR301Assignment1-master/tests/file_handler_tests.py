import unittest
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
    def test_01(self):
        result = self.test.read_file_from_path("valid.txt")
        self.assertTrue(isinstance(result, str), "When given a valid file path a string should be returned")

    def test_write_file_to_path(self):
        # arrange
        test = FileHandler()
        path = "test_path"
        content = "class Controller:" \
                  "    def __init__(self):" \
                  "        data = \"\""
        a_plant_class = NewClass("Controller")
        # act
        test.write_file_to_path(path, content, a_plant_class)
        # assert


    # test case 2 read_file_from_path exception handling prevents file not found error from invalid file path
    def test_02(self):
        try:
            self.test.read_file_from_path("doesnt_exist.txt")
        except FileNotFoundError:
            self.fail("Exception handling failed to handle file not found error")

    # test case 3 read_file_from_path prevents a permission exception from an file with no read permission
    def test_03(self):
        try:
            self.test.read_file_from_path("no_permission.txt")
        except PermissionError:
            self.fail("Exception handling failed to handle permission error")
        cov.stop()
        cov.save()
        cov.html_report()

if __name__ == "__main__":
    import coverage
    cov = coverage.Coverage()
    cov.start()
    unittest.main(verbosity=2)  # with more details
