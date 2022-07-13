class River:
    def __init__(self, name, fishes):
        self.name = name
        self.fish = fishes

    def name_of_river(self):
        self.river.name

    def fish_count(self):
        return len(self.fish())

    def remove_fish_from_river(self,fish):
        self.fish.remove(fish)
    
    def eats_fish_from_river(self, bears, fish):
        self.bear.eat_fish(fish)
        self.remove_fish_from_river(fish)