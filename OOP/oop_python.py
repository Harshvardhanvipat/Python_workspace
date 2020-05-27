# object oriented programming
# organized code
# structured code and modularized code
# class name are Camel Case

class PlayerCharacter:
    def __init__(self, name):  # constructor
        self.name = name

    def run(self):
        print('run')


player1 = PlayerCharacter('test')


print(player1.name)
