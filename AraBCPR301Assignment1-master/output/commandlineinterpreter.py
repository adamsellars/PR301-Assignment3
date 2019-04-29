from .controller import Controller


class CommandLineInterpreter:

    def __init__(self, controller: Controller) -> None:
        self.prompt = str    
        self.my_controller = controller    
        self.banner = str    
    
    def do_load_self(self, path: str) -> None:
        pass

    def do_write_file(self, path: str) -> None:
        pass

    def help_print_file(self) -> None:
        pass

    def help_write_file(self) -> None:
        pass

    def help_load_file(self) -> None:
        pass

    def help_quit(self) -> None:
        pass

    def help_greet(self) -> None:
        pass

    def do_greet(self, line: None) -> None:
        pass

    def do_print_file(self, line: None) -> None:
        pass

    def do_quit(self, line: None) -> None:
        pass


object1 = Controller()
