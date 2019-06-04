from cmd import Cmd
from view.help_display import HelpDisplay
from view.greet_help import GreetHelp
from view.load_file_help import LoadFileHelp
from view.print_file_help import PrintFileHelp
from view.quit_help import QuitHelp
from view.write_file_help import WriteFileHelp


class CommandLineInterpreter(Cmd):
    # Created by Adam
    def __init__(self, controller):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.my_controller = controller
        self.banner = "=====" * 10

    # Created by Adam
    def do_load_file(self, path):
        self.my_controller.read_file_from_path(path)

    # Created by Adam
    def do_write_file(self, path):
        self.my_controller.write_file_to_path(path)

    # Created by Leroi
    def help_print_file(self):
        display = HelpDisplay(PrintFileHelp())
        display.display_message()

    # Created by Leroi
    def help_write_file(self):
        display = HelpDisplay(WriteFileHelp())
        display.display_message()

    # Created by Adam
    def help_load_file(self):
        display = HelpDisplay(LoadFileHelp())
        display.display_message()

    # Created by Adam
    def help_quit(self):
        display = HelpDisplay(QuitHelp())
        display.display_message()

    # Created by Adam
    def help_greet(self):
        display = HelpDisplay(GreetHelp())
        display.display_message()

    # Created by Adam
    def do_greet(self, line):
        print(self.banner + "\nWelcome to the command line interpreter."
                            "\nType help to view available commands\n" + self.banner + "\n")

    # Created by Leroi
    def do_print_file(self, line):
        pep8 = self.my_controller.print_file_to_interpreter()
        print(pep8)

    # Created by Adam
    def do_quit(self, line):
        print("Goodbye thank you for using the command line interpreter")
        return True
