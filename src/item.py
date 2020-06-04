import random


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class AttackItem(Item):
    def __init__(self, name, description, attack_power, element):
        super().__init__(name, description)
        self.attack_power = attack_power
        self.element = element

    def attack(self, target):
        attack_power = self.attack_power * random.random(0, 2)
        defense = target.defense * random.random(0, 2)
        if attack_power > defense:
            print(f"You dealt {attack_power} damage and slaid the foe!")
        else:
            print(f"You dealt {attack_power} damage and failed to slay the target!")

class DefenseItem(Item):
    def __init__(self, name, description, defense, element):
        super().__init__(name, description)
        self.defense = defense
        self.element = element
