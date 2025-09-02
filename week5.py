class Superhero:
    def __init__(self, name, power, origin, level):
        self.name = name
        self.power = power
        self.origin = origin
        self.level = level  # e.g., Beginner, Intermediate, Advanced

    def introduce(self):
        return f"I am {self.name} from {self.origin}, and I fight using {self.power}!"

    def upgrade_level(self):
        if self.level == "Beginner":
            self.level = "Intermediate"
        elif self.level == "Intermediate":
            self.level = "Advanced"
        return f"{self.name} is now {self.level} level!"

class FlyingHero(Superhero):
    def __init__(self, name, power, origin, level, flight_speed):
        super().__init__(name, power, origin, level)
        self.flight_speed = flight_speed  # in km/h

    def introduce(self):
        return f"{self.name} flies at {self.flight_speed} km/h and uses {self.power} to save the day!"

class SecretHero(Superhero):
    def __init__(self, name, power, origin, level, secret_identity):
        super().__init__(name, power, origin, level)
        self.__secret_identity = secret_identity  # private attribute

    def reveal_identity(self):
        return f"{self.name}'s secret identity is {self.__secret_identity}"

class Vehicle:
    def move(self):
        return "Moving..."

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())