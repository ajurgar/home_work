import unittest
from src.river import River
from src.fish import Fish
from src.bears import Bear

class TestRiver(unittest.TestCase):
    
    def setUp(self):
        
        self.fish = Fish("Dory")
        self.fish1 = Fish("Nemo")
        self.fish2 = Fish("Toto")

        fishes = [self.fish, self.fish1, self.fish2]
        self.river = River("Amazon", fishes)
        self.bear = Bear("Yogi", "Grizzly")

    def tests_river_name(self):
        self.assertEqual("Amazon", self.river.name)

    def tests_fish_count(self):
        self.assertEqual(3, len(self.river.fish))

    def tests_remove_fish(self):
       self.river.remove_fish_from_river(self.fish)
    
    def tests_bear_eats_fish_from_river(self):
        self.bear.eat_fish(self.fish)
        self.river.remove_fish_from_river(self.fish)
        self.assertEqual(1, len(self.bear.stomach))
        self.assertEqual(2, len(self.river.fish))


