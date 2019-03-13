class Character(object):
    def __init__(self, name, health: int, weapon, armor):

        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage: int):
        if self.armor.armor_amt > damage:
            print("No damage is done because of some AMAZING armor")
        else:
            self.health -= damage - self.armor.armor_amt
        print("%d has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks for %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)

sword = Sword("Sword","Quick", 15, 20, 10)
canoe = Sword("Canoe Sword", "SLOW", 90, 150, 42)
weibe_armor = BodyArmor("Armor of the gods", "GOOD", 18, 10000000000000000000000000000)


orc = Character("Orc1", 100, sword, BodyArmor("Generic Armor", "BAD", 15, 2))
orc2 = Character("Weibe", 1000, canoe, weibe_armor)
orc.attack(orc2)
orc2.attack(orc)