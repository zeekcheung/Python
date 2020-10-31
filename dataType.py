# -*- coding:utf-8 -*-
L = ['Bart','Lisa','Adam']      # 列表 list  []
T = ('Bart','Lisa','Adam')      # 元组 tuple ()
D = {'name1': 'Bart', 'name2': 'Lisa','name3':'Adam'}    # 字典 dict {}
S = set([1,2]) & set([2,3])     # 集合 set ()

print(type(L))
for x in L:
    print(x)

print(type(T))
for x in T:
    print(x)

print(type(D))
for key,name in D.items():
    print('%s:%s' % (key,name))

print(type(S))
for x in S:
    print(x)
