released = {
    "iphone": 2007,
    "iphone 3g": 2008,
    "iphone 3GS": 2009,
    "iphone 4": 2010,
    "iphone 4s": 2011,
    "iphone 5": 2012
}

print(released)

states = {
    "CA": "California",
    "FL": "Florida",
    "AK": "Alaska",
    "GA": "Georgia"
}

print(states["CA"])
print(states["AK"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000
    }
}

print(nested_dictionary["GA"]["POPULATION"])
print(nested_dictionary["FL"]["NAME"])

georgia = nested_dictionary["GA"]
print(georgia)

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000,
        "CITIES": [
            "Fresno",
            "San Francisco",
            "Los Angeles"
        ]
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000,
        "CITIES": [
            "Miami",
            "Orlando",
            "Tampas",
            "Jacksonville"
        ]
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000,
        "CITIES": [
            "Anchorage",
            "Fairbanks",
            "Barrow"
        ]
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000,
        "CITIES": [
            "Atlanta",
            "Savannah",
            "Columbia"
        ]
    }
}
print(complex_dictionary["AK"]["CITIES"][0])
