# dictonary

is_old = True
is_licenced = True

if is_old:
    print('YOU ARE OLD ENOUGH TO DRIVE THE CAR')
else:
    print('You are young please come back later')

# ternary Operator

is_friend = False
can_message = "Message allowed" if is_friend else "not allowed to message"

print(can_message)

# short circuiting
is_australia_a_country = True
is_test = True
if is_australia_a_country and is_test:
    print("Australia is a country")

# || && these are used for short curcuiting as

# Logical operators

# print(4>5)
# print(4<5)
# print(4==5) # == is used to check and = is used to assign a value
# print(4>=5)
# print(4<=5)
# print(4 != 5)
# print(not(True))


is_magician = True
is_expert = True

# check if magician and expert : "Print you are an master magician"
#

# if is_magician and is_expert:
#     print("You are a master magician")

# elif is_magician == True:
#     if is_expert == False:
#         print("Atleast you are getting there")

# elif is_magician == False:
#     print("You need magical power")

# == checks for equality
print(True == 1)  # true
print("" == 1)  # false
print([] == 1)  # false
print(10 == 10.0)  # true
print([] == [])  # true

# iterables

# user = {
#     'name': 'Golem',
#     'age' : 5005,
#     'can_swim' : False
# }

# for item in user.items():
#     print(item)

# for item in user.values():
#     print(item)

# for item in user.keys():
#     print(item)

# counter

# my_list = [1,2,3,4,5,6,7,8,9,10]
# total_of_list = 0
# for item in my_list:
#     total_of_list += item
# print(total_of_list)

# range function

# picture = [
#     [0,0,0,0,0,0,1,0,0,0],
#     [0,0,0,0,0,0,1,0,0,0],
#     [0,0,0,0,0,0,1,0,0,0],
#     [0,0,0,0,0,0,1,0,0,0],
#     [0,0,0,0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0,0,0,0]
# ]

# for itemss in picture:
#     for value_of_list in itemss:
#         if value_of_list == 0:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print("\n")

# find the duplicates
some_list = ['a', 'b', 'c', 'd', 'e', 'd', 'm', 'n', 'm']

duplicates = []
for unit in some_list:
    if some_list.count(unit) > 1:
        if unit not in duplicates:
            duplicates.append(unit)

print(duplicates)


def say_hello():
    print('Hello ! what are you doing ??')


say_hello()

# parameters are the used when you define a function


def add_numbers(value1, value2):
    value3 = value1 + value2
    print(value3)


# here 2 and 3 are arguments
# parameters are used when functions are defined
# arguments are used when a function is called
add_numbers(2, 3)


def checkDriverAge(age):
    if int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) < 18:
        print("Sorry, you are too young to drive this car")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride")


print('hello')
checkDriverAge(21)
