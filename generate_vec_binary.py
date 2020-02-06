#!/bin/python3


'''
Generate a vector of length m with exactkly n ones
'''

def generate_vec_binary(n, m):
    res = []
    lower = sum(2**i for i in range(m-4))
    upper = sum(2**i for i in range(m-4, m))+1
    for i in range(lower, upper):
        val = bin(i)[2:].zfill(8)
        if sum([int(i) for i in val]) == 4:
            res.append(val)
    return res

if __name__ == '__main__':
	n,m = 4, 8
	print(generate_vec_binary(n,m))
