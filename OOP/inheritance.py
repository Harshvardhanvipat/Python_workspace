class User:

    def signIn(self):
        print("Logged in ")


class Wizard (User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power :  {self.power}')


class Archer (User):
    def __init__(self, name, num_arrrows):
        self.name = name
        self.num_arrows = num_arrrows

    def attack(self):
        print(f'attacking with arrows: arrows left-{self.num_arrows}')


isinstance

wizard1 = Wizard('test', 40)
archer1 = Archer('test_archer', 100)
wizard1.attack()
archer1.attack()
