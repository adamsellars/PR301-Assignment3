class NewClass:

    def __init__(self, class_name: str) -> None:
        self.class_name = class_name
        print("class name")
        print(class_name)
        self.attribute = []
        self.method = []
        self.relationship = []

    def __str__(self) -> str:
        assert type(self.class_name) is str, "__str__ method must return a string"
        return self.class_name

    def add_method(self, method_name: str) -> None:
        self.method.append(method_name)
        print("method name")
        print(method_name)

    def add_attribute(self, attribute: str) -> None:
        self.attribute.append(attribute)
        print("attribute")
        print(attribute)

    def add_relationship(self, relationship: str) -> None:
        self.relationship.append(relationship)
        print("relationship")
        print(relationship)




