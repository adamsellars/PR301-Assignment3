from view.abstract_help_message import AbstractHelpMessage


class LoadFileHelp(AbstractHelpMessage):
    def display_message(self):
        print(
            self.banner +
            "\nload_file command help\n" +
            self.banner +
            "\nDescription: Load a .txt file into the program\n"
            "Syntax: load_file [path]\n"
            "Parameter: [path] = full path name of the file starting from the root directory of this program\n"
            "Example: load_file test4(myowncode).txt\n"
        )
