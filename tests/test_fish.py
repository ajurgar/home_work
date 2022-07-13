import unittest

from src.fish import Fish

class TestFish(unittest.TestCase):
    def setUp(self):
        self.fish = Fish("Dory")
    def test_fish_has_a_name(self):
        self.assertEqual("Dory",self.fish.name)