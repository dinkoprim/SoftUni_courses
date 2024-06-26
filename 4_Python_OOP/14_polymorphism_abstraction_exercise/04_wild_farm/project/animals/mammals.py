from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def appropriate_feed(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self):
        return 0.10


class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def appropriate_feed(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.40


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def appropriate_feed(self):
        return [Vegetable, Meat]

    @property
    def gained_weight(self):
        return 0.30


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def appropriate_feed(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1.00

