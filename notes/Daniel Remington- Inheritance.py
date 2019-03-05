class Item(object):
    def __init__(self, name=None, durability=None):
        self.name = name
        self.durability = durability


class Armor(Item):
    def __init__(self, type, durability):
        super(Armor, self).__init__()
        self.type = type
        self.health = durability


class Helmet(Armor):
    def __init__(self, color, protection_ability):
        super(Helmet, self).__init__(type=Helmet, durability=100)
        self.ability = protection_ability
        self.color = color
        self.health = durability


class Aegon(Helmet):
    def __init__(self):
        super(Aegon, self).__init__("Blue", "Indestructible")
        self.durability = "VERY_GOOD"

class Gold(Helmet):
    def __init__(self):
        super(Gold, self).__init__("Gold", "")

