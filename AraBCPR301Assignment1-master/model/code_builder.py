from abc import ABCMeta, abstractmethod


# abstract builder
class CodeBuilder(metaclass=ABCMeta):

    def __init__(self):
        self.result = ""
        self.class_attributes = []

    def get_result(self):
        return self.result

    def clear_result(self):
        self.result = ""
        self.class_attributes = []

    @abstractmethod
    def generate_class_name(self, class_data):
        pass

    @abstractmethod
    def generate_attributes(self, class_data):
        pass

    @abstractmethod
    def generate_methods(self, class_data):
        pass

    @abstractmethod
    def generate_imports(self, class_data):
        pass



