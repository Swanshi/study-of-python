#整数运算
a=7+8
print(a)
b=(6-8)
print(b)
c=2*7
print(c)
d=3/2
print(d)
f=10**2#乘方运算
print(f)

#浮点数
a=0.1+0.2
print(a)#结果会有多余位数

#类型错误
age=33
print('happy'+age+'rd birthday!')#报错，因为不能混合数据类型拼接（字符和数字）
print('happy'+str(age)+'rd birthday!')