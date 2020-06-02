my_file = open('test.txt')
print(my_file)  # prints out the object type and its specification

# print(my_file.read())
# doesnot print anything as the cursor is at the end to fix this we use my_file.seek(0)
# print(my_file.read())
# print(my_file.read())

print(my_file.readlines())  # returns a list


my_file.close()
# you need to close the file once you are done reading and processing the file


# read write and append mode are the most important operations used

# file paths
with open('test.txt', mode='w') as my_file_without_close:
    text = my_file_without_close.write('what is going on ? ')
    # print(my_file_without_close.readlines())
