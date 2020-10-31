# -*- coding:utf-8 -*-
from typing import Iterable, Iterator

L = []
T = ()
D = {}
S = set(L)
s = 'str'

'''Type = [L,T,D,S,s]
for x in Type:
    print(x)
    print('is Iterable?') 
    print(isinstance(x,Iterable))
    print('is Iterator?') 
    print(isinstance(x,Iterator))
    print(isinstance(iter(x),Iterator))
'''
s1 = iter(s)
print(next(s1))
print(next(s1))
print(next(s1))

# list,tuple,dict等可用于for循环的类型都是 iterable，但不是 iterator
# 使用 iter()函数可将 iterable 转换为 iterator

    




