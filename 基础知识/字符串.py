'''字符大小写'''
name='i am a good guy'
print(name.title())#the first letter
print(name.upper())#all
print(name.lower())#lower case character

#合并字符串
first_name='sheng'
last_name='liu'
full_name=first_name+''+last_name
print(full_name)
print('hello,yaoyihsu'+'i love you'+full_name)

#使用制表符或者换行符来添加空白
print('liuhsneg')
print('\tliusheng')
print('name:\nliusheng\tyaoyishu')

#删除空白
name="smd d sasa d ada "
name.rstrip()#删除末尾空白
name.lstrip()#开头
name.strip()#删除两端
print(name)#结果依旧会显示空格，因为只是暂时删除
name=name.rstrip()#需要将执行结果重新赋值
print(name)
