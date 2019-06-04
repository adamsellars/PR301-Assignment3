from view.abstract_help_message import AbstractHelpMessage


class PrintFileHelp(AbstractHelpMessage):
    def display_message(self):
        print(
            self.banner +
            "\nprint_file command help\n" +
            self.banner +
            "\nDescription: Print a PEP8 format text into the interpreter\n"
            "Syntax: print_file\n"
            "Example: print_file test4.txt\n"
        )
