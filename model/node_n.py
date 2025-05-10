from model.person import Person

class NodeN:
    def __init__(self, person: Person):
        self.person = person
        self.children: list[NodeN] = []
