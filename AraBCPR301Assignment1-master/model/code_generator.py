# Director
class CodeGenerator(object):
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def generate_code(self, class_data):
        self.builder.clear_result()
        self.builder.generate_imports(class_data)
        self.builder.generate_class_name(class_data)
        self.builder.generate_attributes(class_data)
        self.builder.generate_methods(class_data)

