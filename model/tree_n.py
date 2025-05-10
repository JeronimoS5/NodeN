from model.node_n import NodeN
from model.person import Person

class TreeN:
    def __init__(self):
        self.root: NodeN | None = None

    def add(self, person: Person):
        node = NodeN(person)
        if person.parent_id is None:
            if self.root is None:
                self.root = node
        else:
            parent = self.find(person.parent_id)
            if parent:
                parent.children.append(node)

    def find(self, person_id: str) -> NodeN | None:
        def search(node: NodeN) -> NodeN | None:
            if node.person.id == person_id:
                return node
            for child in node.children:
                result = search(child)
                if result:
                    return result
            return None
        return search(self.root) if self.root else None

    def get_all(self) -> list[Person]:
        result = []

        def traverse(node: NodeN):
            result.append(node.person)
            for child in node.children:
                traverse(child)

        if self.root:
            traverse(self.root)
        return result

    def update(self, person_id: str, updated: Person) -> Person | None:
        node = self.find(person_id)
        if node:
            node.person = updated
            return updated
        return None

    def delete(self, person_id: str) -> bool:
        if self.root and self.root.person.id == person_id:
            self.root = None
            return True

        def remove(node: NodeN):
            for child in node.children:
                if child.person.id == person_id:
                    node.children.remove(child)
                    return True
                if remove(child):
                    return True
            return False

        return remove(self.root) if self.root else False
