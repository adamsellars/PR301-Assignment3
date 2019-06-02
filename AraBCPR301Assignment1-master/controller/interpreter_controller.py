from view.console_view import ConsoleView
from view.file_handler import FileHandler
from model.class_finder import ClassFinder
from model.pep8_converter import PEP8Converter
from view.command_line_interpreter import CommandLineInterpreter
from model.database import SQL
from model.pickle import Pickler
from model.code_generator import CodeGenerator
from model.python_builder import PythonBuilder


class InterpreterController:

    def __init__(self, class_finder: object, view: object) -> None:
        self.my_class_finder = class_finder
        self.my_view = view
        self.all_my_classes = []
        self.my_command_line_interpreter = CommandLineInterpreter(self)
        self.data = ""
        self.pep8_content = ""
        self.incorrect_input = True

    def start_menu(self) -> None:
        menu_options = {"1": self.load_text_file, "2": self.write_file_to_code,
                        "3": self.command_line_interpreter, "4": self.write_to_database,
                        "5": self.print_to_screen, "6": self.pickle_file, "7": self.load_pickled_file,
                        "8": self.exit_program}
        while self.incorrect_input:
            self.my_view.print_menu()
            user_input = self.my_view.get_user_menu_option()
            if user_input in menu_options:
                current_option = menu_options.get(user_input)
                current_option()
            else:
                self.my_view.user_has_wrong_input()

    def load_pickled_file(self):
        if self.data is not "":
            pickle_content = Pickler.unpickle_file()
            if self.check_errors(pickle_content) == 0:
                self.my_view.print_my_pickle_content(pickle_content)
                self.my_view.file_loaded_message()
        else:
            self.my_view.file_not_loaded_warning()

    def check_errors(self, content):
        error_count = 0
        if content == PermissionError:
            self.my_view.user_has_no_file_permission()
            error_count += 1
        elif content == FileNotFoundError:
            self.my_view.file_not_found_message()
            error_count += 1
        elif content == Exception:
            self.my_view.generic_error_message()
            error_count += 1
        return error_count

    def exit_program(self):
        self.incorrect_input = False
        self.my_view.exit_program()

    def load_text_file(self):
        self.data = FileHandler.read_file()
        if self.check_errors(self.data) == 0:
            self.my_view.file_loaded_message()

    def write_file_to_code(self):
        directory_name = FileHandler.choose_directory()
        if self.data is not "":
            self.find_all()
            if self.check_errors(self.data) == 0:
                self.write_all(directory_name)
        elif directory_name == FileNotFoundError:
            self.my_view.exit_file_directory()
        else:
            self.my_view.file_not_loaded_warning()

    def write_to_database(self):
        if self.data is not "":
            error_message = SQL.connect_to_db("assignment1")
            if self.check_errors(error_message) == 0:
                SQL.c.execute("""DROP TABLE if exists class;""")
                SQL.create_class_table()
                classes = self.get_class_names()
                SQL.insert_data_into_table(classes)
                self.my_view.database_connected_message()
        else:
            self.my_view.file_not_loaded_warning()

    def print_to_screen(self):
        if self.data is not "":
            sql_database_table = SQL.fetch_all_class_data()
            if self.check_errors(sql_database_table) == 0:
                self.my_view.read_database_file(sql_database_table)
        else:
            self.my_view.file_not_loaded_warning()

    def pickle_file(self):
        self.data = FileHandler.read_file()
        if self.check_errors(self.data) == 0:
            self.my_view.file_loaded_message()
            self.prep_pep8()
            pickle_status = Pickler.pickle_file(self.pep8_content)
            if self.check_errors(pickle_status) == 0:
                self.my_view.pickle_success_message()

    def find_all(self) -> None:
        self.my_class_finder.find_class(self.data)
        self.my_class_finder.relationship_finder(self.data)
        self.all_my_classes = self.my_class_finder.get_all_my_classes()

    def write_all(self, directory_name) -> None:
        assert type(directory_name) is str, "write_all method directory_name must be a string"
        write_file_status = ""
        # client code for builder
        # client creates concrete builder
        python_builder = PythonBuilder()
        # client creates director
        code_generator = CodeGenerator()
        # client chooses the builder for director
        code_generator.set_builder(python_builder)
        for a_plant_class in self.all_my_classes:
            code_generator.generate_code(a_plant_class)
            # client gets the product from the concrete builder via a get method
            content = python_builder.get_result()
            print(content)
            write_file_status = FileHandler.write_file(directory_name, content, a_plant_class)
        if write_file_status == TypeError:
            self.my_view.exit_file_directory()
        else:
            self.my_view.files_written_message()

    def command_line_interpreter(self):
        self.my_command_line_interpreter.do_greet("user")
        self.my_command_line_interpreter.cmdloop()

    def read_file_from_path(self, path):
        self.data = FileHandler.read_file_from_path(path)

    def write_file_to_path(self, path):
        self.find_all()
        for a_plant_class in self.all_my_classes:
            self.pep8_content = PEP8Converter.create_class(a_plant_class)
            FileHandler.write_file_to_path(path, self.pep8_content, a_plant_class)

    def print_file_to_interpreter(self):
        if self.data is not "":
            self.find_all()
            pep8 = ""
            for a_plant_class in self.all_my_classes:
                pep8 += PEP8Converter.create_class(a_plant_class) + "\n"
            assert type(pep8) is str, "print_file_to_interpreter method must return a string"
            return pep8
        else:
            return "\nNo file loaded\n"

    def prep_pep8(self):
        self.find_all()
        pep8 = ""
        for a_plant_class in self.all_my_classes:
            pep8 += PEP8Converter.create_class(a_plant_class) + "\n"
        self.pep8_content = pep8

    def get_class_names(self):
        class_list = []
        counter = 1
        for aClass in self.all_my_classes:
            database_format = []
            class_name = aClass.class_name
            database_format.append("{}".format(counter))
            database_format.append(class_name)
            counter += 1
            class_list.append(database_format)
        assert type(class_list) is list, "get_class_names method must return a list"
        return class_list


# Leroi wrote this
def start_cmd():
    if __name__ == "__main__":
        view = ConsoleView()
        class_finder = ClassFinder()
        controller = InterpreterController(class_finder, view)
        controller.start_menu()


if __name__ == "__main__":
    start_cmd()
