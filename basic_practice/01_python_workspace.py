print ('harshvardhan')
#fundamental data types 

# we are talking about floating point number
int
float


# rint(type(6))
# print (type(2-3))
# print(type(2/4))
# print(type(20+1.1))
print(2**3)
#classes -> custom data types

#specialized data types 
# modules -> extensions 
None # like the idea of 0 -> nothing 

#math functions 
# data types 
print(round(23.23423, 2))

#operator precedence
print((20-3) + 2**2)
print(bin(9))

# result of this operation would be 21

# string testing start here 
tet = "Hi this is a string "
print(tet)
#  string concatenation 
print('Hello' + ' ' + 'world' ) # this is an example of string concatenation 

# formatted strings 
age = 55
name = 'test'
print(f'hi {name} you are {age} years old') # python 3 new feature
print("Hi your name is {} and your age is {}".format(name, age))

# string manipulation 
 
example_string = "012345678"

# [start:stop:stepover]
print(example_string[0:4])
print(example_string[:7])
print(example_string[::1])
print(example_string[-1]) #this means that start at the end

print (example_string[::-1]) # this means you reverse the string 

# string slicing string_name[start: stop : stepover]
# string are immutable 
test_string = "this is a test string"
# test_string[0] = 'T' // this will not work as strings are immutable
# parts of a strings cannot be reassigned 
# only new values can be assigned 
test_string = "How are you doing ? Says Joey " # here the old value is lost and new value is assigned to the variable

print(len(test_string)) # len starts from 1 and not from 0

# string methods                
quote = "What needs to be done, needs to be done"
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be','me'))

# getting user input in python
birth_year = input("What was the year you were born")
curr_year = 2020
age = curr_year - int(birth_year)
print(f"ÿour age is {age}")






