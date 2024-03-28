class Warrior():
    def __init__(self,  name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1

    def walk(self):
        print(f"{self.name} гуляет")

    def info(self):
        print(f"имя воина - {self.name}")
        print(f"цвет волос воина - {self.hair_color}")
        print(f"сила воина - {self.power}")
        print(f"выносливость воина - {self.endurance}")


war2 = Warrior("Stepa",7,20,"black")
war1 = Warrior("Jack",8,20,"red")

print(war2.name)
print(war2.power)
print(war2.endurance)
print(war2.hair_color)
war2.eat()
war2.eat()
war2.eat()
print(war2.power)




