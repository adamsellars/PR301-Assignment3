import unittest
import coverage
cov = coverage.Coverage()
cov.start()


class PEP8ConverterTests(unittest.TestCase):

    def test_pep8_convert_class(self):
        plant_class_name = "ManEater"
        expected = "class ManEater:\n"
        failure_msg = "\nThe actual input: \n{0}\nshould actually be\n{1}."

        actual = PEP8Converter.convert_class(plant_class_name)

        self.assertEqual(actual, expected, failure_msg.format(actual, expected))

    # Test convert_class
    def test_covert_class(self):
        # Arrange
        name = "controller"
        # Act
        actual = PEP8Converter.convert_class(name)
        # Assert
        self.assertEqual(actual, "class controller:\n")

    # Test convert_attribute
    def test_convert_attribute(self):
        # Arrange
        test = PEP8Converter()
        # Act
        result = test.convert_attribute("attribute : String")
        # Assert
        self.assertEqual(result, "    self.attribute = str    \n    ")

    # Test convert_method
    def test_convert_method(self):
        # Arrange
        test = PEP8Converter()
        # Act
        result = test.convert_method("get_all_my_classes(self) : list")
        # Assert
        self.assertEqual(result, "\n    def get_all_my_classes(self) ->: list:\n        pass\n")

    def test_convert_method_string(self):
        # Arrange
        test = PEP8Converter()
        # Act
        result = test.convert_method("get_all_my_classes(self) : String")
        # Assert
        self.assertEqual(result, "\n    def get_all_my_classes(self) ->: str:\n        pass\n")

    def test_convert_method_object(self):
        # Arrange
        test = PEP8Converter()
        # Act
        result = test.convert_method("get_all_my_classes(self) : Object")
        # Assert
        self.assertEqual(result, "\n    def get_all_my_classes(self) ->: T:\n        pass\n")

    def test_convert_constructor_string(self):
        # Arrange
        test = PEP8Converter()
        expected = "\n    def __init__() -> str:\n    data : str"
        # Act
        result = test.convert_constructor("__init__(): String", "data : str")
        # Assert
        self.assertEqual(result, expected)

    def test_convert_constructor_object(self):
        # Arrange
        test = PEP8Converter()
        expected = "\n    def __init__() -> T:\n    data : str"
        # Act
        result = test.convert_constructor("__init__(): Object", "data : str")
        # Assert
        self.assertEqual(result, expected)

    # Test create_relationship
    def test_create_relationship(self):
        # Arrange
        test = PEP8Converter()
        # Act
        result = test.create_relationship("controller o-- ClassFinder", 0)
        # Assert
        self.assertEqual(result, "\nobject0 = o--()")

    # Test create_relationship
    def test_create_relationship_no_relationship(self):
        # Arrange
        test = PEP8Converter()
        # Act
        result = test.create_relationship("controller", 0)
        # Assert
        self.assertEqual(result, "")

    def test_set_import(self):
        # Arrange
        test = PEP8Converter()
        # Act
        result = test.set_import("-- ClassFinder")
        # Assert
        self.assertEqual(result, "from .classfinder import ClassFinder\n")

    def test_set_import_no_import(self):
        # Arrange
        test = PEP8Converter()
        # Act
        result = test.set_import("")
        # Assert
        self.assertEqual(result, "")

    def test_create_class(self):
        # Arrange
        test = PEP8Converter()
        plant_class_name = NewClass("Pickler")
        plant_class_name.add_method("__init__(): None")
        plant_class_name.add_method("unpickle_file(): None")
        plant_class_name.add_attribute("connection : None")
        plant_class_name.add_relationship("-- ClassFinder")
        expected = "from .classfinder import ClassFinder\n\n\n"\
            "class Pickler:\n\n"\
            "    def __init__() -> None:\n"\
            "        self.connection = None    \n    \n"\
            "    @staticmethod\n"\
            "    def unpickle_file() -> None:\n"\
            "        pass\n\n\n"\
            "object1 = ClassFinder()\n"
        # Act
        result = test.create_class(plant_class_name)
        print("----------------------")
        print(result)
        print("----------------------")
        print("=======================")
        print(expected)
        print("=======================")
        # Assert
        self.assertEqual(result, expected)

    def test_create_class_no_relationship(self):
        # Arrange
        test = PEP8Converter()
        plant_class_name = NewClass("Pickler")
        plant_class_name.add_method("__init__(): None")
        plant_class_name.add_method("unpickle_file(): None")
        plant_class_name.add_attribute("connection : None")
        # plant_class_name.add_relationship("-- ClassFinder")
        expected = "class Pickler:\n\n"\
            "    def __init__() -> None:\n"\
            "        self.connection = None    \n    \n"\
            "    @staticmethod\n"\
            "    def unpickle_file() -> None:\n"\
            "        pass\n"\

        # Act
        result = test.create_class(plant_class_name)
        print("----------------------")
        print(result)
        print("----------------------")
        print("=======================")
        print(expected)
        print("=======================")
        # Assert
        self.assertEqual(result, expected)

    def test_create_relationship_valid(self):
        # Arrange
        test = PEP8Converter()
        # Act
        result = test.create_relationship("controller -- ClassFinder", 0)
        # Assert
        self.assertEqual(result, "\nobject0 = --()")
        cov.stop()
        cov.save()
        cov.html_report()


if __name__ == "__main__":
    from model.pep8_converter import PEP8Converter
    from model.class_maker import NewClass
    unittest.main(verbosity=2)  # with more details
