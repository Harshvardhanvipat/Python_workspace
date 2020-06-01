# lambda functions are the functions those are only used once
# they are also called anoymous function
my_list = [1, 2, 3]


# lambda  param: action(param)


print(list(map(lambda item: item*2, my_list)))  # this is a lambda function

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(my_list)
