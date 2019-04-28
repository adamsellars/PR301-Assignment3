import unittest
from view.file_handler import FileHandler
from model.class_finder import ClassFinder
from model.class_maker import NewClass
from model.pep8_converter import PEP8Converter


# ---------------------------------Created by Leroi------------------------------------------------
class FileHandlerTests(unittest.TestCase):

    # test case 1 read_file_from_path returns a String from a valid file path
    def test_01(self):
        # arrange
        test = FileHandler()
        # act
        result = test.read_file_from_path("valid.txt")
        # assert
        self.assertTrue(isinstance(result, str), "When given a valid file path a string should be returned")

    # test case 2 read_file_from_path exception handling prevents file not found error from invalid file path
    def test_02(self):
        # Arrange
        test = FileHandler()
        # Act
        try:
            test.read_file_from_path("doesnt_exist.txt")
        # Assert
        except FileNotFoundError:
            self.fail("Exception handling failed to handle file not found error")

    # test case 3 read_file_from_path prevents a permission exception from an file with no read permission
    def test_03(self):
        # Arrange
        test = FileHandler()
        # Act
        try:
            test.read_file_from_path("no_permission.txt")
        # Assert
        except PermissionError:
            self.fail("Exception handling failed to handle permission error")


class ClassMakerTests(unittest.TestCase):
    # Test __str__ method
    def test_04(self):
        # Arrange
        test = NewClass("test_class")
        # Act
        result = test.__str__()
        # Assert
        self.assertEqual(result, "test_class")

    # Test add_method
    def test_05(self):
        # Arrange
        test = NewClass("test_class")
        # Act
        test.add_method("do_stuff()")
        result = test.method[-1]
        # Assert
        self.assertEqual(result, "do_stuff()")

    # Test that multiple methods can be added
    def test_06(self):
        # Arrange
        test = NewClass("test_class")
        count = 0
        # Act
        while count <= 100:
            test.add_method("do_stuff_" + str(count) + "()")
            count += 1
        # Assert
        self.assertEqual(test.method[0], "do_stuff_0()")
        self.assertEqual(test.method[-1], "do_stuff_100()")

    # Test add_attribute
    def test_07(self):
        # Arrange
        test = NewClass("test_class")
        # Act
        test.add_attribute("attribute1 : String")
        result = test.attribute[-1]
        # Assert
        self.assertEqual(result, "attribute1 : String")

    # Test that multiple methods can be added
    def test_08(self):
        # Arrange
        test = NewClass("test_class")
        count = 0
        # Act
        while count <= 100:
            test.add_attribute("attribute" + str(count))
            count += 1
        # Assert
        self.assertEqual(test.attribute[0], "attribute0")
        self.assertEqual(test.attribute[-1], "attribute100")

    # Test add_relationship
    def test_09(self):
        # Arrange
        test = NewClass("test_class")
        # Act
        test.add_relationship("class1 *-- class2")
        result = test.relationship[-1]
        # Assert
        self.assertEqual(result, "class1 *-- class2")

    # Test that multiple and different types of relationships can be added
    def test_10(self):
        # Arrange
        test = NewClass("test_class")
        # Act
        test.add_relationship("class1 *-- class2")
        test.add_relationship("class1 o-- class3")
        test.add_relationship("class1 *-- class4")
        # Assert
        self.assertEqual(test.relationship[0], "class1 *-- class2")
        self.assertEqual(test.relationship[1], "class1 o-- class3")
        self.assertEqual(test.relationship[2], "class1 *-- class4")


# ---------------------------------Created by Adam-------------------------------------------------
class ClassFinderTests(unittest.TestCase):

    # check that classes have been added
    def test_11(self):
        # Arrange
        test = ClassFinder()
        with open("test4.txt") as file:
            test_data = file.read()
        # Act
        test.find_class(test_data)
        # Assert
        self.assertGreater(test.my_classes.__len__(), 0, "my_classes List should not be empty")

    # check that the correct number of classes are added
    def test_12(self):
        # Arrange
        test = ClassFinder()
        with open("test4.txt") as file:
            test_data = file.read()
        # Act
        test.find_class(test_data)
        # Assert
        self.assertEqual(test.my_classes.__len__(), 8)

    # check that the first added class has the correct class name
    def test_13(self):
        # Arrange
        test = ClassFinder()
        with open("test4.txt") as file:
            test_data = file.read()
        # Act
        test.find_class(test_data)
        first_class = test.my_classes[0].class_name
        # Assert
        self.assertEqual(first_class, "Controller")

    # check that the last added class has the correct class name
    def test_14(self):
        # Arrange
        test = ClassFinder()
        with open("test4.txt") as file:
            test_data = file.read()
        # Act
        test.find_class(test_data)
        last_class = test.my_classes[-1].class_name
        # Assert
        self.assertEqual(last_class, "CommandLineInterpreter")

    # check that the first classes attributes are correctly added
    def test_15(self):
        # Arrange
        test = ClassFinder()
        with open("test4.txt") as file:
            test_data = file.read()
        # Act
        test.find_class(test_data)
        first_class_attributes = test.my_classes[0].attribute
        # Assert
        self.assertEqual(first_class_attributes, ['my_command_line_interpreter : CommandLineInterpreter',
                                                  'data : None', 'pep8_content : None',
                                                  'my_class_finder : class_finder', 'my_view : view',
                                                  'all_my_classes : list'])

    # check that the last classes attributes are correctly added
    def test_16(self):
        # Arrange
        test = ClassFinder()
        with open("test4.txt") as file:
            test_data = file.read()
        # Act
        test.find_class(test_data)
        last_class_attributes = test.my_classes[-1].attribute
        # Assert
        self.assertEqual(last_class_attributes, ['prompt : String', 'my_controller : controller', 'banner : string'])

    # check that the first classes methods are correctly added
    def test_17(self):
        # Arrange
        test = ClassFinder()
        with open("test4.txt") as file:
            test_data = file.read()
        # Act
        test.find_class(test_data)
        first_class_methods = test.my_classes[0].method
        # Assert
        self.assertEqual(first_class_methods, [" __init__(self, class_finder: ClassFinder, view: View): None",
                                               "start_menu(self): None",
                                               "find_all(self): None",
                                               " write_all(self, directory_name: String): None",
                                               "command_line_interpreter(self): None",
                                               " read_file_from_path(self, path: String): None",
                                               " write_file_to_path(self, path: String): None",
                                               "print_file_to_interpreter(self): String",
                                               "prep_pep8(self): None",
                                               "get_class_names(self): List"])

    # check that the last classes methods are correctly added
    def test_18(self):
        # Arrange
        test = ClassFinder()
        with open("test4.txt") as file:
            test_data = file.read()
        # Act
        test.find_class(test_data)
        last_class_methods = test.my_classes[-1].method
        # Assert
        self.assertEqual(last_class_methods, [' __init__(self, controller: Controller): None',
                                              ' do_load_self(self, path: String): None',
                                              ' do_write_file(self, path: String): None',
                                              'help_print_file(self): None',
                                              'help_write_file(self): None',
                                              'help_load_file(self): None',
                                              'help_quit(self): None',
                                              'help_greet(self): None',
                                              ' do_greet(self, line: None): None',
                                              ' do_print_file(self, line: None): None',
                                              ' do_quit(self, line: None): None'])

    # check that a classes relationship is correctly added
    def test_19(self):
        # Arrange
        test = ClassFinder()
        with open("test4.txt") as file:
            test_data = file.read()
        # Act
        test.find_class(test_data)
        test.relationship_finder(test_data)
        class_relationship = test.my_classes[0].relationship
        # Assert
        self.assertEqual(class_relationship, ["-- ClassFinder", "-- FileHandler", "-- PEP8Converter", "-- View"])


class PEP8ConverterTests(unittest.TestCase):

    # Test convert_class
    def test_20(self):
        # Arrange
        test = PEP8Converter()
        # Act
        result = test.convert_class("controller")
        # Assert
        self.assertEqual(result, "class controller:\n")

    # Test convert_attribute
    def test_21(self):
        # Arrange
        test = PEP8Converter()
        # Act
        result = test.convert_attribute("attribute : String")
        # Assert
        self.assertEqual(result, "    self.attribute = str    \n    ")

    # Test convert_method
    def test_22(self):
        # Arrange
        test = PEP8Converter()
        # Act
        result = test.convert_method("get_all_my_classes(self) : list")
        # Assert
        self.assertEqual(result, "\n    def get_all_my_classes(self) ->: list:\n        pass\n")

    # Test create_relationship
    def test_23(self):
        # Arrange
        test = PEP8Converter()
        # Act
        result = test.create_relationship("controller o-- ClassFinder", 0)
        # Assert
        self.assertEqual(result, "\nobject0 = o--()")

    def test_24(self):
        # Arrange
        test = PEP8Converter()
        # Act
        result = test.create_relationship("controller -- ClassFinder", 0)
        # Assert
        self.assertEqual(result, "\nobject0 = --()")


if __name__ == '__main__':
    unittest.main(verbosity=2)  # with more details
    # unittest.main()
