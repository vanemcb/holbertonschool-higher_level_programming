#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    my_list2 = []
    boolean = False
    for num in my_list:
        if num % 2 == 0:
            boolean = True
        my_list2.append(boolean)
