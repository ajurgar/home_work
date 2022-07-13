class Bear:
    def __init__(self, name, type):
        self.name = name 
        self.type = type
        self.stomach = []

    def eat_fish(self, fish):
        self.stomach.append(fish)

    def food_count(self):
        return len(self.stomach)
