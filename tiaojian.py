#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
条件判断第一课

age = input('please input your name:')
age = int(age)
if age >= 18:
	print('your age is',age)
	print('adult')
else:
	print('your age is',age)
	print('teenager')
'''
''' 条件判断第二课
age = input('please input your name:')
age = int(age)
if age >= 18:
	print('your age is',age)
	print('adult')
elif age>=6:
	print('teenager')
else:
	print('kid')
'''
'''条件判断第三课

练习

小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：

代码开始:


name=input('请输入您的姓名:')
print('嗨,',name,'您好!欢迎进行BMI指数测试：')
height=input('请输入您的身高(m):')
weight=input('请输入您的体重(kg):')
h= float(height)
w= float(weight)
bmi= w/h**2
if bmi<=18.5:
	print('您好%s,您的BMI指数为%.1f,体重过轻。' % (name,bmi))
elif bmi<=25:
	print('您好%s,您的BMI指数为%.1f,体重正常。'%(name,bmi))
elif bmi<=28:
	print('您好%s,您的BMI指数为%.1f,体重过重,请注意饮食。' %(name,bmi))
elif bmi<=32:
	print('您好%s,您的BMI指数为%.1f,身体肥胖,请注意减肥。' %(name,bmi))
else:
	print('您好%s,您的BMI指数为%.1f,您已经处于严重肥胖的状态,需要进行治疗。' %(name,bmi))

代码结束:

错误:elif bim<=18.5 后需要跟 : 符号

'''

'''
	for ... in...循环学习

code start

names =['Michael','Bob','Tracy']
for name in names:
	print(name)

code end

code2 start

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum + x
print(sum)


code2 end

如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：


print(list(range(5)))


sum = 0
for x in range(101):
	sum = sum + x
print(sum)




while 循环


我们要计算100以内所有奇数之和

sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n-1
print(sum)



sum = 0

n = 100

while n >=0:
	sum = sum + n
	n-=1
print(sum)


sum = 0
n=1

while n <=100:
	sum = sum + n
	n+=1
print(sum)

100内的累成计算


acc = 1
n =1

while n <=100:
	acc= acc * n
	n+=1
print(acc)

'''


'''

L = ['Bart','Lisa','Adam']

三种方法

for x in L:
	print('Hello,%s!'%x)

L = ['Bart','Lisa','Adam']

n=0
while n<len(L):
	print('Hello,',L[n],'!')
	n+=1

L = ['Bart','Lisa','Adam']
n=0
while n<len(L):
	print('Hello,%s!'%L[n])
	n+=1
'''