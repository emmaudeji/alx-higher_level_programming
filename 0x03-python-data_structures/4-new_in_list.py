#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    for _ in range(len(my_list)):
        new_list.append(my_list[_])
    if idx < 0:
        return new_list
    elif idx >= len((new_list)):
        return new_list
    else:
        new_list[idx] = element
        return new_list
