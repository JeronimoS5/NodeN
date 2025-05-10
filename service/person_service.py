from datetime import date
from model.person import Person
from model.node_n import NodeN
from model.tree_n import TreeN

class PersonService:
    tree = TreeN()

    @classmethod
    def create(cls, person: Person) -> Person:
        cls.tree.add(person)
        return person

    @classmethod
    def get_all(cls) -> list[Person]:
        return cls.tree.get_all()

    @classmethod
    def get_by_id(cls, person_id: str) -> Person | None:
        node = cls.tree.find(person_id)
        return node.person if node else None

    @classmethod
    def update(cls, person_id: str, updated: Person) -> Person | None:
        return cls.tree.update(person_id, updated)

    @classmethod
    def delete(cls, person_id: str) -> bool:
        return cls.tree.delete(person_id)

    @classmethod
    def get_people_with_adult_daughter(cls) -> list[Person]:
        result = []

        def has_adult_daughter(node: NodeN) -> bool:
            for child in node.children:
                age = cls.calculate_age(child.person.birthdate)
                if child.person.gender == "F" and age >= 18:
                    return True
            return False

        def traverse(node: NodeN):
            if has_adult_daughter(node):
                result.append(node.person)
            for child in node.children:
                traverse(child)

        if cls.tree.root:
            traverse(cls.tree.root)

        return result

    @staticmethod
    def calculate_age(birthdate: date) -> int:
        today = date.today()
        return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    @classmethod
    def filter_by_location_typedoc_gender(cls, location_code: str, type_doc: str, gender: str) -> list[Person]:
        return [p for p in cls.tree.get_all() if
                p.location_code == location_code and p.type_doc == type_doc and p.gender == gender]

    @classmethod
    def get_by_location(cls, location_code: str) -> list[Person]:
        return [p for p in cls.tree.get_all() if p.location_code == location_code]
