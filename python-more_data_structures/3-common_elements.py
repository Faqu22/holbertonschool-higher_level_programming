#!/usr/bin/python3
def common_elements(set_1, set_2):
    s1, s2, comm = list(set(set_1)), list(set(set_2)), []
    for x in range(len(s1)):
        for y in range(len(s2)):
            if s1[x] == s2[y]:
                comm.append(s1[x])
    return comm
