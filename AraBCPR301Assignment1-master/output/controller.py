from .classfinder import ClassFinder
from .filehandler import FileHandler
from .pep8converter import PEP8Converter
from .view import View
from .commandlineinterpreter import CommandLineInterpreter


class Controller:

    def __init__(self, class_finder: ClassFinder, view: View) -> None:
        self.my_command_line_interpreter = CommandLineInterpreter    
        self.data = str    
        self.pep8_content = str    
        self.my_class_finder = class_finder    
        self.my_view = view    
        self.all_my_classes = list    
    
    def start_menu(self) -> str:
        pass

    def find_all(self) -> str:
        pass

    def write_all(self, directory_name: str) -> None:
        pass

    def command_line_interpreter(self) -> None:
        pass

    def read_file_from_path(self, path: str) -> None:
        pass

    def write_file_to_path(self, path: str) -> None:
        pass

    def print_file_to_interpreter(self) -> str:
        pass

    def prep_pep8(self) -> None:
        pass

    def get_class_names(self) -> list:
        pass


object1 = ClassFinder()
object2 = FileHandler()
object3 = PEP8Converter()
object4 = View()
object5 = CommandLineInterpreter()
