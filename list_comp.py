# -*- coding:utf-8 -*-
def func(x):
    r = ''
    if(isinstance(x,str)):       
        r = r + x[0].upper()
        for s in x[1:]:
            r = r + s.lower()
    else:
        r = r + 'NotStr'

    return r

L1 = ['Hello','worLd',18,'Apple',None]
L2 = [func(x) for x in L1]                  # 列表生成器 [func(x) for x in L] 映射生成列表
print(L2)