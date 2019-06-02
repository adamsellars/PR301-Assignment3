from model.code_builder import CodeBuilder


# concrete builder
class PythonBuilder(CodeBuilder):

    def generate_class_name(self, class_data):
        converted_class_name = "class {}:\n".format(class_data.class_name)
        self.result += converted_class_name

    def generate_imports(self, class_data):
        if len(class_data.relationship) > 0:
            for a_relationship in class_data.relationship:
                if "--" in a_relationship:
                    relationships = a_relationship.split()
                    import_statement = 'from .{} import {}\n'.format((relationships[1].lower()), relationships[1])
                    self.result += import_statement
            self.result += "\n\n"

    def create_constructor(self, method):
        constructor = self.find_method_data_type(method)
        total_words = len(constructor)
        my_method = self.find_method_details(total_words, constructor)
        pep8_method = "\n    def {}:\n".format(my_method)
        for a_attribute in self.class_attributes:
            pep8_method += "    {}".format(a_attribute)
        self.result += pep8_method

    def build_relationship(self, plant_class_name, class_name, methods):
        counter = 1
        relationship = ""
        import_class = ""
        if (len(plant_class_name.relationship)) > 0:
            for a_relationship in plant_class_name.relationship:
                relationship += self.create_relationship(a_relationship, counter)
                import_class += self.set_import(a_relationship)
                counter += 1
            assert type(import_class) is str, "create_class method must return a string"
            return import_class + "\n\n" + class_name + methods + "\n" + relationship + "\n"
        else:
            assert type(class_name + methods + relationship) is str, "create_class method must return a string"
            return class_name + methods + relationship

    def generate_methods(self, class_data):
        for a_method in class_data.method:
            if "init" in a_method:
                self.create_constructor(a_method)
            else:
                plant_method = self.find_method_data_type(a_method)
                total_words = len(plant_method)
                my_method = self.find_method_details(total_words, plant_method)
                self.result += self.format_method(my_method)

    def find_method_data_type(self, plant_method):
        if "String" in plant_method:
            plant_method = plant_method.replace("String", "str")
        elif "Object" in plant_method:
            plant_method = plant_method.replace("Object", "T")
        return plant_method

    def format_method(self, my_method):
        if "self" not in my_method:
            pep8_method = "\n    @staticmethod\n    def {}:\n        pass\n".format(my_method)
        else:
            pep8_method = "\n    def {}:\n        pass\n".format(my_method)
        assert type(pep8_method) is str, "convert_method method must return a string"
        return pep8_method

    def find_method_details(self, total_words, plant_method):
        for i in range(total_words):
            if "(" in plant_method[i]:
                for j in range(i, total_words):
                    if ")" in plant_method[j]:
                        plant_method = list(plant_method)
                        plant_method[j + 1] = " ->"
                        my_method = "".join(plant_method).lstrip()
        return my_method

    def convert_constructor(self, plant_method: str, pep8_attributes: str) -> str:
        plant_method = self.find_method_data_type(plant_method)
        total_words = len(plant_method)
        my_method = self.find_method_details(total_words, plant_method)
        pep8_method = "\n    def {}:\n    {}".format(my_method, pep8_attributes)
        return pep8_method

    def generate_attributes(self, class_data):
        for a_attribute in class_data.attribute:
            if "String" in a_attribute:
                a_attribute = a_attribute.replace("String", "str")
            attribute_and_type = a_attribute.split(":")
            return_type = attribute_and_type[1].strip()
            attribute = attribute_and_type[0][0].lower() + attribute_and_type[0][1:].strip()
            an_attribute = "    self.{} = {}    \n".format(attribute, return_type)
            self.class_attributes.append(an_attribute)
