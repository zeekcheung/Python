#数据类型与变量
n = 123
f = 456.789
s1 = 'Hello,world'
s2 = 'Hello,\'Adam\''   # 转义字符
s3 = r'Hello,"Bart"'    # r'' 内部字符串默认不转义
s4 = r'''hello,     
Lisa!'''   # 打印多行字符串

L = [n,f,s1,s2,s3,s4]
print(L)

n1 = 72
n2 = 85
r = (n2-n1)/n2 * 100
print('n1/n2 = %0.1f%%' % r)