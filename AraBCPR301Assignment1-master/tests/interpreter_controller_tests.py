import unittest
from view.console_view import ConsoleView
import contextlib
from unittest import mock
from unittest.mock import MagicMock
from unittest.mock import patch
from io import StringIO
from view.file_handler import FileHandler
# from model.exception_handler import ErrorHandler
from model.class_finder import ClassFinder
from controller.interpreter_controller import InterpreterController


class InterpreterControllerUnitTests(unittest.TestCase):

    def test_interpreter_controller_load_text_file_exit_dialogue(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        temp_stdout = StringIO()
        expected = "Error, file not found"
        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."
        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.load_text_file()
        actual = temp_stdout.getvalue().strip()  # std.getvalue gets some extra spaces
        self.assertEqual(actual, expected, failure_msg.format(actual, expected))

    def test_interpreter_controller_start_menu(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        user_input = "8"
        expected = None
        interpreter_controller = InterpreterController(class_finder, view)
        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."

        with patch('builtins.input', side_effect=user_input):
            actual = interpreter_controller.start_menu()
        self.assertEqual(actual, expected, failure_msg.format(actual, expected))

    @mock.patch('controller.interpreter_controller', create=True)
    def test_interpreter_controller_start_menu_correct_input(self, mocked_input):
        class_finder = ClassFinder()
        view = ConsoleView()
        user_input = ["9", "enter", "8"]
        interpreter_controller = InterpreterController(class_finder, view)
        with patch('builtins.input', side_effect=user_input):
            actual = interpreter_controller.start_menu()
        expected = None
        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."
        self.assertEqual(actual, expected, failure_msg.format(actual, expected))
    
    def test_interpreter_controller_translate_uml_to_python_code_no_plant_text_loaded(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        temp_stdout = StringIO()
        expected = "Must load a file first"
        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."
        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.write_file_to_code()
        actual = temp_stdout.getvalue().strip()  # std.getvalue gets some extra spaces
        self.assertEqual(actual, expected, failure_msg.format(actual, expected))

    def test_translate_uml_to_python_code_select_to_delete_dir(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        path = 'plant.txt'
        with open(path, 'r') as file:
            data = file.read()
            #test_data = data.split()
        interpreter_controller.data = data
        interpreter_controller.find_all()
        temp_stdout = StringIO()
        expected = "files have been written in chosen directory"

        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."
        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.write_file_to_code()
        actual = temp_stdout.getvalue().strip()  # std.getvalue gets some extra spaces
        self.assertEqual(actual, expected, failure_msg.format(actual, expected))
    
    @mock.patch('controller.interpreter_controller', create=True)
    def test_interpreter_controller_start_cmd(self, line):
        class_finder = ClassFinder()
        view = ConsoleView()
        user_input = ["quit"]
        interpreter_controller = InterpreterController(class_finder, view)
        with patch('builtins.input', side_effect=user_input):
            actual = interpreter_controller.command_line_interpreter()
        expected = None

        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."

        self.assertEqual(actual, expected, failure_msg.format(actual, expected))
    
    def test_write_file_to_database_no_file_loaded(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        temp_stdout = StringIO()
        expected = "Must load a file first"

        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."
        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.write_to_database()
        actual = temp_stdout.getvalue().strip()  # std.getvalue gets some extra spaces
        self.assertEqual(actual, expected, failure_msg.format(actual, expected))
    
    def test_print_database_file_to_console_with_no_data(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        temp_stdout = StringIO()
        interpreter_controller.my_db = "assignment1"
        expected = "Must load a file first"
        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."
        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.print_to_screen()
        actual = temp_stdout.getvalue().strip()  # std.getvalue gets some extra spaces
        self.assertEqual(actual, expected, failure_msg.format(actual, expected))
    
    def test_load_file_to_pickle_exit_dialogue(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        temp_stdout = StringIO()
        expected = "Error, file not found"
        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."
        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.pickle_file()
        actual = temp_stdout.getvalue().strip()  # std.getvalue gets some extra spaces
        self.assertEqual(actual, expected, failure_msg.format(actual, expected))

    '''
    def test_read_from_pickle_file_read_from_no_permission_pickle(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        temp_stdout = StringIO()
        interpreter_controller.data = "mock data"
        interpreter_controller.my_pickle = "no_permission.pickle"
        expected = "You have no permission"

        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."
        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.load_pickled_file()
        actual = temp_stdout.getvalue().strip()  # std.getvalue gets some extra spaces
        self.assertEqual(actual, expected, failure_msg.format(actual, expected))

    
    def test_read_from_pickle_file_read_with_no_data(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        temp_stdout = StringIO()
        expected = "Must load a file first"

        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."
        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.load_pickled_file()
        actual = temp_stdout.getvalue().strip()  # std.getvalue gets some extra spaces

        self.assertEqual(actual, expected, failure_msg.format(actual, expected))
    
    def test_read_from_pickle_file(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        temp_stdout = StringIO()
        expected = "class PlantEater:\n\n    def __init__() -> None:\n    \n\nFile loaded"
        path = 'pickle_test.txt'
        with open(path, 'r') as file:
            data = file.read()
            test_data = data.split()
        interpreter_controller.data = test_data
        interpreter_controller.find_all()

        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."
        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.read_from_pickle_file()
        actual = temp_stdout.getvalue().strip()  # std.getvalue gets some extra spaces
        self.assertEqual(actual, expected, failure_msg.format(actual, expected))
        
    def test_translate_uml_to_python_code__exit_dialogue(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        interpreter_controller.data = "stuff"
        temp_stdout = StringIO()
        expected = "Exiting file directory dialogue..."
        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."
        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.write_file_to_code()
        actual = temp_stdout.getvalue().strip()  # std.getvalue gets some extra spaces
        self.assertEqual(actual, expected, failure_msg.format(actual, expected))
        
    def test_print_database_file_to_console_with_data(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        path = 'plant.txt'
        with open(path, 'r') as file:
            data = file.read()
            test_data = data.split()
        interpreter_controller.data = test_data
        interpreter_controller.find_all()
        temp_stdout = StringIO()
        interpreter_controller.my_db = "assignment1"
        expected = "('1', 'ManEater')\n('2', 'AnimalEater')\n('3', 'PlantEater')"
        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."
        interpreter_controller.write_file_to_database()
        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.print_database_file_to_console()
        actual = temp_stdout.getvalue().strip()  # std.getvalue gets some extra spaces

        self.assertEqual(actual, expected, failure_msg.format(actual, expected))
        
    def test_print_database_file_to_console_with_corrupt_data(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        interpreter_controller.data = "corruptdata"
        temp_stdout = StringIO()
        # interpreter_controller.my_db = "assignment2"
        expected = "Must load a file first"
        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."
        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.print_to_screen()
        actual = temp_stdout.getvalue().strip()  # std.getvalue gets some extra spaces

        self.assertEqual(actual, expected, failure_msg.format(actual, expected))
        
    def test_load_file_to_pickle_with_valid_text_file(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        temp_stdout = StringIO()
        interpreter_controller.my_pickle = "no_permission.pickle"
        expected = "File loaded\nYou have no permission"

        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."
        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.pickle_file()
        actual = temp_stdout.getvalue().strip()  # std.getvalue gets some extra spaces
        self.assertEqual(actual, expected, failure_msg.format(actual, expected))
        
    def test_load_file_to_pickle_with_test_data(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        temp_stdout = StringIO()
        expected = "File loaded\nPickled successfully"

        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."
        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.load_pickled_file()
        actual = temp_stdout.getvalue().strip()  # std.getvalue gets some extra spaces
        self.assertEqual(actual, expected, failure_msg.format(actual, expected))
        
    def test_write_file_to_database_file_connects_to_database(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        path = 'plant.txt'
        with open(path, 'r') as file:
            data = file.read()
            test_data = data.split()
        interpreter_controller.data = test_data
        interpreter_controller.find_all()
        temp_stdout = StringIO()
        interpreter_controller.my_db = "assignment1"
        expected = "Opened database successfully\nFinishing connecting to database"
        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."

        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.write_file_to_database()
        actual = temp_stdout.getvalue().strip()  # std.getvalue gets some extra spaces

        self.assertEqual(actual, expected, failure_msg.format(actual, expected))
        
    def test_write_file_to_database_file_loaded_raises_error(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        path = 'plant.txt'
        with open(path, 'r') as file:
            data = file.read()
            test_data = data.split()
        interpreter_controller.data = test_data
        interpreter_controller.find_all()
        temp_stdout = StringIO()
        interpreter_controller.my_db = 0
        expected = "Incorrect Type"
        failure_msg = "\nThe actual input: \n{0}\nshould actually print\n{1}."

        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.write_file_to_database()
        actual = temp_stdout.getvalue().strip()  # std.getvalue gets some extra spaces

        self.assertEqual(actual, expected, failure_msg.format(actual, expected))
        
    def test_interpreter_controller_load_text_file(self):
        class_finder = ClassFinder()
        view = ConsoleView()
        interpreter_controller = InterpreterController(class_finder, view)
        temp_stdout = StringIO()
        expected = "File loaded"
        with contextlib.redirect_stdout(temp_stdout):
            interpreter_controller.load_text_file()
        actual = temp_stdout.getvalue().strip()
        self.assertEqual(actual, expected)
    '''

