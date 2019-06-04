from view.abstract_help_message import AbstractHelpMessage


class GreetHelp(AbstractHelpMessage):
    def display_message(self):
        print(
            self.banner +
            "\ngreet command help\n" +
            self.banner +
            "\nDescription: A Greeting message\n"
            "Syntax: greet\n"
            "Parameter: none\n"
            "Example: greet\n"
        )
