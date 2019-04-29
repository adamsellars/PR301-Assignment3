class ConsoleView:

    def print_menu(self) -> None:
        print("\n"
              "------------------------------------------------------\n"
              "Press 1 to load your text file\n"
              "------------------------------------------------------\n"
              "Press 2 to write from plantuml text to python code\n"
              "------------------------------------------------------\n"
              "Press 3 to run the command line interpreter\n"
              "------------------------------------------------------\n"
              "Press 4 to write file to database\n"
              "------------------------------------------------------\n"
              "Press 5 to print class names from database to screen\n"
              "------------------------------------------------------\n"
              "Press 6 to load text file, convert data to PEP8 python\n"
              "        format then convert file to pickle format in\n"
              "        same directory\n"
              "------------------------------------------------------\n"
              "Press 7 to load data from pickle file\n"
              "------------------------------------------------------\n"
              "Press 8 to exit\n"
              "------------------------------------------------------\n"
              "\n")

    def file_not_loaded_warning(self):
        print("Must load a file first")

    def file_empty_warning(self):
        print("File must not be empty")

    def file_type_warning(self):
        print("File must be a .txt file type")

    def exit_file_directory(self):
        print("Exiting file directory dialogue...")

    def user_has_wrong_input(self):
        user_input = input("\nWrong option. Press enter to try again...")
        return user_input

    def exit_program(self):
        print("\ngoodbye..\n")

    def get_user_menu_option(self):
        user_input = input("Please enter your input: ")
        return user_input

    def file_loaded_message(self):
        print("File loaded")

    def file_not_found_message(self):
        print("Error, file not found")

    def user_has_no_file_permission(self):
        print("You have no permission")

    def generic_error_message(self):
        print("Somethings gone wrong...")

    def print_my_pickle_content(self, content):
        print(content)

    def files_written_message(self):
        print("files have been written in chosen directory")

    def database_connected_message(self):
        print("Opened database successfully\nFinishing connecting to database")

    def read_database_file(self, database_file):
        for classes in database_file:
            print(classes)

    def pickle_success_message(self):
        print("Pickled successfully")




