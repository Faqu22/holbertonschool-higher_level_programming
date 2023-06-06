#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l_a, l_b = list(tuple_a), list(tuple_b)
    a = (0 if len(l_a) < 1 else l_a[0]) + (0 if len(l_b) < 1 else l_b[0])
    b = (0 if len(l_a) < 2 else l_a[1]) + (0 if len(l_b) < 2 else l_b[1])
    return (a, b)
