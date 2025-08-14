class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def charge(self):
        return f"{self.model} is charging."

    def info(self):
        return f"{self.brand} {self.model} with {self.battery}mAh battery."

class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, cooling_system):
        super().__init__(brand, model, battery)
        self.cooling_system = cooling_system

    def game_mode(self):
        return f"{self.model} is in gaming mode with {self.cooling_system} cooling."

phone1 = Smartphone("Samsung", "Galaxy S23", 4000)
phone2 = GamingPhone("ASUS", "ROG Phone 6", 6000, "Advanced")

print(phone1.info())
print(phone1.charge())
print(phone2.info())
print(phone2.game_mode())




class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing ⛴️")

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
