# Option 2- Set all at once, modify controller
# ALL CLASSES DONE


class Room(object):
    def __init__(self, north=None, south=None, east=None, west=None, name=None, description=None, up=None, down=None,
                 characters=None, items=None):
        if items is None:
            items = []
        self.description = description
        self.up = up
        self.down = down
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.name = name
        self.characters = characters
        self.items = items
        self.first_enter = True


class Item(object):
    def __init__(self, name=None, health=None, size=None, weight=0):
        self.name = name
        self.health = health
        self.size = size
        self.weight = weight


class Armor(Item):
    def __init__(self, name, classification, health):
        super(Armor, self).__init__(name, health)
        self.type = classification

    def get_hit(self, dmg):
        print("Your armor looses some health")
        self.health -= 1


class Helmet(Armor):
    def __init__(self, name, color, protection_ability, health=100):
        super(Helmet, self).__init__(name, "Helmet", health)
        self.ability = protection_ability
        self.color = color


class Aegon(Helmet):
    def __init__(self):
        super(Aegon, self).__init__("Aegon", "Blue", "Indestructible", 999999999999999999999999999999999999999999999)
        self.power = 100

    def get_hit(self, dmg):
        super(Aegon, self).get_hit(dmg)
        print("Your helmet cannot be damaged.")
        self.health += 1


class Gold(Helmet):
    def __init__(self):
        super(Gold, self).__init__("Gold", "Gold", "Normal", health=100)
        self.power = 50

    def get_hit(self, dmg):
        super(Gold, self).get_hit(dmg)
        print("Your helmet tries to fight back. IT IS A FUGILE ATTEMPT!")


class Leaf(Helmet):
    def __init__(self):
        super(Leaf, self).__init__("Leaf", "Green", "Weak", health=10)
        self.power = 1

    def get_hit(self, dmg):
        super(Leaf, self).get_hit(dmg)
        print("Your helmet doesn't even try. It is destroyed")


class Weapon(Item):
    def __init__(self, size, name, health, classification):
        super(Weapon, self).__init__()
        self.health = health
        self.size = size
        self.name = name
        self.classification = classification


class Spear(Weapon):
    def __init__(self, size, name, health, classification):
        super(Spear, self).__init__(size, name, health, classification)
        self.health = health
        self.size = size
        self.name = name
        self.classification = classification


class StoneTiconderoga(Spear):
    def __init__(self):
        super(StoneTiconderoga, self).__init__(18, "Stone Ticonderoga", 80, Spear)
        self.damage_output = 90


class HolyLance(Spear):
    def __init__(self):
        super(HolyLance, self).__init__(90, "HOLY LANCE", 9999999999999999999999, Spear)
        self.damage_output = 9999999999999999999999999


class Sword(Weapon):
    def __init__(self, name, agility, weight, size, damage_output, health=100):
        super(Sword, self).__init__(size, name, health, "Sword")
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
        super(Noodle, self).__init__("A Noodle", "Immobile", "0.001", 5, health=1, damage_output=10)
        self.weight = 10
        self.health = 1
        self.damage_output = 10


class SchoolMaterials(Item):
    def __init__(self, name, health):
        super(SchoolMaterials, self).__init__()
        self.name = name
        self.health = health


class ClassMaterials(SchoolMaterials):
    def __init__(self, name, classification):
        super(ClassMaterials, self).__init__(name, health=None)
        self.name = name
        self.classification = classification


class GoldenTiconderogaPencils(ClassMaterials):
    def __init__(self):
        super(GoldenTiconderogaPencils, self).__init__("Golden Ticonderoga Pencils! You've obtained Ticonderoga "
                                                       "Pencils", ClassMaterials)


class MSITitan(ClassMaterials):
    def __init__(self):
        super(MSITitan, self).__init__("MSI Titan! You've obtained the MSI Titan", ClassMaterials)


class GrizzlyBearProtection(ClassMaterials):
    def __init__(self):
        super(GrizzlyBearProtection, self).__init__("Grizzly Bear Protection! You've obtained the Grizzly Bear "
                                                    "Protection!", ClassMaterials)


class Food(SchoolMaterials):
    def __init__(self, name, taste, size, quality, health, restoration):
        super(Food, self).__init__(name, health)
        self.name = name
        self.taste = taste
        self.size = size
        self.quality = quality
        self.health_restoration = restoration


class CrappyLunch(Food):
    def __init__(self, name, restoration, size, edibility, health):
        super(CrappyLunch, self).__init__(name, "Deplorable", size, "Bad", restoration, health)
        self.name = name
        self.health_restoration = restoration
        self.size = size
        self.edibility = edibility


# Reheated Broccoli, Chili, Pizza, Raw Chicken
class Chili(CrappyLunch):
    def __init__(self, color, present_container, health_restoration, size, health):
        super(Chili, self).__init__("Chili", -20, size, "Unpalatable", health)
        self.color = color
        self.present_container = present_container
        self.health_restoration = health_restoration


class MeatLoversChili(Chili):
    def __init__(self):
        super(MeatLoversChili, self).__init__("Brown", "Styrofoam_Cup", -100, 80, -90)


class VegetarianChili(Chili):
    def __init__(self):
        super(VegetarianChili, self).__init__("Green", "Red_Cup", -70, 15, 9)


class Pizza(CrappyLunch):
    def __init__(self, restoration, size, edibility, color, health):
        super(Pizza, self).__init__("Pizza", restoration, size, edibility, health)
        self.color = color
        self.size = size
        self.health_restoration = restoration
        self.edibility = edibility
        self.health = health


class SaladPizza(Pizza):
    def __init__(self):
        super(SaladPizza, self).__init__(10, 15, "Tolerable", "Green", 50)


class CannedTunaPizza(Pizza):
    def __init__(self):
        super(CannedTunaPizza, self).__init__(1, 25, "Disgusting", "Brown", 80)


class DecentPizza(Pizza):
    def __init__(self):
        super(DecentPizza, self).__init__(20, 10, "Good", "Normal", 100)


class TeacherSustenance(Food):
    def __init__(self, name, taste, size, quality, restoration, health):
        super(TeacherSustenance, self).__init__(name, taste, size, quality, health, restoration)
        self.name = name
        self.taste = taste
        self.size = size
        self.quality = quality
        self.health_restoration = restoration


class Eggs(TeacherSustenance):
    def __init__(self, taste, size, quality, state, texture, name, health, restoration=100):
        super(Eggs, self).__init__("EGGS", taste, size, quality, restoration, health)
        self.taste = taste
        self.size = size
        self.quality = quality
        self.texture = texture
        self.state = state
        self.health_restoration = restoration
        self.name = name
        self.health = health


class BoiledEggs(Eggs):
    def __init__(self, health_restoration):
        super(BoiledEggs, self).__init__("GOOD", 10, "GOOD", "BOILED", "MUSHY", "Boiled Eggs", health_restoration, 80)


class ScrambledEggs(Eggs):
    def __init__(self, health_restoration):
        super(ScrambledEggs, self).__init__("GREAT", 12, "GOOD", "SCRAMBLED", "SOFT", "Scrambled Eggs",
                                            health_restoration, 90)


class VervainHummingbirdEggs(Eggs):
    def __init__(self):
        super(VervainHummingbirdEggs, self).__init__("GREAT", 0.3, "GREAT", "RAW", "LIQUID", "Vervain Hummingbird Eggs",
                                                     9999999999999)


class TreeOfLifeEggs(Eggs):
    def __init__(self):
        super(TreeOfLifeEggs, self).__init__("BAD", 10, "BAD", "RAW", 'LIQUID', "Tree of Life Eggs", 10, )


class BodyArmor(Armor):
    def __init__(self, name, protection_ability, size, damage_output, health=100):
        super(BodyArmor, self).__init__(name, "Body Armor", health)
        self.protection_ability = protection_ability
        self.size = size
        self.name = name
        self.damage_output = damage_output


class Cardstock(BodyArmor):
    def __init__(self, exertion):
        super(Cardstock, self).__init__("Cardstock", "WEAK", 15, 0, 20)
        self.power = 10
        self.exertion = exertion
        self.weight = 100

    def get_hit(self, dmg):
        super(Cardstock, self).get_hit(dmg)
        print("Your armor tries to fight back. IT IS A FUGILE ATTEMPT!")


class ModularTacticalVest(BodyArmor):
    def __init__(self, exertion, size):
        super(ModularTacticalVest, self).__init__('Modular Tactical Vest', "STRONG", size, 9999999, 10)
        self.exertion = exertion
        self.power = 99999999999

    def get_hit(self, dmg):
        super(ModularTacticalVest, self).get_hit(dmg)
        print("Your armor hits them back with the MIGHT OF ZEUS")


class Lasers(Weapon):

    def __init__(self, size, name, health, classification, joules, energy_output, damage_output):

        super(Lasers, self).__init__(size, name, health, classification)
        self.joules = joules
        self.energy = energy_output
        self.size = size
        self.name = name
        self.classification = classification
        self.damage_output = damage_output


class TwoPettawattLaser(Lasers):
    def __init__(self, damage_ouput):
        super(TwoPettawattLaser, self).__init__(78, "Two Pettawatt Laser", 99999, Lasers, 2000000000000, 2000000000000,
                                                2000000000)
        self.damage_output = damage_ouput


class LaserPointer(Lasers):
    def __init__(self, damage_output):
        super(LaserPointer, self).__init__(20, "Laser Pointer", 1, Lasers, 20, 10, 1)
        self.damage_output = damage_output


class Scripts(Weapon):
    def __init__(self, size, name, health, classification):
        super(Scripts, self).__init__(size, name, health, classification)
        self.size = size
        self.name = name
        self.health = health
        self.classification = classification


class HealthPotions(Item):
    def __init__(self, name, health_restoration):
        super(HealthPotions, self).__init__()
        self.name = name
        self.health_restoration = health_restoration


class Character(object):
    def __init__(self, name, health: int, weapon, armor, size):

        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.size = size

    def take_damage(self, damage: int):
        if self.armor.health >= damage:
            print("No damage is done because of some AMAZING armor")
        else:
            self.health -= damage - self.armor.health
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks for %s for %d damage" % (self.name, target.name, self.weapon.health))
        target.take_damage(self.weapon.health)


class Boss(Character):
    def __init__(self, name, health: int, weapon, armor, size, ):
        super(Boss, self).__init__(name, health, weapon, armor, size)
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.size = size

    def attack(self, target):
        print("%s attacks for %s for %d damage" % (self.name, target.name, self.weapon.health))
        target.take_damage(self.weapon.health)

    def take_damage(self, damage: int):
        if self.armor.health >= damage:
            print("No damage is done because of some AMAZING armor")
        else:
            self.health -= damage - self.armor.health
        print("%s has %d health left" % (self.name, self.health))


class Albert(Character):
    def __init__(self, name, health, weapon, armor, size):
        super(Albert, self).__init__(name, health, weapon, armor, size)
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.size = size

    def take_damage(self, damage: int):
        if self.armor.health >= damage:
            print("No damage is done because of some AMAZING armor")
        else:
            self.health -= damage - self.armor.health
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks for %s for %d damage" % (self.name, target.name, self.weapon.health))
        target.take_damage(self.weapon.health)


class ShakespereanCharacters(Character):
    def __init__(self, name, health, weapon, armor, size):
        super(ShakespereanCharacters, self).__init__(name, health, weapon, armor, size)
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.size = size

    def take_damage(self, damage: int):
        if self.armor.health >= damage:
            print("No damage is done because of some AMAZING armor")
        else:
            self.health -= damage - self.armor.health
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks for %s for %d damage" % (self.name, target.name, self.weapon.health))
        target.take_damage(self.weapon.health)


class Hobo(object):
    def __init__(self, personality, cleanliness, clothing, appearance, items, name):
        self.items = items
        self.name = name
        self.personality = personality
        self.cleanliness = cleanliness
        self.health = 100
        self.appearance = appearance
        self.clothing = clothing


# Blueprint for room
# Ex. R-19A =(North-Parking lot, South-etc.)
# Each room follows attributes set by object Room
# Ex. (North,South,East,West) = R-19A =(Parking Lot, ....)
# Presets-(like name=None)- must be applied to all attributes within the constructor


sword = Sword("Sword", "Quick", 15, 20, 10)
canoe = Sword("Canoe Sword", "SLOW", 90, 150, 42)
weibe_armor = BodyArmor("Armor of the gods", "GOOD", 18, 10000000000000000000000000000)
Traaaaaaaaaaaaash_Armor = BodyArmor("Traaaaaaaaaaash Armor", 99999999999999999, 20, 999999999999, 99999999)
Laser_pointer_1 = LaserPointer(5)
_007_Laser = TwoPettawattLaser(7000)
Laser_Pointer_3 = LaserPointer(10)
Laser_Pointer_4 = LaserPointer(10)
Cardstock_Armor = Cardstock(10)
Modular_Tactical_Vest_1 = ModularTacticalVest(80, 15)
Slow_Sword = Sword("Slow Sword", "SLOW", 10, 20, 5)
Vervain = VervainHummingbirdEggs()
Boiled = BoiledEggs(15)
Scrambled = ScrambledEggs(50)
Chestplate = BodyArmor("Chestplate", 15, 20, 10)
Aegon = Aegon()
Gold = Gold()
Golden_Ticonderoga_Pencils = GoldenTiconderogaPencils()
StoneTiconderoga = StoneTiconderoga()
Laser_Pointer_2 = LaserPointer(18)
Urumi = Urumi()
Seven_Branched_Sword_1 = SevenBranchedSword()
Vegetarian_Chili = VegetarianChili()
Meat_Lovers_Chili = MeatLoversChili()
Pencil1 = Pencil()
Pencil2 = Pencil()
Pencil3 = Pencil()
Pencil4 = Pencil()
Pencil5 = Pencil()
Pencil7 = Pencil()
Pencil8 = Pencil()
Pencil9 = Pencil()
Krishang = Hobo("NICE", "Krishang", "CLEAN", "PLAID_SHIRT", "Scruffy yet, well kept", "Slow_Sword")
Pencil10 = Pencil()
Tree_Of_Life = TreeOfLifeEggs()
Canned_Tuna_Pizza = CannedTunaPizza()
Salad_Pizza = SaladPizza()
Quadsword = Sword("Quad Sword", "QUICK", 15, 10, 15)
Decent_Pizza = DecentPizza()
MSI_Titan = MSITitan()
MSI_Titan2 = MSITitan()
MSI_Titan3 = MSITitan()
Grizzly_Bear_Protection = GrizzlyBearProtection()
Codesword = Sword("Code Sword", "QUICK", 20, 20, 100)
Codearmor = BodyArmor("Code Armor", 50, 20, 50)
Noodle = Noodle()
Pencil = Pencil()
Noodle2 = Noodle
Noodle3 = Noodle
Noodle4 = Noodle
Noodle5 = Noodle
Noodle7 = Noodle
Noodle8 = Noodle
Gold1 = Gold
Noodle9 = Noodle
Noodle10 = Noodle
Aegon1 = Aegon
StoneTiconderoga1 = StoneTiconderoga
Holy_Lance = HolyLance()
Leaf = Leaf()
# QuadHobo = Character("Quad Hobo", )
Albert2 = Albert("IT'S ALBERT""...."".... 2!", 900, Urumi, Modular_Tactical_Vest_1, 800)
Math_Sword = Sword("Math Sword", "QUICK", 20, 10, 80)
orc = Character("Orc1", 100, sword, BodyArmor("Generic Armor", "BAD", 15, 2, 10), 10)
orc2 = Character("Wiebe", 1000, canoe, weibe_armor, 10)
Armor_Of_The_Gods = BodyArmor("Armor of the Gods", 999999999, 18, 99999999, 99999999999)
orc.attack(orc2)
orc2.attack(orc)
Albert = Albert("IT'S ALBERT!", 50, Noodle10, Cardstock_Armor, 90)
TROLL1 = Character("Dave", 999999999999999999999, Urumi, Modular_Tactical_Vest_1, 20)
TROLL2 = Character("Bob", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL3 = Character("Jaxx", 80, Slow_Sword, weibe_armor, 20)
TROLL4 = Character("Yosroel", 50, Slow_Sword, Cardstock_Armor, 20)
TROLL5 = Character("Arnold", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL6 = Character("Peter", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL7 = Character("Justin", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL8 = Character("Oliver", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL9 = Character("DANNY DEVITO", 9999999, Urumi, Armor_Of_The_Gods, 20)
TROLL10 = Character("Mason", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL11 = Character("Alex", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL12 = Character("Henry", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL13 = Character("Wyatt", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL14 = Character("Owen", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL15 = Character("Sebastian", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL16 = Character("Levi", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL17 = Character("Joshua", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL18 = Character("Issac", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL19 = Character("Aaron", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL20 = Character("Thomas", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL21 = Character("Caleb", 10, Slow_Sword, Cardstock_Armor, 20)
TROLL22 = Character("DANNY DEVITO- REDUX", 999999999999999999999, Slow_Sword, Traaaaaaaaaaaaash_Armor, 20)
Noodle1 = Noodle
Hobo1 = Character("Hobo1", 10, Slow_Sword, Cardstock_Armor, 20)
Othello_Act1_Scene1 = Scripts(20, "Act 1; Scene 1", 20, Scripts)
Othello_Act1_Scene2 = Scripts(20, "Act 1; Scene 2", 20, Scripts)
Othello_Act4_Scene3 = Scripts(20, "Act 4; Scene 3", 20, Scripts)
Othello_Act3_Scene2 = Scripts(20, "Act 3; Scene 2", 20, Scripts)
Basic_Potion = HealthPotions("Basic Potion", 10)
Tier2_Potion = HealthPotions("Tier 2 potion", 20)
Tier3_Potion = HealthPotions("Tier 3 potion", 30)
Tier4_Potion = HealthPotions("Tier 4 potion", 50)
MEGA_Potion = HealthPotions("MEGA POTION", 100)
ShakespereanArmor = BodyArmor("Shakespearan Armor", 20, 20, 10)
Hamlet_Act1_Scene1 = Scripts(20, "Act1; Scene 1", 20, Scripts)
Hamlet_Act2_Scene2 = Scripts(20, "Act2; Scene 2", 20, Scripts)
Hamlet_Act3_Scene4 = Scripts(20, "Act3; Scene4", 20, Scripts)
Hamlet_Act5_Scene1 = Scripts(20, "Act 5; Scene1", 20, Scripts)
SecretRoomBoss = Boss("Secret Room Boss", 20, None, Gold, 20)
Leaf1 = Leaf
Urumi1 = Urumi
Null_Sword = Sword("Null Sword", "QUICK", 15, 20, 10)
Math_Armor = BodyArmor("Math Armor", 20, 15, 20)
Nightmare_sword = Sword("Nightmare Sword", "SLOW", 10, 20, 5)
Nightmare_Armor = BodyArmor("Nightmare Armor", 10, 10, 10)

orc = Character("Orc1", 100, sword, BodyArmor("Generic Armor", "BAD", 15, 2, 10), 20)
orc2 = Character("Wiebe", 1000, canoe, weibe_armor, 20)
orc.attack(orc2)
orc2.attack(orc)
MATHTROLL1 = Character("Math Troll 1", 10, Math_Sword, Math_Armor, 10)
MATHTROLL2 = Character("Math Troll 2", 20, Math_Sword, Math_Armor, 10)
NIGHTMARE_TROLL1 = Character("Spooky Dave", 20, Nightmare_sword, Nightmare_Armor, 10)

Iago = ShakespereanCharacters("Iago", 50, Othello_Act1_Scene1, ShakespereanArmor, 20)
Othello = ShakespereanCharacters("Othello", 50, Othello_Act1_Scene2, ShakespereanArmor, 20)
Desedemonda = ShakespereanCharacters("Desedemonda", 50, Othello_Act3_Scene2, ShakespereanArmor, 20)
Cassio = ShakespereanCharacters("Cassio", 50, Othello_Act4_Scene3, ShakespereanArmor, 20)
Hamlet = ShakespereanCharacters("Hamlet", 50, Hamlet_Act1_Scene1, ShakespereanArmor, 20)
Ghosts_of_Hamlets_father = ShakespereanCharacters("The Ghosts of Hamlets father", 50, Hamlet_Act2_Scene2,
                                                  ShakespereanArmor, 20)
Claudius = ShakespereanCharacters("Claudius", 50, Hamlet_Act3_Scene4, ShakespereanArmor, 20)
Horatio = ShakespereanCharacters("Horatio", 50, Hamlet_Act5_Scene1, ShakespereanArmor, 20)

TROLL20.attack(TROLL22)

Heisenwiebe = Boss("HEISENWIEBE", 250, Urumi, Modular_Tactical_Vest_1, 250)
Papa_Pearson = Boss("Papa Pearson", 200, Math_Sword, Chestplate, 250)
HOBO = Boss("Hobo.... It's a hobo. Not much more to say", 80, Slow_Sword, Cardstock, 80)
MathJesus = Boss("Math Jesus", 100, Math_Sword, Math_Armor, 100)


R19A = Room("PARKING_LOT", "QUAD", "DRAMA_BUILDING", "SCIENCE_BUILDING", "R19A",
            "This is the classroom you are in right now. There are two doors on the north wall. There are two doors on"
            " the north wall. There is a big mailbox in the sky for some reason", "MAILBOX", None, [TROLL2],
            [Cardstock(10), Noodle1, Tree_Of_Life, _007_Laser, Modular_Tactical_Vest_1])

print(Room(R19A.items))

PARKING_LOT = Room(None, "R19A", "HOBO_ATTACKS", "GYM_PORTAL", "Parking Lot", "There are a couple cars parked here. ",
                   None, "FLOOR", [TROLL1], None)

HOBO_ATTACKS = Room(None, "HOBO_WORLD", None, None, "Hobo Attacks you", "There is a homeless person here. He does not"
                    "like you. He hits you! You also can't seem to go back", "CEILING", "FLOOR", [Hobo1],
                    [Golden_Ticonderoga_Pencils])

GYM_PORTAL = Room(None, None, None, None, "Gym Portal", "This is the gym. It is dark and extremely musty. "
                  "I do not like it", "THE_REALM_OF_HEISENWEIBE", "THE_TRENCHES_OF_PAPA_PEARSON", [TROLL3, TROLL4],
                  [Modular_Tactical_Vest_1, Urumi])

SCIENCE_BUILDING = Room("POOL", "W_BUILDING", "HOBO_ATTACKS_YOU", "QUAD", "The Science Building", "This is the science "
                        "building. I suppose you know what they teach in this, given the name.", "CEILING", "FLOOR",
                        [Albert, TROLL4], [Slow_Sword, Cardstock_Armor, Noodle3])

QUAD = Room(None, None, "R_BUILDINGS", "W_BUILDINGS", "The Quad", "The main area. There is an ampitheatre here. There "
            "is also a couple of lamp posts.You can only go East and West, for some reason. ", "CEILING", "FLOOR",
            [TROLL7, TROLL13], [Quadsword, Leaf1])

W_BUILDING = Room("PARKING_LOT", "R_BUILDING", "QUAD", "PARKING_LOT", "W Building", "This is the W Building. It is a "
                  "two story masterpiece of a building. It,conveniently, is the building for languages.",
                  "THE SPANISH DILEMMA", "FLOOR", [TROLL13, TROLL2], [Leaf1, Urumi1])

SECRET_ROOM = Room(None, None, None, None, "Secret Room", "Welcome to the Secret Room- You will never find a place "
                   "with more valuable treasures!", "STREETS_OF_VERONA", None, [SecretRoomBoss], [Aegon, Holy_Lance])


MAILBOX = Room(None, None, None, None, "THE HOLY MAILBOX WELCOMES YOU!", "WELCOME TO SCHOOL WARRIOR, THE HIGHEST "
               "QUALITY GAME IN SCHOOL BASED" "CHOOSE YOUR OWN ADVENTURE GAMES! DEFEAT ONE BOSS AND COLLECT 20 ITEMS TO"
               "WIN THE GAME!", None, "R19A", [None], [None])

DRAMA_BUILDING = Room("NIGHTMARE_EDISON", "SHAKESPEARE_WORLD", "W_BUILDING", "PARKING_LOT", "The Drama Building", "This"
                      "is a long winding hallway. At the end there is a large telephone box. Paintings cover the wall",
                      "CEILING", None, [Krishang, TROLL18], [Decent_Pizza, Boiled])

R_BUILDINGS = Room("THE_ESSAY_TYPING", "GYM_PORTAL", "PARKING_LOT", "QUAD", "The R Buildings", "This is a row of "
                   "buildings. You can only go North, however. The other areas are blocked off.", "CEILING", None,
                   [TROLL7, TROLL22], [Pencil4, Scrambled])

HOBO_WORLD = Room("CHALLENGE_AREA", None, None, None, "Hobo World", "YoU haVe DECidEd tO Go SoUtH! Welcome to Hobo "
                  "World, the realm of the desolate and the weak. Here, you must complete one of  three challenges- "
                  "Garbage collecting, tent folding, and the hardest one of all, finding 4 pieces of food. After you "
                  "face these challenges, you win the game!", None, None, [TROLL1, TROLL7, TROLL18], [None])

POOL = Room("POOL", "POOL", "POOL", "POOL", "The Pool", "CONGRATULATIONS, YOU'VE MADE IT TO THE POOL!", "POOL", "POOL",
            [None], [None])

THE_REALM_OF_HEISENWEIBE = Room("THE_MAZE", "THE_MAZE", "THE_MAZE", "THE_MAZE", " The Realm of Heisenwiebe", "Welcome"
                                " to a world unlike any other- THE REALM OF HEISENWIEBE. This place is a maze. Once you"
                                "enter the realm, you can not get out. Reach the end of the realm,fight the Heisenwiebe"
                                " himself, then you win.", "THE MAZE", "THE MAZE", [TROLL5], [Null_Sword, Boiled])

THE_DARK_TRENCHES_OF_PAPA_PEARSON = Room("THE_LONG_WINDING_HALLWAY", "LABYRINTH", "LABYRINTH", "LABYRINTH", "The Dark "
                                         "Trenches of Papa Pearson", "Welcome. There really is not much to say about "
                                         "this place. There is a jar of Jolly Ranchers. and Popcorn in the corner. In "
                                         "front of you is a long winding hallway that goes only north. It is dark. "
                                         "Really dark. Also, any other direction you go seems to drop you in sometime "
                                         "of labyrinth ", "CEILING", "FLOOR", [MATHTROLL1, MATHTROLL2], [Math_Sword,
                                                                                                         Math_Armor])

NIGHTMARE_EDISON = Room("NIGHTMARE_W_BUILDING", "NIGHTMARE_R19A", "NIGHTMARE_PARKING_LOT", "NIGHTMARE_SCIENCE_BUILDING",
                        "NiGhTmArE EDiSon.", "WELCOME! This is Nightmare Edison. It is the same map as before only "
                        "SPOOKY! Get back to the normal world to win the game.", "NIGHTMARE_CEILING", None,
                        [TROLL7])

CEILING = Room("CEILING", "CEILING", "CEILING", "CEILING", "The Ceiling", "This is the ceiling. Do not go up, again!",
               "CEILING", None, [None], [Urumi1, Aegon1])


SHAKESPEARE_WORLD = Room("HAMLET", "OTHELLO", None, "ROMEO_AND_JULIET", "Shakespeare World", "You are "
                         "now in a medieval area. The buildings are that of 16th century.Everyone around you is wearing"                   
                         "some type of Victorian clothing. In this world, you must act on a play. Essentially, You are"
                         " dropped into the world of the play and must find the way out.", "CEILING",
                         "FLOOR", [], [])

THE_SPANISH_DILEMMA = Room("PROBLEMA_CUATRO", "PROBLEMA_UNO", "PROBLEMA_TRES", "UN PROBLEMA DIFICIL",
                           "THE_SPANISH_DILEMMA", "Este cuarto tiene una problema ese necesita resolver. Tu necesecitas"
                           " resolver la problema rapidamente. Si tu resuelves en tiempo, tu seras GANAR!", "CEILING",
                           "PROBLEMA_DOS")

FLOOR = Room("FLOOR", "FLOOR", "FLOOR", "FLOOR", "FLOOR", "This is the floor", "FLOOR", "FLOOR", [], [])

CHALLENGE_AREA = Room(None, "HOBO_WORLD", None, None, "The Challenge Area", "Welcome to the Challenge area."
                      "This is a very dark and musty cave. From what it seems,in the cave there are walls that block "
                      "off certain areas. There is also a huge homeless person here", "CEILING", "FLOOR", [HOBO], [])


NIGHTMARE_PARKING_LOT = Room("NIGHTMARE_CEILING", None, "NIGHTMARE_W_BUILDING", "NIGHTMARE_FLOOR", "Nightmare Parking "
                             "Lot", "Welcome to the Nightmare Version of the parking lot. All the cars are Hummers."
                             "Get spooked by their carbon emissions and their excessive gas prices!",
                             "NIGHTMARE_GYM_PORTAL", "NIGHTMARE_R19A", [NIGHTMARE_TROLL1], [])

NIGHTMARE_W_BUILDING = Room("NIGHTMARE_EDISON", "NIGHTMARE_CEILING", "NIGHTMARE_R_BUILDINGS", "NIGHTMARE_EDISON", "The "
                            "Nightmare W Buildings", "The building in a never ending staircase. It's almost like... a "
                            "maze. But it isn't. However, there are a lot of signs that just say- Look out for the "
                            "start.", "NIGHTMARE_CEILING", "NIGHTMARE_EDISON", [NIGHTMARE_TROLL1], [])

NIGHTMARE_R19A = Room("NIGHTMARE_GYM_PORTAL", "NIGHTMARE_HOBO_WORLD", "NIGHTMARE_DRAMA_BUILDING", "NIGHTMARE_QUAD",
                      "Nightmare R19A", "This is a SpOoOky computer room. All of the computers are Windows 98 and are "
                      "slower than paces of snails. ", "R19A", "NIGHTMARE_EDISON", [NIGHTMARE_TROLL1], [])

NIGHTMARE_SCIENCE_BUILDING = Room("NIGHTMARE_QUAD", "NIGHTMARE_HOBO_WORLD", "NIGHTMARE_EDISON", "NIGHTMARE_FLOOR", "The"
                                  "Nightmare Science Buildings", "The classes are terrifying! They're taught by "
                                  "flat-earthers and people who are against vaccines. What has this world come to?!",
                                  "NIGHTMARE_FLOOR", None, [Albert2])

NIGHTMARE_FLOOR = Room("R19A", "NIGHTMARE_EDISON", "NIGHTMARE_FLOOR", None, "Nightmare Floor", "It's dirty- Be spooked",
                       [], [MSI_Titan, MSI_Titan2, MSI_Titan3, Grizzly_Bear_Protection])

NIGHTMARE_QUAD = Room("NIGHTMARE_EDISON", "NIGHTMARE_FLOOR", "NIGHTMARE_CEILING", "NIGHTMARE_DRAMA_BUILDING",
                      "Nightmare Quad", "The ampitheatre is upside down and the music playing is... DOLLY PARTON?!?!",
                      "NIGHTMARE_GYM_PORTAL", "NIGHTMARE_PARKING_LOT", [TROLL13, TROLL22], [])

HAMLET = Room("DRAMA_BUILDING", None, None, None, "Hamlet", "Considered to be his best play, Hamlet is "
              "play in which Hamlet's father dies and it tells of his slow descent into madness. Here, you fight some "
              "important characters from this play, and collect a new series of weapon, THE SCRIPTS",
              "CEILING", "FLOOR", [Ghosts_of_Hamlets_father, Hamlet, Claudius, Horatio], [Othello_Act1_Scene2])


OTHELLO = Room("DRAMA_BUILDING", None, None, None, None, "Welcome to othello- The "
               "play, not the game. The play is about a Venetian soldier who passed over promotion by Othello and the "
               "story of how Othello undermines him, causing him to get revenge. Here, you fight some "
               "important characters from this play, and collect a new series of weapon, THE SCRIPTS",
               "CEILING", "FLOOR", [Hamlet, Ghosts_of_Hamlets_father, Claudius, Horatio], [Hamlet_Act1_Scene1])

THE_MAZE = Room("NULL_PATH", "IMPORT_GOD_PATH", "__INIT__PATH", "BAD_JOKE_PATH", "The Maze", "Welcome to the "
                "Heisenwiebe Maze. This maze has each path leading to a different aspect of the Heisenwiebe. Complete "
                "the path you go down to win. At the end of each path, you will fight the HEISENWIEBE himself",
                "SPAAAACE_PATH", "LUCKY_7S_PATH", [], [])

THE_LONG_WINDING_HALLWAY = Room("MATH_JESUS", "2019'S_CANCEL_OUT", "2019^2", "THE_INTEGRAL_OF_THE_SIN_OF_THE_COSINE_OF_"
                                "THE_DERIVATIVE_OF_INTEGRAL_OF_THE_LOG_OF_X_SQUARED_CUBED_SQUARED", "The Long Winding "
                                "Hallway", "It's... just... It'sj really difficult. Complete all 1 to win", "CEILING",
                                "FLOOR", [MATHTROLL1, MATHTROLL2], [Math_Sword])

NULL_PATH = Room("ERROR_ROOM", "HEISENWIEBE_ROOM", "NULL_PATH", "DEAD_END", "The Null Path", "Welcome to..."
                 "the Null Path! Don't expect anything of value.", "CEILING", "FLOOR", [], [])

ERROR_ROOM = Room("DEAD_END", "DEAD_END", "DEAD_END", "DEAD_END", "It's not working",
                  "Welcome to... ERROR 43942478-(DOES NOT COMPUTE ATTRIBUTE NAME- PRINTING- ^^%%*@##<<>@??<@##&. ",
                  "DEAD_END", "FLOOR", [], [Aegon1])

HEISENWIEBE_ROOM = Room(None, None, None, None, "Heisenwiebe's lair", "Welcome to the fiery depths of the Heisenwiebe"
                        "Here, the strongest, most powerful organism known to life resides- The HEISENWIEBE"
                        "He acknowledges your existance, but is mad at you, for being a mortal", None, None,
                        [Heisenwiebe], [])


IMPORT_GOD_PATH = Room("CODE_ITEMS_AREA", "HEISENWIEBE_ROOM", "NULL_PATH", "IMPORT_GOD_PATH", "Welcome to Import God",
                       "This isn't an evil path. Come, take some necessities so you can fight the Heisenwiebe, himself",
                       "CEILING", "FLOOR", [], [])

CODE_ITEMS_AREA = Room(None, "IMPORT_GOD_PATH", None, None, "The area with code items", "You'll need these", None, None,
                       [], [Codesword, Codearmor])

SPAAAACE_PATH = ("CEILING", "CEILING", "CEILING", "CEILING", "SPAAAAAAACE!", "Welcome.", "CEILING", "CEILING", [], [])


LUCKY_7S_PATH = ("R19A", "R19A", "R19A", "R19A", "Lucky 7's", "Your lucky to get on out of here!", "R19A", "R19A", [],
                 [])

MATH_JESUS = Room(None, None, None, None, "MATH JESUS", "Welcome to the most difficult of boss fights- THE MATH JESUS"
                  "Can you beat his lightning fast speed?", None, None, [MathJesus], [])

_2019S_CANCEL_OUT = Room("R19A", "R19A", "R19A", "R19A", "The 2019's Cancel", "Come on! You didn't get that? Go back to"
                         "the start", "R19A", "R19A", [], [])

THE_INTEGRAL_OF_THE_SINE_OF_THE_COSINE_OF_THE_DERIVATIVE_OF_INTEGRAL_OF_THE_LOG_OF_X_SQUARED_CUBED_SQUARED = Room(
    None, None, None, None, "THE_INTEGRAL_OF_THE_SINE_OF_THE_COSINE_OF_THE_DERIVATIVE_OF_INTEGRAL_OF_THE_LOG_OF_X_"
    "SQUARED_CUBED_SQUARED", "Got it? NOW GO!", None, None, [Papa_Pearson], [])

_2019_SQUARED = Room("FLOOR", "FLOOR", "FLOOR", "FLOOR", "The 2019's square", "This does not work in your favor",
                     "FLOOR", "FLOOR", [], [])


class Player(object):
    def __init__(self, starting_location, helmet=Aegon1, weapon=Urumi1, armor=Cardstock_Armor):
        self.current_location = starting_location
        inventory = []
        self.inventory = inventory
        self.weight_left = 100
        self.weight_max = 100
        self.size_capacity = 50
        self.size_max = 50
        self.health_starting = 100
        self.weapon = weapon
        self.name = "Player"
        self.armor = armor
        self.helmet = helmet

    def attack(self, target):
        print("You attack %s for %d damage" % (target.name, self.weapon.health))
        target.take_damage(self.weapon.health)

    def move(self, new_location):
        """ This moves the player to a new room
        :param new_location: The rooms object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """ This method searches the current room to see if a room exists in that direction
        :param direction: The direction that ypu want to move to
        :return: The room object if it exists, or none if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]

    def take_damage(self, damage: int):
        if self.armor.health >= damage:
            print("No damage is done because of some AMAZING armor")
        else:
            self.health_starting -= damage - self.armor.health
        print("%s has %d health left" % (self.name, self.health_starting))


player = Player(R19A)
print(player.inventory)

# Controller
playing = True
directions = ['north', 'south', "west", "east", "up", "down"]
short_directions = ['n', 's', 'w', 'e', 'u', 'd']
inventory_terms = ["Inventory", "I", "inventory", "i"]
health_and_eat_terms = ["EAT", "Eat", "eat", "CONSUME", "Consume", "consume"]
food_list = []
player.attack(Iago)
while playing:

    print(player.current_location.name)  # player- indicates the instantiated object. current_location- refers to the
    # variable. .name = refers to the attribute of the location
    print(player.current_location.description)

    for num, character in enumerate(player.current_location.characters):
        beat_characters = []

        print_character = (print(str(num + 1) + ": " + character.name))
        fight_command = input("Who do you want to fight?")

        if fight_command == "Bob":
            player.attack(TROLL2)
            TROLL2.health -= player.weapon.damage_output
            if TROLL2.health <= 0:
                print("%s has died" % TROLL2.name)
                TROLL2.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL2.name)
            else:
                print("%s has %d health left" % TROLL2.name, TROLL2.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL2.attack(player)

        elif fight_command == "Justin":
            player.attack(TROLL7)
            TROLL7.health -= player.weapon.damage_output
            if TROLL7.health <= 0:
                print("%s has died" % TROLL7.name)
                TROLL7.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL7.name)
            else:
                print("%s has %d health left" % TROLL7.name, TROLL7.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL7.attack(player)

        elif fight_command == "Jaxx":
            player.attack(TROLL3)
            TROLL3.health -= player.weapon.damage_output
            if TROLL3.health <= 0:
                print("%s has died" % TROLL3.name)
                TROLL3.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL3.name)
            else:
                print("%s has %d health left" % TROLL3.name, TROLL3.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL3.attack(player)

        elif fight_command == "Yosroel":
            player.attack(TROLL4)
            TROLL4.health -= player.weapon.damage_output
            if TROLL4.health <= 0:
                print("%s has died" % TROLL4.name)
                TROLL4.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL4.name)
            else:
                print("%s has %d health left" % TROLL4.name, TROLL4.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL4.attack(player)

        elif fight_command == "Arnold":
            player.attack(TROLL5)
            TROLL5.health -= player.weapon.damage_output
            if TROLL5.health <= 0:
                print("%s has died" % TROLL5.name)
                TROLL5.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL5.name)
            else:
                print("%s has %d health left" % TROLL5.name, TROLL5.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL5.attack(player)

        elif fight_command == "Peter":
            player.attack(TROLL6)
            TROLL6.health -= player.weapon.damage_output
            if TROLL6.health <= 0:
                print("%s has died" % TROLL6.name)
                TROLL6.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL6.name)
            else:
                print("%s has %d health left" % TROLL6.name, TROLL6.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL6.attack(player)

        elif fight_command == "Oliver":
            player.attack(TROLL8)
            TROLL8.health -= player.weapon.damage_output
            if TROLL8.health <= 0:
                print("%s has died" % TROLL8.name)
                TROLL8.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL8.name)
            else:
                print("%s has %d health left" % TROLL8.name, TROLL8.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL8.attack(player)

        elif fight_command == "DANNY DEVITO":
            player.attack(TROLL9)
            TROLL9.health -= player.weapon.damage_output
            if TROLL9.health <= 0:
                print("%s has died" % TROLL9.name)
                TROLL9.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL9.name)
            else:
                print("%s has %d health left" % TROLL9.name, TROLL9.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL9.attack(player)

        elif fight_command == "Dave":
            player.attack(TROLL1)
            TROLL1.health -= player.weapon.damage_output
            if TROLL1.health <= 0:
                print("%s has died" % TROLL1.name)
                TROLL1.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL1.name)
            else:
                print("%s has %d health left" % TROLL1.name, TROLL1.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL1.attack(player)

        elif fight_command == "Mason":
            player.attack(TROLL10)
            TROLL10.health -= player.weapon.damage_output
            if TROLL10.health <= 0:
                print("%s has died" % TROLL10.name)
                TROLL10.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL10.name)
            else:
                print("%s has %d health left" % TROLL10.name, TROLL10.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL10.attack(player)

        elif fight_command == "Alex":
            player.attack(TROLL11)
            TROLL11.health -= player.weapon.damage_output
            if TROLL11.health <= 0:
                print("%s has died" % TROLL11.name)
                TROLL11.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL11.name)
            else:
                print("%s has %d health left" % TROLL11.name, TROLL11.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL11.attack(player)

        elif fight_command == "Henry":
            player.attack(TROLL12)
            TROLL12.health -= player.weapon.damage_output
            if TROLL12.health <= 0:
                print("%s has died" % TROLL12.name)
                TROLL12.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL12.name)

            else:
                print("%s has %d health left" % TROLL12.name, TROLL12.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL12.attack(player)

        elif fight_command == "Wyatt":
            player.attack(TROLL13)
            TROLL13.health -= player.weapon.damage_output
            if TROLL13.health <= 0:
                print("%s has died" % TROLL13.name)
                TROLL13.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL13.name)
            else:
                print("%s has %d health left" % TROLL13.name, TROLL13.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL13.attack(player)

        elif fight_command == "Owen":
            player.attack(TROLL14)
            TROLL14.health -= player.weapon.damage_output
            if TROLL14.health <= 0:
                print("%s has died" % TROLL14.name)
                TROLL14.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL14.name)
            else:
                print("%s has %d health left" % TROLL14.name, TROLL14.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL14.attack(player)

        elif fight_command == "Sebastian":
            player.attack(TROLL15)
            TROLL15.health -= player.weapon.damage_output
            if TROLL15.health <= 0:
                print("%s has died" % TROLL15.name)
                TROLL15.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL15.name)
            else:
                print("%s has %d health left" % TROLL15.name, TROLL15.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL15.attack(player)

        elif fight_command == "Levi":
            player.attack(TROLL16)
            TROLL16.health -= player.weapon.damage_output
            if TROLL16.health <= 0:
                print("%s has died" % TROLL16.name)
                TROLL16.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL16.name)
            else:
                print("%s has %d health left" % TROLL16.name, TROLL16.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL16.attack(player)

        elif fight_command == "Joshua":
            player.attack(TROLL17)
            TROLL17.health -= player.weapon.damage_output
            if TROLL17.health <= 0:
                print("%s has died" % TROLL17.name)
                TROLL17.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL17.name)
            else:
                print("%s has %d health left" % TROLL17.name, TROLL17.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL17.attack(player)

        elif fight_command == "Issac":
            player.attack(TROLL18)
            TROLL18.health -= player.weapon.damage_output
            if TROLL18.health <= 0:
                print("%s has died" % TROLL18.name)
                TROLL18.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL18.name)
            else:
                print("%s has %d health left" % TROLL18.name, TROLL18.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL18.attack(player)

        elif fight_command == "Aaron":
            player.attack(TROLL19)
            TROLL19.health -= player.weapon.damage_output
            if TROLL19.health <= 0:
                print("%s has died" % TROLL19.name)
                TROLL19.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL19.name)
            else:
                print("%s has %d health left" % TROLL19.name, TROLL19.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL19.attack(player)

        elif fight_command == "Thomas":
            player.attack(TROLL20)
            TROLL20.health -= player.weapon.damage_output
            if TROLL20.health <= 0:
                print("%s has died" % TROLL20.name)
                TROLL20.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL20.name)
            else:
                print("%s has %d health left" % TROLL20.name, TROLL20.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL20.attack(player)

        elif fight_command == "Caleb":
            player.attack(TROLL21)
            TROLL21.health -= player.weapon.damage_output
            if TROLL21.health <= 0:
                print("%s has died" % TROLL21.name)
                TROLL21.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL21.name)
            else:
                print("%s has %d health left" % TROLL21.name, TROLL21.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL21.attack(player)

        elif fight_command == "DANNY DEVITO- REDUX":
            player.attack(TROLL22)
            TROLL22.health -= player.weapon.damage_output
            if TROLL22.health <= 0:
                print("%s has died" % TROLL22.name)
                TROLL22.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(TROLL22.name)
            else:
                print("%s has %d health left" % TROLL22.name, TROLL22.health)
        elif fight_command in ["None", "none", "no one"]:
            TROLL22.attack(player)

        elif fight_command == "Orc1":
            player.attack(orc)
            orc.health -= player.weapon.damage_output
            if orc.health <= 0:
                print("%s has died" % orc.name)
                orc.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(orc.name)
            else:
                print("%s has %d health left" % orc.name, orc.health)
        elif fight_command in ["None", "none", "no one"]:
            orc.attack(player)

        elif fight_command == "Wiebe":
            player.attack(orc2)
            orc2.health -= player.weapon.damage_output
            if orc2.health <= 0:
                print("%s has died" % orc2.name)
                orc2.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(orc2.name)
            else:
                print("%s has %d health left" % orc2.name, orc2.health)
        elif fight_command in ["None", "none", "no one"]:
            orc2.attack(player)

        elif fight_command == "Math Troll 1":
            player.attack(MATHTROLL1)
            MATHTROLL1.health -= player.weapon.damage_output
            if MATHTROLL1.health <= 0:
                print("%s has died" % MATHTROLL1.name)
                MATHTROLL1.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(MATHTROLL1.name)
            else:
                print("%s has %d health left" % MATHTROLL1.name, MATHTROLL1.health)
        elif fight_command in ["None", "none", "no one"]:
            MATHTROLL1.attack(player)

        elif fight_command == "Math Troll 2":
            player.attack(MATHTROLL2)
            MATHTROLL2.health -= player.weapon.damage_output
            if MATHTROLL2.health <= 0:
                print("%s has died" % MATHTROLL2.name)
                MATHTROLL2.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(MATHTROLL2.name)
            else:
                print("%s has %d health left" % MATHTROLL2.name, MATHTROLL2.health)
        elif fight_command in ["None", "none", "no one"]:
            MATHTROLL2.attack(player)

        elif fight_command == "Spooky Dave":
            player.attack(NIGHTMARE_TROLL1)
            NIGHTMARE_TROLL1.health -= player.weapon.damage_output
            if NIGHTMARE_TROLL1.health <= 0:
                print("%s has died" % NIGHTMARE_TROLL1.name)
                NIGHTMARE_TROLL1.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(NIGHTMARE_TROLL1.name)
            else:
                print("%s has %d health left" % NIGHTMARE_TROLL1.name, NIGHTMARE_TROLL1.health)
        elif fight_command in ["None", "none", "no one"]:
            NIGHTMARE_TROLL1.attack(player)

        elif fight_command == "Iago":
            player.attack(Iago)
            Iago.health -= player.weapon.damage_output
            if Iago.health <= 0:
                print("%s has died" % Iago.name)
                Iago.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(Iago.name)
            else:
                print("%s has %d health left" % Iago.name, Iago.health)
        elif fight_command in ["None", "none", "no one"]:
            Iago.attack(player)

        elif fight_command == "Othello":
            player.attack(Othello)
            Othello.health -= player.weapon.damage_output
            if Othello.health <= 0:
                print("%s has died" % Othello.name)
                Othello.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(Othello.name)
            else:
                print("%s has %d health left" % Othello.name, Othello.health)
        elif fight_command in ["None", "none", "no one"]:
            Othello.attack(player)

        elif fight_command == "Desedemonda":
            player.attack(Desedemonda)
            Desedemonda.health -= player.weapon.damage_output
            if Desedemonda.health <= 0:
                print("%s has died" % Desedemonda.name)
                Desedemonda.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(Desedemonda.name)
            else:
                print("%s has %d health left" % Desedemonda.name, Desedemonda.health)
        elif fight_command in ["None", "none", "no one"]:
            Desedemonda.attack(player)

        elif fight_command == "Cassio":
            player.attack(Cassio)
            Cassio.health -= player.weapon.damage_output
            if Cassio.health <= 0:
                print("%s has died" % Cassio.name)
                Cassio.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(Cassio.name)
            else:
                print("%s has %d health left" % Cassio.name, Cassio.health)
        elif fight_command in ["None", "none", "no one"]:
            Cassio.attack(player)

        elif fight_command == "Hamlet":
            player.attack(Hamlet)
            Hamlet.health -= player.weapon.damage_output
            if Hamlet.health <= 0:
                print("%s has died" % Hamlet.name)
                Hamlet.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(Hamlet.name)
            else:
                print("%s has %d health left" % Hamlet.name, Hamlet.health)
        elif fight_command in ["None", "none", "no one"]:
            Hamlet.attack(player)

        elif fight_command == "Ghosts of Hamlet's Father":
            player.attack(Ghosts_of_Hamlets_father)
            Ghosts_of_Hamlets_father.health -= player.weapon.damage_output
            if Ghosts_of_Hamlets_father.health <= 0:
                print("%s has died" % Ghosts_of_Hamlets_father.name)
                Ghosts_of_Hamlets_father.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(Ghosts_of_Hamlets_father.name)
            else:
                print("%s has %d health left" % Ghosts_of_Hamlets_father.name, Ghosts_of_Hamlets_father.health)
        elif fight_command in ["None", "none", "no one"]:
            Ghosts_of_Hamlets_father.attack(player)

        elif fight_command == "Claudius":
            player.attack(Claudius)
            Claudius.health -= player.weapon.damage_output
            if Claudius.health <= 0:
                print("%s has died" % Claudius.name)
                Claudius.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(Claudius.name)
            else:
                print("%s has %d health left" % Claudius.name, Claudius.health)
        elif fight_command in ["None", "none", "no one"]:
            Claudius.attack(player)

        elif fight_command == "Horatio":
            player.attack(Horatio)
            Horatio.health -= player.weapon.damage_output
            if Horatio.health <= 0:
                print("%s has died" % Horatio.name)
                Horatio.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(Horatio.name)
            else:
                print("%s has %d health left" % Horatio.name, Horatio.health)
        elif fight_command in ["None", "none", "no one"]:
            Horatio.attack(player)

        if len(inventory_terms) >= 20 and len(beat_characters) >= 30:
            print("You have won the GAME!")
            playing = False
        elif player.health_starting <= 0:
            print("You have died")
            playing = False

        while player.health_starting > 0 and fight_command in ["Heisenwiebe", "Papa Pearson", "Hobo",
                                                               "Secret Room Boss"]:
            if fight_command == "Heisenwiebe":
                player.attack(Heisenwiebe)
            elif Heisenwiebe.health > 0:
                Heisenwiebe.attack(player)
            elif Heisenwiebe.health == 0:
                print("You have defeated the Heisenwiebe himself.")
                Heisenwiebe.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(Heisenwiebe.name)

            elif fight_command == "Papa Pearson":
                player.attack(Papa_Pearson)
            elif Papa_Pearson.health > 0:
                Papa_Pearson.attack(player)
            elif Papa_Pearson.health == 0:
                print("Papa Pearson has left to buy more Jolly Ranchers. Consider him defeated.")
                Papa_Pearson.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(Papa_Pearson.name)

            elif fight_command == "Hobo":
                player.attack(HOBO)
            elif HOBO.health > 0:
                HOBO.attack(player)
            elif HOBO.health == 0:
                print("The Hobo... he has died!")
                HOBO.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(HOBO.name)

            elif fight_command == "Secret Room Boss":
                player.attack(SecretRoomBoss)
            elif SecretRoomBoss.health > 0:
                SecretRoomBoss.attack(player)
            elif SecretRoomBoss.health == 0:
                print("Well, you defeated him. Congrats... I guess")
                SecretRoomBoss.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(SecretRoomBoss.name)

            elif fight_command == "Math Jesus":
                player.attack(MathJesus)
            elif MathJesus.health > 0:
                MathJesus.attack(player)
            elif MathJesus.health == 0:
                print("Well, you defeated him. Congrats... I guess")
                MathJesus.alive = False
                player.current_location.characters.remove(character)
                beat_characters.append(MathJesus.name)

    if len(player.current_location.items) > 0 and player.current_location.first_enter:
        player.current_location.first_enter = False
        print("There are the following items in the room:")
        print()

        for num, item in enumerate(player.current_location.items):
            print(str(num + 1) + ": " + item.name)
        pick_up_command = input("What item would you like to pick up")

        selected_item = None
        for item in player.current_location.items:
            if pick_up_command in item.name:
                print("You have selected %s" % pick_up_command)
                selected_item = item

        if selected_item is not None:
            player.inventory.append(selected_item)
            player.weight_left -= selected_item.weight
            player.size_capacity -= selected_item.size
            player.current_location.items.remove(selected_item)

        elif pick_up_command.lower() == "none":
            print("Ok. You do not pick up an item!")
        else:
            print("I don't see one here")

    command = input(">_")
    if command in short_directions:
        index = short_directions.index(command)
        command = directions[index]
    if command.lower() in ["q", "quit", 'exit']:
        playing = False
        print("GAME OVER.")
    elif command.lower() in directions:

        try:
            next_room = player.find_next_room(command)
            player.move(next_room)

        except KeyError:
            print("I can't go that way!")
    else:
        print("Command not found")

    if command in inventory_terms:
        for item in player.inventory:
            print("Your inventory consists of %s" % item.name)

    if command == "Eat":
        for Food in player.inventory:
            print("Your inventory consists of %s" % Food.name)
            food_command = input("What do you want to eat")
            if food_command == "Tree of Life Eggs":
                player.health_starting += Tree_Of_Life.health_restoration
                print("You now have %d health" % player.health_starting)
            elif food_command == "Meat Lover's Chili":
                player.health_starting += Meat_Lovers_Chili.health_restoration
                print("You now have %d health" % player.health_starting)
            elif food_command == "Vegetarian Chili":
                player.health_starting += Vegetarian_Chili.health_restoration
                print("You now have %d health" % player.health_starting)
            elif food_command == "Vervain Hummingbird Eggs":
                player.health_starting += Vervain.health_restoration
                print("You now have %d health" % player.health_starting)
            elif food_command == "Scrambled Eggs":
                player.health_starting += Scrambled.health_restoration
                print("You now have %d health" % player.health_starting)
            elif food_command == "Boiled Eggs":
                player.health_starting += Boiled.health_restoration
                print("You now have %d health" % player.health_starting)
            elif food_command == "Tier 2 Health Potion":
                player.health_starting += Tier2_Potion.health_restoration
                print("You now have %d health" % player.health_starting)
            elif food_command == "Tier 3 Health Potion":
                player.health_starting += Tier3_Potion.health_restoration
                print("You now have %d health" % player.health_starting)
            elif food_command == "Tier 4 Health Potion":
                player.health_starting += Tier4_Potion.health_restoration
                print("You now have %d health" % player.health_starting)
            elif food_command not in Food:
                print("This is not Food")
                player.health_starting -= 10

    if command == "switch weapon":
        for item in player.inventory:
            print("Your inventory consists of %s" % item.name)
            switch_command = input("What weapon do you want to switch to")
            if switch_command == "A Noodle":
                player.weapon = Noodle1
                print("You now have %s as your weapon" % player.weapon.name)
            elif switch_command == "Urumi":
                player.weapon = Urumi1
                print("You now have %s as your weapon" % player.weapon.name)
            elif switch_command == "_007_Laser":
                player.weapon = _007_Laser
                print("You now have %s as your weapon" % player.weapon.name)
            elif switch_command == "Laser Pointer":
                player.weapon = Laser_pointer_1
                print("You now have %s as your weapon" % player.weapon.name)
            elif switch_command == "Stone Ticonderoga":
                player.weapon = StoneTiconderoga1
                print("You now have %s as your weapon" % player.weapon.name)
            elif switch_command == "Pencil":
                player.weapon = Pencil1
                print("You now have %s as your weapon" % player.weapon.name)
            elif switch_command not in Weapon:
                print("This is not a weapon")
                player.weapon = Slow_Sword

    if command == "put on armor":
        for item in player.inventory:
            print("Your inventory consists of %s" % item.name)
            armor_command = input("What armor do you want to put on")
            if armor_command == "Modular Tactical Vest":
                player.armor = Modular_Tactical_Vest_1
                print("You now have %s as your armor" % player.armor.name)
            elif armor_command == "Cardstock":
                player.armor = Cardstock_Armor
                print("You now have %s as your armor" % player.armor.name)
            elif armor_command == "Armor of the Gods":
                player.armor = weibe_armor
                print("You now have %s as your armor" % player.armor.name)
            elif armor_command not in Armor:
                print("This is not an armor")
                player.armor = Cardstock_Armor

    if command == "put on helmet":
        for item in player.inventory:
            print("Your inventory consists of %s" % item.name)
            armor_command = input("What helmet do you want to put on")
            if armor_command == "Aegon":
                player.helmet = Aegon1
                print("You now have %s as your helmet" % player.helmet.name)
            elif armor_command == "Gold":
                player.helmet = Gold1
                print("You now have %s as your helmet" % player.helmet.name)
            elif armor_command == "Leaf":
                player.helmet = Leaf1
                print("You now have %s as your helmet" % player.helmet.name)
            elif armor_command not in Helmet:
                print("This is not a Helmet")
                player.helmet = Leaf1

# Get rid of room items
