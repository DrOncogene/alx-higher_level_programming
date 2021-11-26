#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weights = [item[1] for item in my_list]
    total_sum = sum(list(map(lambda x: x[0]*x[1], my_list)))
    return total_sum / sum(weights)
