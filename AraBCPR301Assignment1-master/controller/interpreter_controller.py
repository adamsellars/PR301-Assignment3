from view.console_view import ConsoleView
from view.file_handler import FileHandler
from model.class_finder import ClassFinder
from model.pep8_converter import PEP8Converter
from view.command_line_interpreter import CommandLineInterpreter
from model.database import SQL
from model.pickle import Pickler


class InterpreterController:

    def __init__(self, class_finder: object, view: object) -> None:
        self.my_class_finder = class_finder
        self.my_view = view
        self.all_my_classes = []
        self.my_command_line_interpreter = CommandLineInterpreter(self)
        self.data = ""
        self.pep8_content = ""

    def start_menu(self) -> None:
        incorrect_input = True
        while incorrect_input:
            self.my_view.print_menu()
            user_input = self.my_view.get_user_menu_option()

            # Press 1 to load your text file
            if user_input == "1":
                self.data = FileHandler.read_file()
                if self.data == FileNotFoundError:
                    self.my_view.file_not_found_message()
                else:
                    self.my_view.file_loaded_message()

            # Press 2 to write from plantuml text to python code
            elif user_input == "2":
                if self.data is not "":
                    self.find_all()
                    directory_name = FileHandler.choose_directory()
                    if directory_name == TypeError:
                        self.my_view.file_not_found_message()
                    elif directory_name == Exception:
                        self.my_view.generic_error_message()
                    else:
                        self.write_all(directory_name)

                elif directory_name == FileNotFoundError:
                    self.my_view.exit_file_directory()
                else:
                    self.my_view.file_not_loaded_warning()

            # Press 3 to start command line interpreter
            elif user_input == "3":
                self.command_line_interpreter()

            # Press 4 to write file to data base
            elif user_input == "4":
                if self.data is not "":
                    error_message = SQL.connect_to_db("assignment1")
                    if error_message == PermissionError:
                        self.my_view.user_has_no_file_permission()
                    elif error_message == FileNotFoundError:
                        self.my_view.file_not_found_message()
                    elif error_message == Exception:
                        self.my_view.generic_error_message()
                    else:
                        SQL.c.execute("""DROP TABLE if exists class;""")
                        SQL.create_class_table()
                        classes = self.get_class_names()
                        SQL.insert_data_into_table(classes)
                        self.my_view.database_connected_message()
                else:
                    self.my_view.file_not_loaded_warning()

            # Press 5 to print PEP8 class file to screen from database
            elif user_input == "5":
                if self.data is not "":
                    sql_database_table = SQL.fetch_all_class_data()
                    if sql_database_table == PermissionError:
                        self.my_view.user_has_no_file_permission()
                    elif sql_database_table == FileNotFoundError:
                        self.my_view.file_not_found_message()
                    elif sql_database_table == Exception:
                        self.my_view.generic_error_message()
                    else:
                        self.my_view.read_database_file(sql_database_table)
                else:
                    self.my_view.file_not_loaded_warning()

            # Press 6 to load text file, convert data to PEP8 python format then convert file to pickle
            # format in same directory
            elif user_input == "6":
                self.data = FileHandler.read_file()
                if self.data == FileNotFoundError:
                    self.my_view.file_not_found_message()
                else:
                    self.my_view.file_loaded_message()
                    self.prep_pep8()
                    pickle_status = Pickler.pickle_file(self.pep8_content)
                    if pickle_status == PermissionError:
                        self.my_view.user_has_no_file_permission()
                    elif pickle_status == FileNotFoundError:
                        self.my_view.file_not_found_message()
                    elif pickle_status == Exception:
                        self.my_view.generic_error_message()
                    else:
                        self.my_view.pickle_success_message()

            # Press 7 to load data from pickle file
            elif user_input == "7":
                if self.data is not "":
                    pickle_content = Pickler.unpickle_file()
                    if pickle_content == PermissionError:
                        self.my_view.user_has_no_file_permission()
                    elif pickle_content == FileNotFoundError:
                        self.my_view.file_not_found_message()
                    elif pickle_content == Exception:
                        self.my_view.generic_error_message()
                    else:
                        self.my_view.print_my_pickle_content(pickle_content)
                        self.my_view.file_loaded_message()
                else:
                    self.my_view.file_not_loaded_warning()

            # Exit
            elif user_input == "8":
                incorrect_input = False
                self.my_view.exit_program()

            else:
                self.my_view.user_has_wrong_input()

    def find_all(self) -> None:
        self.my_class_finder.find_class(self.data)
        self.my_class_finder.relationship_finder(self.data)
        self.all_my_classes = self.my_class_finder.get_all_my_classes()

    def write_all(self, directory_name) -> None:
        assert type(directory_name) is str, "write_all method directory_name must be a string"
        write_file_status = ""
        for a_plant_class in self.all_my_classes:
            content = PEP8Converter.create_class(a_plant_class)
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
