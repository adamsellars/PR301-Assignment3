from view.abstract_help_message import AbstractHelpMessage


class QuitHelp(AbstractHelpMessage):
    def display_message(self):
        print(
            self.banner +
            "\nquit command help\n" +
            self.banner +
            "\nDescription: terminate the command line interpreter\n"
            "Syntax: quit\n"
            "Parameter: none\n"
            "Example: quit\n"
        )
