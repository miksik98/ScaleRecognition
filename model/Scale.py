class Scale:
    def __init__(self, name, steps):
        self.steps = steps
        self.name = name

    def __str__(self):
        return f"{self.name}: {self.steps}"
