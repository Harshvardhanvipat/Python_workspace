# lambda functions are the functions those are only used once
# they are also called anoymous function
my_list = [1, 2, 3]


# lambda  param: action(param)


print(list(map(lambda item: item*2, my_list)))  # this is a lambda function

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(my_list)


# lambda expression
# square the list

print(list(map(lambda item: item*item, my_list)))

a = [(101, -56), (0, 2), (4, 3), (21, 83), (10, -1), (9, 9)]
# we are sorting the tuples on the basis of second key and the lambda function used here is used to specify the key
a.sort(key=lambda x: x[1])
print(a)
