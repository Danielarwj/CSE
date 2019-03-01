class Item(object):
    def __init__(self, name, durability):
        self.name = name
        self.durability = durability

class Armor(Item):
    def __init__(self, protection_ability, type, health):
        super(Armor, self).__init__(name=None, durability=None)
        self.protection_ability = protection_ability
        self.type = type
        self.health = health











