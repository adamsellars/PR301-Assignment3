import unittest
from model.class_finder import ClassFinder


class ClassFinderTests(unittest.TestCase):

    # check that classes have been added
    def test_classes_added(self):
        # Arrange
        test = ClassFinder()
        with open("test4.txt") as file:
            test_data = file.read()
        # Act
        test.find_class(test_data)
        # Assert
        self.assertGreater(test.my_classes.__len__(), 0, "my_classes List should not be empty")

    # check that the correct number of classes are added
    def test_correct_number_of_classes(self):
        # Arrange
        test = ClassFinder()
        with open("test4.txt") as file:
            test_data = file.read()
        # Act
        test.find_class(test_data)
        # Assert
        self.assertEqual(test.my_classes.__len__(), 8)

    # check that the first added class has the correct class name
    def test_first_class_name_correct(self):
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
    def test_last_class_name_correct(self):
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
    def test_first_class_correct_attributes(self):
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
    def test_last_class_correct_attributes(self):
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
    def test_first_class_correct_methods(self):
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

    def test_get_all_my_classes(self):
        # Arrange
        test = ClassFinder()
        with open("test4.txt") as file:
            test_data = file.read()
        # Act
        test.find_class(test_data)
        result = test.get_all_my_classes()
        # Assert
        self.assertIsInstance(result, list)

    # check that the last classes methods are correctly added
    def test_last_class_correct_methods(self):
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
    def test_class_relationship(self):
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
        cov.stop()
        cov.save()
        cov.html_report()


if __name__ == "__main__":
    import coverage
    cov = coverage.Coverage()
    cov.start()
    unittest.main(verbosity=2)  # with more details
