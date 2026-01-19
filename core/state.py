class RelationshipState:
    def __init__(self):
        self.generation = 0
        self.lineage = None
        self.gender = None
        self.age = None
        self.affinity = "blood"
        self.path = []

    def update(self, token):
        self.path.append(token["type"])

        if token["type"] == "parent":
            self.generation += 1
            self.lineage = self.lineage or token.get("lineage")

        elif token["type"] == "child":
            self.generation -= 1

        elif token["type"] == "spouse":
            self.affinity = "affinal"

        self.gender = token.get("gender", self.gender)
        self.age = token.get("age", self.age)
