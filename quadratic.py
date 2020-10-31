# -*- coding:utf-8 -*-
import math
def quadratic(a,b,c):
    delta = b*b-4*a*c
    if delta<0:
        print(Exception)
    else:
        sqrt_delta = math.sqrt(b*b-4*a*c)
        return [(-b+sqrt_delta)/(2*a),(-b-sqrt_delta)/(2*a)]

a = int(input('Please input a:'))
b = int(input('Please input b:'))
c = int(input('Please input c:'))
r = quadratic(a,b,c)
print(r)