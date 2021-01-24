import random

class Warrior:
    def __init__(self, name, hp, level):
        self.name = name
        self.level = level
        self.hp = hp

    def attack(self):
        return random.randint(0,15)

    def block(self):
        return random.randint(0,5)
