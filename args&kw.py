# -*- coding:utf-8 -*-
def product1(*args):             # 可变参数
    r = 1
    for x in args:
        r = r * x
    print(r)
    return

product1(1,2,3)

def product2(**kw):             # 关键字参数
    for key,value in kw:
        print('key='+key,'value='+value)
    return

product2(a='1',b='2',c='3')