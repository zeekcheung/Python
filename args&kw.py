# -*- coding:utf-8 -*-
def func1(*args):             # 可变参数
    r = 1
    for x in args:
        r = r * x
    print(r)

func1(1,2,3)         #直接传参
func1(*[1,2,3])      #先组装成list
func1(*(1,2,3))      #先组装成tuple

def func2(**kw):             # 关键字参数
    for key, value in kw.items():
        print('%s %d' % (key,value))

func2(a=1,b=2)                #直接传参
func2(**{'a': 1, 'b': 2})     #先组装成dict  