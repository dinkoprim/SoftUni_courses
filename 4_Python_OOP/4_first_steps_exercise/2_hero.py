class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, damage):
        defeated = f"{self.name} was defeated"
        self.health = max(0, self.health - damage)
        return defeated if self.health == 0 else None

    def heal(self, amount):
        self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
