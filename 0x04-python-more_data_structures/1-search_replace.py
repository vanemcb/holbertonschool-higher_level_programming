#!/usr/bin/python3
def search_replace(my_list, search, replace):

    my_list2 = my_list[:]
    for i, num in enumerate(my_list):
        if num == search:
            my_list2[i] = replace

    return my_list2
