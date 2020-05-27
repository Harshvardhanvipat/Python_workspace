# object oriented programming
# organized code
# structured code and modularized code
# class name are Camel Case

class PlayerCharacter:
    # Class attributes

    membership = True

    def __init__(self, name='anonymous', age=0):  # constructor
        self.name = name
        self.age = age
        # self.name = name

    def run(self):
        print('run')

    def shout(self):
        return (self)

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2


player1 = PlayerCharacter('test', 2)


print(player1.shout())
