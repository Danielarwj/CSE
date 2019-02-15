t = 1


class Planet(object):
    def __init__(self, rings, talking, orbit, time, matter):
        self.gravity = True
        self.density = 0.693
        self.gravitational_force_exerted_by_planet = orbit
        self.state_of_matter = matter
        self.rings = rings
        self.talking = talking
        self. time_spent_orbiting = time

    def actual_flying(self, fuel, flying):
        if flying:
            print("You are now flying")
            fuel -= 10
        else:
            print("You can't fly this ship")
        if fuel == 0:
            print("You can not fly. You have no fuel")
        if self.gravitational_force_exerted_by_planet > 10:
            print("The gravitational force is too strong. EEAHHHH!")
            print("You burned up from the atmosphere")
        if self.time_spent_orbiting > 5 or self.gravitational_force_exerted_by_planet > 10:
            if self.time_spent_orbiting > 5:
                print("You've been orbiting too long. Your ship explodes")
            print("You can't fly this plane. IT'S DESTROYED!")
        if self.talking:
            print("The planet speaks to you! You lose all of your fuel. No one knows why.")
            fuel -= 100
        if self.rings:
            print("There are rings on this planet. The existence of rings causes your ship to start going into the plan"
                  "et very fast.")

    def landing(self):
        if self.state_of_matter == "GAS":
            print("You can't land on this planet")
        if self.state_of_matter == "SOLID":
            print("You're now on the planet. Nothing happens..."
                  "..."
                  "There is now a comet... It misses the planet. "
                  "You are now safe")


my_planet = Planet(False, False, 9, 4, "SOLID")
my_planet.actual_flying(100, True)
my_planet.landing()
