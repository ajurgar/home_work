import unittest

from src.bears import Bear
from src.fish import Fish

class TestBear(unittest.TestCase):

    def setUp(self):
        self.bears = Bear("Yogi", "Grizzly")
        self.fish = Fish("Salmon")

    def test_bear_has_name(self):
        self.assertEqual("Yogi", self.bears.name)

    def test_bear_type(self):
        self.assertEqual("Grizzly", self.bears.type)

    def test_bear_eat_fish(self):
        self.bears.eat_fish("Salmon")
        self.assertEqual(["Salmon"], self.bears.stomach)
    
    def test_bear_food_count(self):
        self.bears.eat_fish("Salmon")
        self.assertEqual(1, self.bears.food_count())
    
    