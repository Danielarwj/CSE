import timeit

t = timeit.Timer()
print(t.timeit())


class Planet(object):
    def __init__(self, rings, talking, orbit):
        self.gravity = True
        self.density = 0.693
        self.gravitational_force_exerted_by_planet = orbit
        self.state_of_matter = "GAS"
        self.rings = rings
        self.talking = talking
        self. time_spent_orbiting = 0

    def orbiting(self):
        self.time_spent_orbiting += t
        if self.time_spent_orbiting >= 1:
            print("You've been orbiting for a while there")
        if self.time_spent_orbiting >= 4:
            print("Your ship exploded from orbiting too long")
            return

    def actual_flying(self, fuel, flying):
        fuel = 100
        flying = True
        if flying == True :
            print("You are now flying")
            fuel -= 10
        if fuel == 0:
            print("You can not fly. You have no fuel")
        return


my_planet = Planet(True, True, 10.44)
my_planet.actual_flying(10, True)

