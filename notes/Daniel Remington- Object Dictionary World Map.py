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


class Item(object):
    def __init__(self, name=None, health=None):
        self.name = name
        self.health = health


class Player(object):
    def __init__(self, starting_location, inventory):
        inventory = []
        self.current_location = starting_location
        self.inventory = inventory

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


class Armor(Item):
    def __init__(self, name, classification, health):
        super(Armor, self).__init__(name, health)
        self.type = classification

    def get_hit(self, dmg):
        print("Your armor looses some health")
        self.health -= 1

    def power(self, exertion):
        print("Your helmet tries to shoot energy back to the enemy")


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

    def power(self, exertion):
        super(Aegon, self).power(100)
        print("Your helmet sends back TEN THOUSANDS units of energy. Good Job")
        self.power += 1


class Gold(Helmet):
    def __init__(self):
        super(Gold, self).__init__("Gold", "Gold", "Normal", health=100)
        self.power = 50

    def get_hit(self, dmg):
        super(Gold, self).get_hit(dmg)
        print("Your helmet tries to fight back. IT IS A FUGILE ATTEMPT!")

    def power(self, exertion):
        super(Gold, self).power(50)
        print("Your helmet is attempting... so close but no.")


class Leaf(Helmet):
    def __init__(self):
        super(Leaf, self).__init__("Leaf", "Green", "Weak", health=10)
        self.power = 1

    def get_hit(self, dmg):
        super(Leaf, self).get_hit(dmg)
        print("Your helmet doesn't even try. It is destroyed")

    def power(self, exertion):
        super(Leaf, self).power(1)
        print("Don't even try.")


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
        super(Noodle, self).__init__("A Noodle", "Immobile", "0.001", 5, health=1, damage_output=1)


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
    def __init__(self, restoration):
        super(BoiledEggs, self).__init__("GOOD", 10, "GOOD", "BOILED", "MUSHY", "Boiled Eggs", restoration, 80)


class ScrambledEggs(Eggs):
    def __init__(self, restoration):
        super(ScrambledEggs, self).__init__("GREAT", 12, "GOOD", "SCRAMBLED", "SOFT", "Scrambled Eggs", restoration, 90)


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


class Shopkeepers(Character):
    def __init__(self, name, health, size):
        super(Shopkeepers, self).__init__(name, health, None, None, size)
        self.name = name
        self.health = health
        self.size = size
        self.inventory = []


class Boss(Character):
    def __init__(self, name, health: int, weapon, armor, size, boss_power):
        super(Boss, self).__init__(name, health, weapon, armor, size)
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.size = size
        self.BOSS_POWER = boss_power

    def attack(self, target):
        print("%s attacks for %s for %d damage" % (self.name, target.name, self.weapon.health))
        target.take_damage(self.weapon.health)

    def take_damage(self, damage: int):
        if self.BOSS_POWER >= damage:
            print("Because %s is a BOSS, he takes no damage")
        else:
            self.health -= damage - self.armor.health
            print("%s has %d health left! %s is losing his BOSSINESS")


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


class Hobo(object):
    def __init__(self, personality, cleanliness, clothing, appearance, items):
            self.items = items
            self.personality = personality
            self.cleanliness = cleanliness
            self.health = 100
            self.appearance = appearance
            self.clothing = clothing


Krishang = Hobo("NICE", "CLEAN", "PLAID_SHIRT", "Scruffy yet, well kept", ["Sword", "Health_potion", "Roman_Candle"])

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
Pencil10 = Pencil()
Tree_Of_Life = TreeOfLifeEggs()
Canned_Tuna_Pizza = CannedTunaPizza()
Salad_Pizza = SaladPizza()
Decent_Pizza = DecentPizza()
MSI_Titan = MSITitan()
MSI_Titan2 = MSITitan()
MSI_Titan3 = MSITitan()
Grizzly_Bear_Protection = GrizzlyBearProtection()
Noodle = Noodle()
Pencil = Pencil()
Noodle2 = Noodle
Noodle3 = Noodle
Noodle4 = Noodle
Noodle5 = Noodle
Noodle7 = Noodle
Noodle8 = Noodle
Noodle9 = Noodle
Noodle10 = Noodle
Holy_Lance = HolyLance()
Leaf = Leaf()
Albert2 = Albert("IT'S ALBERT""...."".... 2!", 900, Urumi, Modular_Tactical_Vest_1, 800)
Math_Sword = Sword("Math Sword", "QUICK", 20, 10, 80)
orc = Character("Orc1", 100, sword, BodyArmor("Generic Armor", "BAD", 15, 2, 10), 10)
orc2 = Character("Wiebe", 1000, canoe, weibe_armor, 10)
Armor_Of_The_Gods = BodyArmor("Armor of the Gods", 999999999, 18, 99999999, 99999999999)
orc.attack(orc2)
orc2.attack(orc)
Albert = Albert("IT'S ALBERT!", 50, Noodle10, Cardstock_Armor, 90)
TROLL1 = Character("Dave", 999999999999999999999, Urumi, Modular_Tactical_Vest_1, 20)
TROLL2 = Character("Bob", 10, Slow_Sword, weibe_armor, 20)
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

orc = Character("Orc1", 100, sword, BodyArmor("Generic Armor", "BAD", 15, 2, 10), 20)
orc2 = Character("Wiebe", 1000, canoe, weibe_armor, 20)
orc.attack(orc2)
orc2.attack(orc)

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

Heisenwiebe = Boss("HEISENWIEBE", 250, Urumi, Modular_Tactical_Vest_1, 250, 100)
Papa_Pearson = Boss("Papa Pearson", 200, Math_Sword, Chestplate, 250, 100)
HOBO = Boss("Hobo.... It's a hobo. Not much more to say", 80, Slow_Sword, Cardstock, 80, 50)

R19A = Room("PARKING_LOT", "QUAD", "DRAMA_BUILDING", "SCIENCE_BUILDING", "R19A",
            "This is the classroom you are in right now. There are two doors on the north wall. There are two doors on"
            " the north wall. There is a big mailbox in the sky for some reason", "MAILBOX", None, None,
            [Cardstock(10), Noodle1, Tree_Of_Life])

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
                        [Albert, TROLL4], [])

QUAD = Room(None, None, "R_BUILDINGS", "W_BUILDINGS", "The Quad", "The main area. There is an ampitheatre here. There "
            "is also a couple of lamp posts.You can only go East and West, for some reason. ", "CEILING", "FLOOR")

W_BUILDING = Room("PARKING_LOT", "R_BUILDING", "QUAD", "PARKING_LOT", "W Building", "This is the W Building. It is a "
                  "two story masterpiece of a building. It,conveniently, is the building for languages.",
                  "THE SPANISH DILEMMA", "FLOOR")

MAILBOX = Room(None, None, None, None, "THE HOLY MAILBOX WELCOMES YOU!", "WELCOME TO SCHOOL WARRIOR, THE HIGHEST "
               "QUALITY GAME IN SCHOOL BASED" "CHOOSE YOUR OWN ADVENTURE GAMES! DEFEAT ONE BOSS AND COLLECT 20 ITEMS TO"
               "WIN THE GAME!", None, "R19A")

DRAMA_BUILDING = Room("NIGHTMARE_EDISON", "SHAKESPEARE_WORLD", "W_BUILDING", "PARKING_LOT", "The Drama Building", "This"
                      "is a long winding hallway. At the end there is a large telephone box. Paintings cover the wall",
                      "CEILING", None, Krishang)

R_BUILDINGS = Room("THE_ESSAY_TYPING", "GYM_PORTAL", "PARKING_LOT", "QUAD", "The R Buildings", "This is a row of "
                   "buildings. You can only go North, however. The other areas are blocked off.", "CEILING", None)

HOBO_WORLD = Room("CHALLENGE_AREA", None, None, None, "Hobo World", "YoU haVe DECidEd tO Go SoUtH! Welcome to Hobo "
                  "World, the realm of the desolate and the weak. Here, you must complete one of  three challenges- "
                  "Garbage collecting, tent folding, and the hardest one of all, finding 4 pieces of food. After you "
                  "face these challenges, you win the game!", None, None)

POOL = Room("POOL", "POOL", "POOL", "POOL", "The Pool", "CONGRATULATIONS, YOU'VE MADE IT TO THE POOL!", "POOL", "POOL")

THE_REALM_OF_HEISENWEIBE = Room("THE_MAZE", "THE_MAZE", "THE_MAZE", "THE_MAZE", " The Realm of Heisenwiebe", "Welcome"
                                " to a world unlike any other- THE REALM OF HEISENWIEBE. This place is a maze. Once you"
                                "enter the realm, you can not get out. Reach the end of the realm,fight the Heisenwiebe"
                                " himself, then you win.", "THE MAZE", "THE MAZE")

THE_DARK_TRENCHES_OF_PAPA_PEARSON = Room("THE_LONG_WINDING_HALLWAY", "LABYRINTH", "LABYRINTH", "LABYRINTH", "The Dark "
                                         "Trenches of Papa Pearson", "Welcome. There really is not much to say about "
                                         "this place. There is a jar of Jolly Ranchers. and Popcorn in the corner. In "
                                         "front of you is a long winding hallway that goes only north. It is dark. "
                                         "Really dark. Also, any other direction you go seems to drop you in sometime "
                                         "of labyrinth ", "CEILING", "FLOOR")

NIGHTMARE_EDISON = Room("NIGHTMARE_W_BUILDING", "NIGHTMARE_R19A", "NIGHTMARE_PARKING_LOT", "NIGHTMARE_SCIENCE_BUILDING",
                        "NiGhTmArE EDiSon.", "WELCOME! This is Nightmare Edison. It is the same map as before only "
                        "SPOOKY! Get back to the normal world to win the game.", "NIGHTMARE_CEILING", None)

CEILING = Room("CEILING", "CEILING", "CEILING", "CEILING", "The Ceiling", "This is the ceiling. Do not go up, again!",
               "CEILING", None)


SHAKESPEARE_WORLD = Room("HAMLET", "OTHELLO", "TAMING_OF_THE_SHREW", "ROMEO_AND_JULIET", "Shakespeare World", "You are "
                         "now in a medieval area. The buildings are that of 16th century.Everyone around you is wearing"                   
                         "some type of Victorian clothing. In this world, you must act on a play. Essentially, You are"
                         " dropped into the world of the play and must find the way out.", "THE_GENTLEMEN_OF_VERONA",
                         "THE_MERCHANT_OF_VENICE")

THE_SPANISH_DILEMMA = Room("PROBLEMA_CUATRO", "PROBLEMA_UNO", "PROBLEMA_TRES", "UN PROBLEMA DIFICIL",
                           "THE_SPANISH_DILEMMA", "Este cuarto tiene una problema ese necesita resolver. Tu necesecitas"
                           " resolver la problema rapidamente. Si tu resuelves en tiempo, tu seras GANAR!", "CEILING",
                           "PROBLEMA_DOS")

FLOOR = Room("FLOOR", "FLOOR", "FLOOR", "FLOOR", "FLOOR", "This is the floor", "FLOOR", "FLOOR")

CHALLENGE_AREA = Room("PATH_1", "HOBO_WORLD", "PATH_3", "PATH_2", "The Challenge Area", "Welcome to the Challenge area."
                      "This is a very dark and musty cave. From what it seems,in the cave there are walls that block "
                      "off certain areas. Kind of like a maze?", "CEILING", "FLOOR")

PATH_1 = Room("MINI_PATH_1", "HOBO_WORLD", "MINI_PATH_2", "DEAD_END", "The North Path", "This part of the challenge "
              "area is quite large. I don't like it. North and East seem to both have something", "CEILING", "FLOOR")

PATH_2 = Room("MINI_PATH_3", "DEAD_END", "MINI_PATH_4", "MINI_PATH_5", "The Western Path", "This part of the challenge "
              "is strange. Odd paintings cover the walls. South seems to go somewhere... or does it?", "CEILING",
              "FLOOR")

NIGHTMARE_PARKING_LOT = Room("NIGHTMARE_CEILING", None, "NIGHTMARE_W_BUILDING", "NIGHTMARE_FLOOR", "Nightmare Floor",
                             "Welcome to the Nightmare Version of the parking lot. All the cars are Hummers.Get spooked"
                             " by their carbon emissions and their excessive gas prices!", "NIGHTMARE_GYM_PORTAL",
                             "NIGHTMARE_R19A")

NIGHTMARE_W_BUILDING = Room("NIGHTMARE_EDISON", "NIGHTMARE_CEILING", "NIGHTMARE_R_BUILDINGS", "NIGHTMARE_EDISON", "The "
                            "Nightmare W Buildings", "The building in a never ending staircase. It's almost like... a "
                            "maze. But it isn't. However, there are a lot of signs that just say- Look out for the "
                            "start.", "NIGHTMARE_CEILING", "NIGHTMARE_EDISON")

NIGHTMARE_R19A = Room("NIGHTMARE_GYM_PORTAL", "NIGHTMARE_HOBO_WORLD", "NIGHTMARE_DRAMA_BUILDING", "NIGHTMARE_QUAD",
                      "Nightmare R19A", "This is a SpOoOky computer room. All of the computers are Windows 98 and are "
                      "slower than paces of snails. ", "NIGHTMARE_CEILING", "NIGHTMARE_EDISON")

NIGHTMARE_SCIENCE_BUILDING = Room("NIGHTMARE_QUAD", "NIGHTMARE_HOBO_WORLD", "NIGHTMARE_EDISON", "NIGHTMARE_FLOOR", "The"
                                  "Nightmare Science Buildings", "The classes are terrifying! They're taught by "
                                  "flat-earthers and people who are against vaccines. What has this world come to?!",
                                  "NIGHTMARE_FLOOR", None)

HAMLET = Room("NORTH_ROOM", "SOUTH_ROOM", "HALLWAY", "GROVE", "Hamlet", "Considered to be his best play, Hamlet is "
              "play in which Hamlet's father dies and it tells of his slow descent into madness. Get to the last scene "
              "to win", "CEILING", "FLOOR", None)

OTHELLO = Room("VENITIAN_STREET", "COUNCIL_CHAMBER", "SEA_PORT", "THE_CASTLE", "Othello", "Welcome to othello- The "
               "play, not the game. The play is about a Venetian soldier who passed over promotion by Othello and the "
               "story of how Othello undermines him, causing him to get revenge. Get to the last scene to win",
               "CEILING", "FLOOR")

THE_MERCHANT_OF_VENICE = Room()

PROBLEMA_UNO = Room("SECCION_UNO", "SECCION_DOS", "SECCION_TRES", "SECCION_QUATRO", "Problema Uno", "Es el primero"
                    " problema. You need to solve one puzzle and ten queestions", "CEILING", "FLOOR")

PROBLEMA_DOS = Room("SECCION_CINCO", "SECCION_SEIS", "SECCION_SIETE", "SECCION_OCHO", "Problema Dos", " Es el segundo "
                    "problema. This challenges requires you to complete four mazes and code in spanish ", None, None)

PROBLEMA_TRES = Room("LOS_PANQUEQUES", "EL_FUTURO", "EL_PRETERITO", "PRESENTE-PROGRESIVO", "Problema Tres", "Es el "
                     "trecero problema. In this one, you have to answer high intensity questions on verbs and "
                     "vocabulary", "VOCABULARIO_UNO", None)

THE_MAZE = Room("NULL_PATH", "IMPORT_GOD_PATH", "__INIT__PATH", "BAD_JOKE_PATH", "The Maze", "Welcome to the "
                "Heisenwiebe Maze. This maze has each path leading to a different aspect of the Heisenwiebe. Complete "
                "the path you go down to win. At the end of each path, you will fight the HEISENWIEBE himself",
                "SPAAAACE_PATH", "LUCKY_7'S_PATH")

THE_LONG_WINDING_HALLWAY = Room("MATH_JESUS", "2019'S_CANCEL_OUT", "2019^2", "THE_INTEGRAL_OF_THE_SIN_OF_THE_COSINE_OF_"
                                "THE_DERIVATIVE_OF_INTEGRAL_OF_THE_LOG_OF_X_SQUARED_CUBED_SQUARED", "The Long Winding "
                                "Hallway", "It's... just... It'sj really difficult. Complete all 4 to win", "CEILING",
                                "FLOOR")

player = Player(R19A, [])
print(player.inventory)

# Controller
playing = True
directions = ['north', 'south', "west", "east", "up", "down"]
short_directions = ['n', 's', 'w', 'e', 'u', 'd']
inventory_terms = ["Inventory", "I", "inventory", "i"]
while playing:
    print(player.current_location.name)  # player- indicates the instantiated object. current_location- refers to the
    # variable. .name = refers to the attribute of the location
    print(player.current_location.description)
    if len(player.current_location.items) > 0:
        print("There are the following items in the room:")
        print()

        for num, item in enumerate(player.current_location.items):
            print(str(num + 1) + ": " + item.name)
        pick_up_command = input("What item would you like to pick up")

        for item in player.current_location.items:
            if pick_up_command in item.name:
                print("You have selected %s" % pick_up_command)
                player.inventory.append(item)
            elif pick_up_command not in item.name:
                print("Ok. You do not pick up an item!")
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
# Get rid of room items
