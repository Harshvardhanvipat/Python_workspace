# map(), filter, zip, reduce function

# map is a pure function

# below map function is a pure function

my_list = [1, 2, 3]


def multiple_by2(item):
    return item*2


# this print statement takes a function and a list as there arguments, and returns a new list that is not changed. As you can see that my_list is unchanged
# Thus map function doesnot change the my_list, rather it creates a new list  and returns that list
# with map we get the same number of items as given in
print(list(map(multiple_by2, my_list)))
print(my_list)


# filter

def check_odd(item):
    return item % 2 != 0


print(list(filter(check_odd, my_list)))
