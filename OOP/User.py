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


# what is functional programming ?
# seperation of concern and also seperate - data and - function

# Pure functions
# [1,2,3] ----- > function (input) ------> [output]
# same input should give same output
# function should not generate any side effects, i.e. it should not change the outside world

# pure function
# the below function is a pure function
def multiple_by_2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

# the above function does create the same results for same input
# the above function doesnot change or has any side affects the outside world, thus it is a pure function

# in place if it had a print statement in the function it would affect the outside world, and secondly if the list is global thus it work and change the list outside the function scope, thus it would conflict the statement of a pure function


print(multiple_by_2([1, 2, 3, 4]))  # example of a pure function
