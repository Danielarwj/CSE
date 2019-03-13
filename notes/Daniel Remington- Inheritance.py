class Item(object):
    def __init__(self, name=None, durability=None):
        self.name = name
        self.durability = durability


class Armor(Item):
    def __init__(self, name, classification, durability):
        super(Armor, self).__init__(name, durability)
        self.type = classification

    def get_hit(self, dmg):
        print("Your armor looses some durability")
        self.durability -= 1

    def power(self, exertion):
        print("Your helmet tries to shoot energy back to the enemy")


class Helmet(Armor):
    def __init__(self, name, color, protection_ability, durability=100):
        super(Helmet, self).__init__(name, "Helmet", durability)
        self.ability = protection_ability
        self.color = color


class Aegon(Helmet):
    def __init__(self):
        super(Aegon, self).__init__("Aegon", "Blue", "Indestructible", 999999999999999999999999999999999999999999999)
        self.power = 100

    def get_hit(self, dmg):
        super(Aegon, self).get_hit(dmg)
        print("Your helmet cannot be damaged.")
        self.durability += 1

    def power(self, exertion):
        super(Aegon, self).power(100)
        print("Your helmet sends back TEN THOUSANDS units of energy. Good Job")
        self.power += 1


class Gold(Helmet):
    def __init__(self):
        super(Gold, self).__init__("Gold", "Gold", "Normal", durability=100)
        self.power = 50

    def get_hit(self, dmg):
        super(Gold, self).get_hit(dmg)
        print("Your helmet tries to fight back. IT IS A FUGILE ATTEMPT!")

    def power(self, exertion):
        super(Gold, self).power(50)
        print("Your helmet is attempting... so close but no.")


class Leaf(Helmet):
    def __init__(self):
        super(Leaf, self).__init__("Leaf", "Green", "Weak", durability=10)
        self.power = 1

    def get_hit(self, dmg):
        super(Leaf, self).get_hit(dmg)
        print("Your helmet doesn't even try. It is destroyed")

    def power(self, exertion):
        super(Leaf, self).power(1)
        print("Don't even try.")


class Weapon(Item):
    def __init__(self, size, name, classification):
        super(Weapon, self).__init__()
        self.durability = 100
        self.size = size
        self.name = name
        self.classification = classification


class Sword(Weapon):
    def __init__(self, name, agility, weight, size, damage_output, health=100):
        super(Sword, self).__init__(size, name, "Sword")
        self.agility = agility
        self.weight = weight
        self.name = name
        self.health = health
        self.damage_output = damage_output


class SevenBranchedSword(Sword):
    def __init__(self):
        super(SevenBranchedSword, self).__init__("Seven Branched Sword", "Quick", 150, 25, health=100, damage_output=30)


class Urumi(Sword):
    def __init__(self):
        super(Urumi, self).__init__("The Urumi", "Quick", 400, 35, health=999999999999999999999, damage_output=99999999)


class Pencil(Sword):
    def __init__(self):
        super(Pencil, self).__init__("A Pencil", "Slow", 0.2, 12, health=2, damage_output=3)


class Noodle(Sword):
    def __init__(self):
        super(Noodle, self).__init__("A Noodle", "Immobile", "0.001", 5, health=1, damage_output=1)


class SchoolMaterials(Item):
    def __init__(self, name, durability, impact):
        super(SchoolMaterials, self).__init__()
        self.name = name
        self.durability = durability
        self.impact = impact


class Food(SchoolMaterials):
    def __init__(self, name, taste, size, quality, restoration):
        super(Food, self).__init__(name, durability=None, impact=None)
        self.taste = taste
        self.size = size
        self.quality = quality
        self.health_restoration = restoration


class CrappyLunch(Food):
    def __init__(self, name, restoration, size, edibility):
        super(CrappyLunch, self).__init__(name, "Deplorable", size, "Bad", restoration)
        self.name = name
        self.health_restoration = restoration
        self.size = size
        self.edibility = edibility


# Reheated Broccoli, Chili, Pizza, Raw Chicken
class Chili(CrappyLunch):
    def __init__(self, color, present_container, health_restoration, size):
        super(Chili, self).__init__("Chili", -20, size, "Unpalatable")
        self.color = color
        self.present_container = present_container
        self.health_restoration = health_restoration


class MeatLoversChili(Chili):
    def __init__(self):
        super(MeatLoversChili, self).__init__("Brown", "Styrofoam_Cup", -100, 80)


class VegetarianChili(Chili):
    def __init__(self):
        super(VegetarianChili, self).__init__("Green", "Red_Cup", -70, 15)


class Pizza(CrappyLunch):
    def __init__(self, restoration, size, edibility, color):
        super(Pizza, self).__init__("Pizza", restoration, size, edibility)
        self.color = color
        self.size = size
        self.health_restoration = restoration
        self.edibility = edibility


class SaladPizza(Pizza):
    def __init__(self):
        super(SaladPizza, self).__init__(10, 15, "Tolerable", "Green")


class CannedTunaPizza(Pizza):
    def __init__(self):
        super(CannedTunaPizza, self).__init__(1, 25, "Disgusting", "Brown")


class DecentPizza(Pizza):
    def __init__(self):
        super(DecentPizza, self).__init__(20, 10, "Good", "Normal")


class TeacherSustenance(Food):
    def __init__(self, name, taste, size, quality, restoration):
        super(TeacherSustenance, self).__init__(name, taste, size, quality, restoration)
        self.name = name
        self.taste = taste
        self.size = size
        self.quality = quality
        self.health_restoration = restoration


class Eggs(TeacherSustenance):
    def __init__(self, taste, size, quality, state, texture, name, restoration=100):
        super(Eggs, self).__init__("EGGS", taste, size, quality, restoration)
        self.taste = taste
        self.size = size
        self.quality = quality
        self.texture = texture
        self.state = state
        self.health_restoration = restoration
        self.name = name


class BoiledEggs(Eggs):
    def __init__(self):
        super(BoiledEggs, self).__init__("GOOD", 10, "GOOD", "BOILED", "MUSHY", "Boiled Eggs")


class ScrambledEggs(Eggs):
    def __init__(self):
        super(ScrambledEggs, self).__init__("GREAT", 12, "GOOD", "SCRAMBLED", "SOFT", "Scrambled Eggs")


class VervainHummingbirdEggs(Eggs):
    def __init__(self):
        super(VervainHummingbirdEggs, self).__init__("GREAT", 0.3, "GREAT", "RAW", "LIQUID", "Vervain Hummingbird Eggs",
                                                     9999999999999)


class Pastries(TeacherSustenance):
    def __init__(self):
        super(Pastries, self).__init__()


class BodyArmor(Armor):
    def __init__(self, name, protection_ability, size, damage_output ,durability=100):
        super(BodyArmor, self).__init__(name, "Body Armor", durability)
        self.protection_ability = protection_ability
        self.size = size
        self.name = name
        self.damage_output = damage_output


class Cardstock(BodyArmor):
    def __init__(self, exertion):
        super(Cardstock, self).__init__("Cardstock", "WEAK", 15, 0, 20)
        self.power = 10
        self.exertion = exertion

    def get_hit(self, dmg):
            super(Cardstock, self).get_hit(dmg)
            print("Your armor tries to fight back. IT IS A FUGILE ATTEMPT!")

    def power(self, exertion):
            super(Cardstock, self).power(10)
            self.exertion = 10
            print("It can't exert power back at them! It is destroyed")


class ModularTacticalVest(BodyArmor):
    def __init__(self, exertion, size):
        super(ModularTacticalVest, self).__init__('Modular Tactical Vest', "STRONG", size, 9999999, 10)
        self.exertion = exertion
        self.power = 99999999999

    def get_hit(self, dmg):
            super(ModularTacticalVest, self).get_hit(dmg)
            print("Your armor hits them back with the MIGHT OF ZEUS")

    def power(self, exertion):
            super(ModularTacticalVest, self).power(99999999999)
            self.exertion = 999999999
            print("YOU ARE INVINCIBLE! They are destroyed")


class Lasers(Weapon):

    def __init__(self, size, name, classification, joules, energy_output, damage_output):

        super(Lasers, self).__init__(size, name, classification)
        self.joules = joules
        self.energy = energy_output
        self.size = size
        self.name = name
        self.classification = classification
        self.damage_output = damage_output


class TwoPettawattLaser(Lasers):
    def __init__(self, damage_ouput):
        super(TwoPettawattLaser, self).__init__(78, "Two Pettawatt Laser", Lasers, 2000000000000, 2000000000000)
        self.damage_output = damage_ouput


class Character(object):
    def __init__(self, name, health: int, weapon, armor):

        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage: int):
        if self.armor.durability >= damage:
            print("No damage is done because of some AMAZING armor")
        else:
            self.health -= damage - self.armor.durability
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks for %s for %d damage" % (self.name, target.name, self.weapon.durability))
        target.take_damage(self.weapon.durability)

sword = Sword("Sword","Quick", 15, 20, 10)
canoe = Sword("Canoe Sword", "SLOW", 90, 150, 42)
weibe_armor = BodyArmor("Armor of the gods", "GOOD", 18, 10000000000000000000000000000)


orc = Character("Orc1", 100, sword, BodyArmor("Generic Armor", "BAD", 15, 2, 10))
orc2 = Character("Weibe", 1000, canoe, weibe_armor)
orc.attack(orc2)
orc2.attack(orc)