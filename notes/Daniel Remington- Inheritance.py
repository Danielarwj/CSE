class Item(object):
    def __init__(self, name=None, durability=None):
        self.name = name
        self.durability = durability


class Armor(Item):
    def __init__(self, type, durability):
        super(Armor, self).__init__()
        self.type = type
        self.health = durability

    def get_hit(self, dmg):
        print("Your armor looses some durability")
        self.durability -= 1

    def power(self, exertion):
        print("Your helmet tries to shoot energy back to the enemy")


class Helmet(Armor):
    def __init__(self, color, protection_ability, durability=100):
        super(Helmet, self).__init__("Helmet", durability)
        self.ability = protection_ability
        self.color = color


class Aegon(Helmet):
    def __init__(self):
        super(Aegon, self).__init__("Blue", "Indestructible", 999999999999999999999999999999999999999999999)
        self.power = 100

    def get_hit(self, dmg):
        super(Aegon, self).get_hit(dmg)
        print("Your helmet cannot be damaged.")
        self.durability += 1

    def power(self, exertion):
        super(Aegon, self).power(100)
        print("Your helmet sends back TEN THOUSANDS units of energy. Good Job")
        self.power +=1

class Gold(Helmet):
    def __init__(self):
        super(Gold, self).__init__("Gold", "Normal", durability=100)
        self.power = 50

    def get_hit(self, dmg):
        super(Gold, self).get_hit(dmg)
        print("Your helmet tries to fight back. IT IS A FUGILE ATTEMPT!")

    def power(self, exertion):
        super(Gold, self).power(50)
        print("Your helmet is attempting... so close but no.")


class Leaf(Helmet):
    def __init__(self):
        super(Leaf, self).__init__("Green", "Weak", durability=10)
        self.power = 1

    def get_hit(self, dmg):
        super(Leaf, self).get_hit(dmg)
        print("Your helmet doesn't even try. It is destroyed")

    def power(self, exertion):
        super(Leaf, self).power(1)
        print("Don't even try.")

class BodyArmor(Armor):
        def __init__(self, protection_ability, durability=100,):
            super(BodyArmor, self).__init__("Body Armor", durability)
            self.protection_abilty = protection_ability


class Weapon(Item):
    def __init__(self, size):
        super(Weapon, self).__init__()
        self.durability = 100
        self.size = size

class Sword(Weapon):
    def __init__(self, agility, weight):
        super(Sword, self).__init__(size=None)
        self.agility = agility
        self.weight = weight
