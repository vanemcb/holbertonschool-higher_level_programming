#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    my_list2 = my_list[:]
    for num in my_list:
        if num == search:
            my_list2[i] = replace
        i += 1
    return my_list2
