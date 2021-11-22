def print_list_integer(my_list=[]):
    for item in my_list:
        if type(item) == int:
            print("{:d}".format(item))
