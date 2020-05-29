class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age

    # redefining dunder method __str__
    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __del__(self):
        print('deleted')

    def __call__(self):
        return ('yess??')


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
# del action_figure
print(action_figure())  # calling __call__


# method resolution order
class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.mro())
