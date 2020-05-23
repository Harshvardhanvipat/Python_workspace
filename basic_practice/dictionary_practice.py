# dictonary

is_old = True
is_licenced = True

if is_old:
    print('YOU ARE OLD ENOUGH TO DRIVE THE CAR')
else:
    print('You are young please come back later')

#ternary Operator

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

print(4>5)
print(4<5)
print(4==5) # == is used to check and = is used to assign a value
print(4>=5)
print(4<=5)
print(4 != 5)
print(not(True))


is_magician = True
is_expert = True

# check if magician and expert : "Print you are an master magician"
# 

if is_magician and is_expert:
    print("You are a master magician")

elif is_magician == True:
    if is_expert == False:
        print("Atleast you are getting there")

elif is_magician == False:
    print("You need magical power")

