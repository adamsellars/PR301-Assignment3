from view.abstract_help_message import AbstractHelpMessage


class WriteFileHelp(AbstractHelpMessage):
    def display_message(self):
        print(
            self.banner +
            "\nwrite_file command help\n" +
            self.banner +
            "\nDescription: write a PEP8 format .txt file into path chosen\n"
            "Syntax: write_file [path]\n"
            "Parameter: [path] = full path name of the file starting from the root directory of this program\n"
            "Example: write_file test4(myowncode).txt\n"
        )
