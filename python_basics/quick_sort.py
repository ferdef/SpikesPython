#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Author: Fernando de Francisco
#

from random import randrange

def __choose_pivot3(elements):
    """Take 3 ramdom elements and select the mid value as pivot"""
    num = len(elements)
    pivot_list = [randrange(num) for x in range(3)]
    # TODO Select mid value
    pivot = pivot_list[1]
    return pivot


def __choose_pivot(elements):
    """Take ramdom element"""
    num = len(elements)
    pos = randrange(num)
    pivot = (pos,elements[pos])

    return pivot

def quick_sort(elements):
    """Quicksort algorithm passing a tuple as argument"""
    pivot = __choose_pivot(elements)
    lower_list = []
    upper_list = []
    for index, element in enumerate(elements):
        if index!=pivot[0]:
            if element<pivot[1]:
                lower_list.insert(0, element)
            else:
                upper_list.insert(0, element)
    if len(lower_list)>1:
        lower_list = quick_sort(lower_list)
    if len(upper_list)>1:
        upper_list = quick_sort(upper_list)
    new_list = lower_list + ['['+str(pivot[1])+']',] + upper_list

    return new_list


def __generate_list(number, max_value):
    elements = []
    for counter in range(number):
        elements.append(randrange(max_value))
    return elements

if __name__ == "__main__":
    elements = __generate_list(100,100)
    print "Original List (%d):" % len(elements)
    print elements
    sorted_elements = quick_sort(elements)
    print "Ordered List (%d):" % len(sorted_elements)
    print sorted_elements
