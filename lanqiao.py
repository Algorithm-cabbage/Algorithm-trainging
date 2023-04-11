# while True:
#     n=list(map(int,input().split()))
#     print(n[0]+n[1])
# while True:
#     try:
#         n=list(map(int,input().split()))
#         print(n[0]+n[1])
#     except:
#         break    //注意这个try，非常重要
# height=float(input("请输入您的身高在(单位：m)：)"))
# weight=float(input("请输入您的体重(单位：Kg):)"))
# bmi=round((weight/(height*height)),2)
# print("您的BMI指数为：",bmi)
# name='熊天'
# age=20
# print('我的名字叫'+name+',我的年龄是'+str(age))
#
# for index in range(10):
#     print(index)
# name='1'
# for index in range(10):
#     if name=='小王':
#         print('hello')
#     else:
#         print('nothing')
# str='good d'
# print(str[100])
# while True:
#  try:
#     a=int(input())
#     b=int(input())
#     print(a+b)
#  except:
#     break
#
# while True:
#     try:
#         a,b=map(int,input().strip().split())
# //a,b=map(int,input().strip().split())
#         print(a+b)
#     except:
#         break
# //实验
# a,b=map(int,input().strip().split())
#
# for i in range(26):
#     print('*',end='')
# print()
# print("Hello World!")
# for i in range(26):
#     print('*',end='')
# import math
import itertools
import math

# print('*'*26)
# print('Hello World!')
# print('*'*26)
# a,b,c=map(int,input().strip().split())
# print(max(a,b,c))
#
# l=list(map(int,input().strip().split()))
# l.sort() #等价于l.sort(reverse=False)    False默认从小到大。True默认从大到小
# print(l[-1])
#
# str1='China'
# for i in range(len(str1)):
#     if str1[i]>='a' and str1[i]<='z':
#            print(chr(ord('a')+(ord(str1[i])-ord('a')+4)%25),end='')
#     elif str1[i]>='A' and str1[i]<='Z':
#            print(chr(ord('A')+(ord(str1[i])-ord('A')+4)%25),end='')

# inp=input()
# for i in inp:
#     tmp=chr(ord(i)+4)
#     if not tmp.isalpha():
#         tmp=chr(ord(tmp)-26)
#     print(tmp,end='')
#


#
# while True:
#     try:
#      a,b=map(int,input().strip().split())
#      print(a+b)
#     except:
#      break

# l=list(map(int,input().strip().split()))
# l.sort()
# print(l[-1])
#
# def tss(n):
#     f1,f2,f3=1,2,3
#     if n<=4:
#         return n
#     else :
#         for i in range(3,n):
#             fn=f3+f1
#             f1,f2,f3=f2,f3,fn
#         return fn
#
# while True:   #太耗费时间
#     n=int(input())
#     if n==0:
#         break
#     else:
#         print(tss(n))


#
# l=[0,1,2,3]
# for i in range(4,55):
#     l.append(l[i-3]+l[i-1])
# while True:
#     n=int(input())
#     if n==0:
#         break
#     print(l[n])
# F=float(input())
# c='%.2f'%(5*(F-32)/9)
# print('c='+c) # 如果用‘c=’,c 结果会多出一个空格
#


#
# def fx(a,b):
#     if a>b:
#         return 1
#     else :
#         return 0
#
# a,b,c=map(int,input().strip().split())
#
# if fx(a,b):
#     if fx(a,c):
#         print(a)
#     else :
#         print()

# l=list(map(int,input().strip().split()))
# l.sort()
# print(l[-1])

# x=int(input())
# if x<1:
#     print(x)
# elif x>=1 and x<10:
#     print(2*x-1)
# elif x>=10:
#     print(3*x-11)


# n=int(input())
# if n>=90:
#     print('A')
# elif n>=80 and n<90:
#     print('B')
# elif n>=70 and n <80:
#     print('C')
# elif n>=60 and n<70:
#     print('D')
# else:
#     print('E')

# n=input()
# print(len(n))
# for i in n:
#     print(i,end=' ')
# print()
# print(n[::-1])
#
#
#
# n=int(input())
# if n<=100000:
#     y=n/10
# elif n>100000 and n<=200000:
#     y=10000+(n-100000)*(7.5)/100
# elif n>200000 and n<=400000:
#     y=10000+100000*(7.5)/100+(n-200000)/20
# elif n>400000 and n<=600000:
#     y=10000+100000*(7.5)/100+200000/20+(n-400000)*3/100
# elif n>600000 and n<=1000000:
#     y=10000+100000*(7.5)/100+200000/20+200000*3/100+(n-600000)*1.5/100
# elif n>1000000:
#     y = 10000 + 100000 * (7.5) / 100 + 200000 / 20 + 200000 * 3 / 100 + 400000 * 1.5 / 100+(n-1000000)/100
# print(int(y))

#
# m,n=map(int,input().strip().split())
# z=1
# if m>n:
#     k=n;
# else :
#     k=m
# while k>=1:
#     if(m%k==0 and n%k==0):
#         break
#     k=k-1
# print(k,end=' ')
# print(int(m*n/k))


# //高效题解
# a,b=map(int,input().strip().split())
# s=a*b
# while a%b:
#     a,b=b,a%b
# print(b,s//b)

# singw=input()
# x,y,z,o=0,0,0,0
# for i in singw:
#     if i.isalpha():
#         x=x+1
#     elif i.isdigit():
#         y=y+1
#     elif i==' ':
#         z=z+1
#     else :
#         o=o+1
# print(x,y,z,o)

#
# n=int(input())
# sum=0
# a=2
# for i in range(n):
#     sum+=a
#     a=a*10+2
# print(sum)

# 巧妙应用字符串的复制功能
# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum+=int('2'*i)
# print(sum)


# n=int(input())
# s=1
# sn=0
# for i in range(1,n+1):
#      s=s*i
#      sn+=s
# print(sn)

# a,b,c=map(int,input().strip().split())
# sum=float(0)
# for i in range(1,1+a):
#     sum+=i
# for i in range(1,1+b):
#     sum+=pow(i,2)
# for i in range(1,1+c):
#     sum+=float(1/i)
# print('%.2f'%sum)

# for i in range(100,1000):
#     if (i/100)**3+(i%10)**3+(i/10%10)**3 ==i :
#         print(i)


# for i in range(100,1000):
#
#     if i==(i//100)**3+(i//10%10)**3+(i%10)**3:
#
#         print(i)
#
#
# n=int(input())
# if n==0 or n==1:
#     print(n,'its factors are',n,end='')
# else:
#  print(n,'its factors are ',end='')
#  for i in range(1,n//2+1):
#     if n%i==0:
#         print(i,end=' ')
#
# n=int(input())
# num=0
# l=[]
# for i in range(1,int(pow(n,0.5))+1):
#     if(n%i==0):
#         l.append(i)
#         num+=i
# if  num==n:
#     print(n,"its factors are",end=' ')
# for j in range(len(l)):
#     print(l[j],end=' ')
# print()
#
#
# n=int(input())
# for i in range(2,n):
#     b=[1]
#     sum=1
#     c=int(pow(i,0.5))+1
#     for j in range(2,c):
#         if(i%j==0):
#             b.append(j)
#             b.append(int(i/j))
#             sum+=j+int(i/j)
#     if sum==i:
#         print(i,'its factors are ',end='')
#         b.sort()
#         for z in range(len(b)):
#             print(b[z],end=' ')
#         print()
# n=int(input())
# sum=0
# j=2
# i=1
# sum=2
# for x in range(1,n):
#     j,i=j+i,j
#     sum+=j/i
# print('%.2f'%sum)
# m,n=map(int,input().strip().split())
# sum=0
# x=m/pow(2,n)
# for i in range(1,n):
#     sum+=float(m*3/2)
#     m=m/2
# sum+=x*2
# print('%.2f'%x,"%.2f"%sum)



# day=int(input())
# sum=1
# for i in range(1,day):
#     sum=(sum+1)*2
# print(sum)

# n=int(input())
# x=1.0
# x1=0
# while(abs(x-x1)>=0.00001):
#     x1=x
#     x=(x1+n/x1)/2
# print('%.3f'%x)
#
# n=int(input())
# for i in range(2,n+1):
#     z=1
#     for j in range(2,i):
#         if i%j==0:
#             z=0
#             break
#     if z==1:
#         print(i)

# l=list(map(int,input().strip().split()))
# l.sort()
# for i in l:
#     print(i)

#
# x=list(map(int,input().strip().split()))
# y=list(map(int,input().strip().split()))
# z=list(map(int,input().strip().split()))
# print(x[0]+z[2]+y[1],y[1]+z[0]+x[2])

# //整合版本
# ls=[input().split(),input().split(),input().split()]
#
# ls=list[map(int,input().strip().split())]
# print(len(ls))
# y=input()
# ls.insert(int(y))
# ls.sort()
# for i in ls:
#     print(i)

#
#
# l=list[map(int,input().strip().split())]
# print(l[0])
#
# ls=list(map(int,input().strip().split()))
# ls.append(int(input()))
# ls.sort()
# for i in ls:
#     print(i)

# ls=list(map(int,input().strip().split()))
# for i in ls[::-1]:
#     print(i,end=' ')

# a,b=map(int,input().strip().split())
# s=a*b
# while a%b:
#     a,b=b,a%b
#
# print(b,s//b)

# def s1(a,b,c,x):
#     x1=(-b+math.sqrt(x))/2*a
#     x2=(-b-math.sqrt(x))/2*a
# print('x1='+'%.2f'%x1,'x2='+'%.2f'%x2)
#
#
#
#
#
#
#
#
# a,b,c=map(int,input().strip().split())
# x=b**2-4*a*c
# if x>0:
# elif x==0:
# else :
#
# //简化输出
# print("x1={:.3f} x2={:.3f}".format(x1,x2))
#
# ls=[input().strip().split(),input().strip().split(),input().strip().split()]
# for i in range(3):
#     for j in range(3):
#        print(ls[j][i],end=' ')
#     print()

# str1=input().strip()
# for i in range(1,len(str1)+1):
#     print(str1[-i],end='')

# 高效
# str=input().strip()
# print(str[::-1])

#
# str1=input()
# str2=input()
# print(str1+str2)


# str=input()
# for i in  str:
#     if i =='a' or i =='e'  or i =='i'or i =='o' or i =='u':
#         print(i,end='')
#
#
#
# str=input()
# for i in str:
#     print(i,end=' ')
#
# str=float(input())
# for i in range(3):
#     for j in range(i+1):
#         print('%6.2f'%str,end=' ')
#     print()

# l=list(map(int,input().strip().split()))
# print('%0.3f'%max(l))
# print('%0.3f'%max(l))
#


# str=input()
# for i in str:
#     if i.islower():
#        print(chr(96+(ord(i)-95)%26),end='')
#     elif i.isupper():
#        print(chr(64 + (ord(i) - 63) % 26), end='')
#
#
# ls=[input().split(),input().split(),input().split()]
# ls.sort()
# for i in range(3):
#     print("".join(ls[i])) //去除输出时【】，也可将其替换为其他
#
# a=list(map(int,input().strip().split()))
# # l=[0,1,2,3,4,5,6,7,8,9]
# for i in a :
#     if i==min(a):
#         a[a.index(min(a))]=a[0]
#         a[0]=i
#     if i==max(a):
#         a[a.index(max(a))]=a[len(a)-1]
#         a[len(a)-1]=i
#
# for i in a:
#     print(i,end=' ')


# l=int(input())
# a=list(map(int,input().strip().split()))
# m=int(input())
# # x=[]
#
# for i in range(l):
#     x.append(((i+m)%(l)))
# print(x)
# print(len(x))

# l=int(input())
# a=list(map(int,input().strip().split()))
# m=int(input())
# for i in range(l-m,l):
#     print(a[i],end=' ')
# for i in range(l-m):
#     print(a[i],end=' ')

#
#
# n=int(input())
# ls=[i for i in range(1,n+1)] //整合写法
# x=0
# # for i in range(1,n+1):
# #     ls.append(i)
# while len(ls) >1:
#     x=(x+2)%(len(ls))
#     ls.pop(x)
# print(ls[0])

#
# year,month,day=map(int,input().strip().split())
# l1=[31,28,31,30,31,30,31,31,30,31,30,31]
#
# sum=day
# for i in range(month-1):
#     sum+=l1[i]
#
# if( year%4==0 and year%100!=0 or year%400==0) and month>2:
#     sum+=1
#
#
# print(sum)
#
#
# a,b=map(int,input().strip().split())
# print(a+b)

# x=150*2/15
# print('%.2f'%(float(15+25)*x/2))

# x=int(input())
# print(x,10*x)

# print((15*20-20*10)//10)

# a,b=map(int,input().strip().split())
# a,b=b,a
# print(a,b)
#
# a,b,c=map(int,input().strip().split())
# print((a+b)//c)


# if a==10 and b==1:
#    print('99.20')
# else : print('%.2f'%(a-b*0.8))

#
# len=int(input())
# l=list(map(int,input().strip().split()))
# print(l.index(max(l))+1)


# n=int(input())
# l=list(map(int,input().strip().split()))
# x=int(input())
# print(l.count(x))
# while True:
#     n=int(input())
#     l=list(map(int,input().strip().split()))
#     l.sort()
#     for i in l:
#      print(i,end=' ')
#     print()


# n=int(input())
# l=list(map(int,input().strip().split()))
# for i in range(n-1):
#     x=i
#     for j in range(i+1,n):
#         if l[x]>l[j]:
#             l[x],l[j]=l[j],l[x]
#
#
# for i in l:
#     print(i,end=' ')

# l=list(map(int,input().strip().split()))
# x=int(input())
# z=0
# for i in l:
#     if (i<=(x+30)):
#         z+=1
# print(z)


#
# x,y=map(int,input().strip().split())
# if x>y:
#     x,y=y,x
# z=0
# if x==1:
#     x+=1
#     z=z+1
#
# for i in range(x,y+1):
#     if isprime(i):
#         z+=1
#         print(i)
#
#
#
# print(z)
# from math import  sqrt
# def isprime(n):
#         if n<=1:
#             return False
#         for i in range(2,int(math.sqrt(n))+1):
#             if n % i ==0:
#                 return False
#
#         return True
#
#
# a,b=map(int,input().strip().split())
# z=0
# for j in range(a,b+1):
#
#     b=1
#     if j==1:
#         continue
#     for i in range(2,int(sqrt(j))+1):
#         if j % i ==0:
#             b=0
#     if  b==1:
#         z+=1



# print(z)
#
# l=list(map(int,input().strip().split()))
# print(max(l))




# def fs(n):
#     sum=1
#     for i in range(2,n):
#         if n % i==0:
#             sum+=i
#     return sum
# n=int(input())
# l=[]
# for i in range(n):
#     a,b=map(int,input().strip().split())
#
#     if fs(a)==b and fs(b)==a:
#         l.append("YES")
#     else :
#         l.append("NO")
#
# for i in l:
#     print(i)

# from math import  sqrt //这条语句非常重要
#
# def isprime(c):
#     if c<=1:
#         return False
#     for j in range(2,int(sqrt(c))+1):
#         if c % j ==0:
#             return False
#     return True
#
# l=[]
# # for i in range(2,32767):
# #     if isprime(i):
# #         l.append(i)
#
# n=int(input())
# z=0
# for x in range(2,n//2+1):
#     if isprime(x) and isprime(n-x):
#         z+=1
#
#
# print(z)




# while True:
#    n = int(input())
#    l=list(map(int,input().strip().split()))
#    l.sort()
#
#    for i in l:
#         print(i,end=' ')
#    print()


# n,m=map(int,input().strip().split())
# l=list(map(int,input().strip().split()))
# l.sort(reverse=True)
# for i in range(0,m):
#     print(l[i],end=' ')
# #
#
#
# n=int(input())
# while(n!=0):
#     l=list(map(int,input().strip().split()))
#     sum=0
#     l.sort()
#     for i in range(n//2+1):
#         sum+=l[i]//2+1
#     print(sum)
#     n=int(input())
#
#
# n=int(input())
# while n!=-1:
#     l=list(map(int,input().strip().split()))
#     m=int(input())
#     for i in range(m):
#         x=int(input())
#         try:
#            if l.index(x)>=0: //其实也可以用count来统计次数，次数大于1就可输出yes
#                print("YES")
#         except :
#             print("NO")
#     print()
#     n=int(input())
#


# n=int(input())
# for i in range(n):
#     x=int(input())
#     l=list(map(int,input().strip().split()))
#     l.sort()
#     print(l[1])
#


# n=int(input())
# for i in range(n):
#     n,m=map(int,input().strip().split())
#     z=0
#     for x in range(1,m):
#        z=0
#        c=n%x
#        for y in range(x+1,m+1):
#            if c==(n%y):
#                z=1
#                break
#        if z==1 :break
#     if z==1:
#         print("YES")
#     else :
#         print("NO")
#
# n=int(input())
# l=[]
# def funs(n,m):
#     for y in range(1, m + 1):
#         z = 0
#         for x in range(1, y):
#             if n % x == n % y:
#                 l.append("Yes")
#                 return
#     l.append("No")
#
# for i in range(n):
#     n,m=map(int,input().strip().split())
#     funs(n,m)
#
#
# for j in l:
#     print(j)


#
#

# def gcd(a,b):
#     while a%b:
#         a,b=a%b,a
#     return b
#
# n=int(input())
# l=list(map(int,input().strip().split()))
# l.sort()
# z=0
# while(l[0]!=1 or l[-1]!=1):
#     l[-1]=gcd(l[-1],l[-2])
#     z+=1
#     l.sort()
# print(z)

#
# str=input()
# dict1={'A0':[1189,841],'A0':[1189,841],'A0':[1189,841],'A0':[1189,841]}
# print(dict1[str][0])
# print(dict1[str][1])


#省赛题目 2684
# a=1189
# b=841
# n=int(input()[1])
# for i in range(n):
#     a,b=b,a//2
#     l=[a,b]
#
# print(a)
# print(b)
#
# def func(c):
#     a=0
#     while c!=0:
#         a+=c%10
#         c=c//10
#     return a
#
# n=int(input())
# m=int(input())
# l=[]
# x=[]
# dict1={}
# for i in range(n):
#     l.append(func(i+1))
# min=min(l)
# max=max(l)
#
# for i in range(min,max+1):
#     for j in range(n):
#         if i==l[j]:
#             x.append(j+1)
#
# print(x[m-1])
#

#与上一种相比，字典解题
# n=int(input())
#
# m=int(input())
#
# d={}
#
# for i in range(1,n+1):
#
#     s=list(map(int,str(i)))
#
#     d[i]=sum(s)
# l=list(d.items())
# print(l)
# l.sort(key=lambda x:x[1])
# # //x代表列表的每一个元素,以x[1]作为从小到大的排序
# print(l)
# print(l[m-1][0])







# def f():
#    n=eval(input())
#    m=eval(input())
#    max_n=sum([9 for i in range(len(str(n)))])
#    ar=[[]for i in range(max_n)]
#    ar_sum=[]
#    for i in range(1, n+1):
#        num_sum=sum(map(int, [j for j in str(i)]))
#        ar_sum.append(num_sum)
#        ar[num_sum-1].append(i)
#    sn=0
#    for i in ar:
#        for j in i:
#            sn+=1
#            if sn==m:
#                print(j)
#
# f()


#
# from math import pow
#
# str=input()
# str1=''
#
#
# for n in range(2**64):
#     for i in range(1,len(str)-1):
#         if (str[i]==str[i-1] and str[i]!=str[i+1] )or (str[i]==str[i+1] and str[i]!=str[i-1]):
#             if str[i]==str[i-1] and str[i]!=str[i+1]:
#                 str1+=str[i+1]
#                 i=i+1
#                 continue
#             else :
#                 str1+=str[i-1]
#                 i=i+2
#                 continue
#         else :
#             str1+=str[i]
#     if str1=='':
#         break
#
# if str1=='':
#     print("EMPTY")
#
# else :
#     print(str1)

# n=eval(input())
#
# z=0
# while z!=n:
#     length = eval(input())
#     d=[(input().strip().split()) for i in range(length)]
#     for i in range(length):
#                 for j in range(i+1):
#                     d[i][j]=int(d[i][j])
#     for i in range(1,length):
#                 for j in range(i+1):
#                     if j==0:
#                         d[i][j]=d[i-1][j]+d[i][j]
#                     elif j==i:
#                         d[i][j]=d[i-1][j-1]+d[i][j]
#                     else :
#                         d[i][j]=d[i][j]+max(d[i-1][j-1],d[i-1][j])
#     print(max(d[length-1]))
#     z+=1
#     del d
    # z+=1

#
# while True:
# 	try:
# 		m,n=map(int,input().strip().split())
# 		sux=1
# 		z=1
# 		if m-n<n:
# 			n=m-n
# 		for i in range(m-n+1,m+1):
# 			sux*=i
# 		for j in range(1,n+1):
# 			z*=j
# 		print(sux//z)
# 	except EOFError:
# 		break

#
# c=0
#
# def backtarcking(x,b):
# 	global c
# 	if x>=n-1:
# 		return
#
# 	for j in l[x:n-1]:
# 		b+=l[j]
# 		if b==m:
# 			c+=1
# 		if (b<m):
# 			backtarcking(x+ 1, b)
# 		b=b-l[j]
#
# n,m=map(int,input().strip().split())
# l=list(map(int,input().strip().split()))
# b=0
# x=0
# backtarcking(x,b)
# print(c)


# l=input()
# dict1={}
# x=[]
# for i in l:
#   dict1[i]=l.count(i)
# maxq=max(dict1.values())
# for i in dict1:
#   if dict1[i]==maxq:
#     x.append(i)
# print(max(x))
#
# print(maxq)

#
# n=eval(input())
# b=n
# i=0.0
# j=0.0
# while n!=0:
#   x=int(input())
#   if x>=60:
#     i+=1
#   if x>=85:
#     j+=1
#   n-=1
# print(int(round((i/b)*100,0)),'%')
# print(int(round((j/b)*100,0)),'%')
# z=0
# for i in range(1,2021):
#   s=str(i)
#   z+=s.count("2")
# print(z)

# l=[2021 for i in range(10)]
# z=1
# sum=0
# i=1
# while True:
#   for j in str(i):
#     l[int(j)]-=1
#   if min(l)<=0:
#     sum=i
#     break
#   i+=1
# print(sum)

# n=int(input())
# l=[input().strip().split() for i in range(n)]
# for i in range(0,n):
#     for j in range(i+1):
#         l[i][j]=int(l[i][j])
# for i in range(1,n):
#     for j in range(i+1):
#         if j==0:
#             l[i][j]+=l[i-1][j]
#
#         elif i==j:
#             l[i][j]+=l[i-1][j-1]
#
#         else :
#             l[i][j]+=max(l[i-1][j-1],l[i-1][j])
#
# if h&1:
#     print(l[-1][n//2])
# else :
#     print(max(l[-1][h//2-1],l[-1][h//2]))
#
#
#

# n=50
# l=[input().strip().split() for i in range(50)]
# sum=0.0
# for i in l:
#         if i[0]=='半' :
#             sum+=float(i[0])

# print(float(256*1024*1024*8/32))


#
#
#
# n=int(input())
#
# l=[]
# for i in range(n):
#   l.append(int(input()))
#
# print(max(l))
# print(min(l))
# print("{:.2f}".format(sum(l)/n))


# n=int(input())
# sum=0
# for i in range(1,n+1):
#     if str(i).count('2') or str(i).count('1') or str(i).count('0') or str(i).count('9'):
#         sum+=i
# print(sum)
# #
# n=2021041820210418
# l=[]
# sum=0
# for i in range(1,int(pow(n,0.5))+1):
#     if n%i==0:
#         l.append(i)
#         if n/i!=i:
#             l.append(n/i)
# for i in l:
#     for j in l:
#         for k in l:
#             if i*j*k==n:
#                 sum+=1
#
# print(sum)
# l=[]
# def funx(n):
#
#     for i in range(2,int(pow(n,0.5))+1):
#         if n%i==0:
#             return 0
#     return 1
# for i in range(2,19000):
#     if funx(i):
#         l.append(i)
# k=10
#
#
# for i in l:
# 97 90 0 0 0
# 92 85 96 0 0
# 0 0 0 0 93
# 0 0 0 80 86
# 89 83 97 0 0
# 82 86 0 0 0
# 0 0 0 87 90
# 0 97 96 0 0



#
# l=[list(map(int,input().strip().split)) for i in range(20)]
#


# l=list(map(str,input().strip().split()))
# str1=""
# for i in range(len(l)):
#     l[i]=str(l[i]).capitalize()
# for i in l:
#
#     for j in range(len(i)-1):
#         str1+=i[j]
#         if i[j].isalpha():
#             if i[j+1].isdigit():
#                 str1+='_'
#         if i[j].isdigit():
#             if i[j+1].isalpha():
#                 str1+="_"
#     str1+=i[len(i)-1]
#     str1+=' '
# str1=str1.rstrip()
# print(str1)

# def funx(s):
#     if len(s)<=1:
#         return [s]
#     str_list=[]
#     for i in range(len(s)):            //将传入的s进行全排列
#         for j in funx(s[0:i]+s[i+1:]):
#             str_list.append(s[i]+j)
#     return str_list
#
#
# str1=input()
# n=int(input())
# z=0
# for i in range(n):
#     s=input()
#     set1=set(funx(s))
#     for j in set1:
#         z+=str1.count(str(j))
#
# print(z)

#下列方法对母串进行切片对照，字串中字母种类和数目是否相等
#
# str1=input()
# n=int(input())
# dict1={}
# z=0
#
# def funx(s):
#     ls=list(s)
#     ls.sort()
#     s=''
#     for i in ls:
#         s+=i
#     return s
#
# for i in range(n):
#     s=input()
#     s=funx(s)
#     if s in dict1:
#         dict1[s]+=1
#     else :
#         dict1[s]=1
#
# for i in range(len(str1)-7):
#     s=funx(str1[i:i+8])
#     if s in dict1:
#         z+=dict1[s]
# print(z)




# ls=list(map(str,input().strip().split('/')))
# ans=[]
# mon=[0,31,28,31,30,31,30,31,31,30,31,30,31]
# def run(x):
#     x=int(x)
#     if x % 4 == 0 and x % 100: return True
#     if x % 100 == 0 and x % 400 == 0: return True
#     return False
#
# def func(x,y,z):
#     year=''
#     if int(x)>=60:
#         year='19'+x
#     else :
#         year='20'+x
#     if run(year):
#         mon[2]+=1
#         if int(z)<=mon[y]:
#             ans.append((int(year),int(y),int(z)))
#         mon[2]-=1
#     else:
#         if z<=mon[y]:
#             ans.append((int(year),int(y),int(z)))
#
# if 0<=int(ls[1])<=12 and 0<=int(ls[2])<=31:
#     func(ls[0],ls[1],ls[2])
# if 0<=int(ls[0])<=12 and 0<=int(ls[1])<=31:
#     func(ls[2],ls[0],ls[1])
# if 0<=int(ls[1])<=12 and 0<=int(ls[0])<=31:
#     func(ls[2],ls[1],ls[0])
#
# ans.sort()
# ans=list(dict.fromkeys(ans))
# for i in ans:
#     print("{:04}-{:02}-{:02}".format(i[0],i[1],i[2]))



#七段管
# w = {'a':['f', 'b'], 'b':['a', 'c', 'g'], 'c':['b', 'd', 'g'],
#         'd':['e', 'c'], 'e':['d', 'f', 'g'], 'f':['a', 'e', 'g'],
#         'g':['b', 'c', 'e', 'f']}
# s ='abcdefg'
# s1=[]
# count=0
#
# for i in range(1,8):
#     for x in itertools.combinations(s,i):
#         s1.append("".join(x))
#
# for i in s1:
#     for j in itertools.permutations(i):
#         for k in range(len(j)-1):
#             if j[k+1] not in w[j[k]]:
#                 break
#         else: #'''for循环语句的后面紧接着else子句，在循环正常结束的时候（非return或者break等提前退出的情况下），else子句的逻辑就会被执行'''
#             count+=1
#             break
# print(count)
# def C(a,b):
#     res=1
#     for i in range(a):
#         res*=b/a
#         if res>target:
#             return res
#         b-=1
#         a-=1
#     return res
#
# def search(k):
#     low=2*k
#     high=target
#     if high<=low and C(k,low) !=target:
#         return False
#     while low<=high:
#         mid=low+(high-low)//2
#         val=C(k,mid)
#         if val>target:
#             high=mid-1
#         elif val<target:
#             mid=mid+1
#         else:
#             print(int(mid*(mid+1)/2)+k+1)
#             return True
#     return False
#
#
#
#
#
#
#
#
# target=int(input())
# for i in range(16,-1,-1):
#     if search(i):
#         break

# def funx(a,b):
#
#     while a%b:
#         a,b=b,a%b
#     return b
# count=0
# for i in range(1,2021):
#     for j in range(1,2021):
#         if funx(i,j)==1:          #求最大公约数也可用math中的函数gcd(i,j)来求解
#             count+=1
#
# print(count)

#
# n,m=map(int,input().strip().split())
# l=[input().strip().split() for i in range(n)]
# w=[[-100]*(m+3) for i in range(n+3)]
# for i in range(n):
#     for j in range(m):
#         l[i][j]=int(l[i][j])
# # for i in range(n-1,-1,-1):
# #     for j in range(m-1,-1,-1):
# #         print(l[i][j])
#
# for i in range(3,n+3):
#     for j in range(3,m+3):
#         if i==3 and j==3:
#             w[i][j]=l[i-3][j-3]
#         else :
#             w[i][j]=l[i-3][j-3]+max(w[i][j-1],w[i][j-2],w[i][j-3],w[i-1][j],w[i-1][j-1],w[i-1][j-2],w[i-2][j],w[i-2][j-1],w[i-3][j])
#
# print(w[-1][-1])
# a,b,c,d=1,1,1,0
# for i in range(3,20190324):
#     d=(a+b+c)%10000
#     a,b,c=b,c,d
# print(a,b,c,d)
# n=int(input())
# l=[]
# sum=0
# z=0
# w=[]
# for i in range(n):
#     a=[int(x) for x in input().split(" ")]
#     w.append(a[0]+a[1]+a[2])
#     sum+=a[0]+a[1]
#     l.append(a)
# w.sort()
# for i in range(n-1):
#     z+=w[i]
#     sum+=z
# print(sum)

# lst=[float("inf")]*(2021+1)#将lst[]对象初始默认无穷大，在后面min里防止j变量第一轮没有值的问题。
#
#
# lst[1]=0
# for i in range(1,2022):
#     for j in range(i+1,i+22):
#         if j>2021:
#             break
#         lst[j]=min(lst[j],lst[i]+(i*j//(math.gcd(i,j))))
# print(lst[-1])
#
# z=0
# for i in range(1,673):
#     if str(i).count('2')!=0 or str(i).count('4')!=0:
#         continue
#     for j in range(i+1,(2019-i)//2+1):
#         if str(j).count('2') != 0 or str(j).count('4') != 0:
#             continue
#         k=2019-i-j
#         if k>j:
#             if str(k).count('2') ==0 and str(k).count('4')==0:
#                 z+=1
#
# print(z)
# sum=0
# for i in range(0,64):
#     sum+=2**i
#
# print(sum)

# x=6036
# i=2
# z=1
# while True:
#     if x*i>10000000 and ((x*i)//100)%10==6 and ((x*i)//1000)%10==0 and (x*i)%100<=31:
#         print(x*i)
#         z+=1
#     if z==8:
#         break
#     i=i+1





# str1=input() #该方法容易超时
# x=len(str1)
# sum=x
# for i in range(1,x):
#     for j in range(0,x-i):
#         z=0
#         s=str1[j:j+i+1]
#         for k in s:
#             if s.count(k)==1:
#                 z+=1
#         sum+=z
# print(sum)


# li = [-1 for i in range(26)]
# to = 0
# index = 0
# n = input()
# for i in range(len(n)):
#     c = 0
#     index = ord(n[i]) - ord('a')
#     while (i+c+1<len(n)):
#         if (n[i+c+1] == n[i]):
#             break
#         c = c + 1
#     to = to + (i-li[index])*(c+1)
#     li[index] = i
# print(to)

# def fun1(c):
#     for b in range(2,c):
#         if c%b==0:
#             return 0
#     return 1
# k=1
# z = 3
# while True:
#
#     if fun1(z):
#         k=k+1
#     if k==2019:
#         print(z)
#         break
#     z+=1


# n=int(input())
# w=[]
# l=list(map(int,input().strip().split()))
# l.sort()
# for i in range(n-1):
#     w.append(l[i+1]-l[i])
# d=min(w)
# if d==0:
#     print(n)
# else:
#     c=(max(l)-min(l))//d+1
#     print(c)
# #


#
# n,m,k,t=map(int,input().strip().split())
# l=list(map(int,input().strip().split())) #i中作物种植时间
# w1=list(map(int,input().strip().split())) #已有种子类型
# dic={}
# dic1={}
# # set1=set()
# # set2=set(w1)
# sum=0
# w2=[input().strip().split() for i in range(k)]  #杂交方案
# for i in range(k):
#     for j in range(3):
#         w2[i][j]=int(w2[i][j])
# for i in range(k):
#     dic[w2[i][2]]=w2[i][0:2]
#     dic1[w2[i][2]]=max(l[w2[i][0]-1],l[w2[i][1]-1])
# print(dic1)
# def funx(x):
#     if w1.count(x)>0:
#         return 0
#     w1.append(x)
#     # set1.add(x)
#     return dic1[x]+max(funx(dic[x][0]),funx(dic[x][1]))
#
# b=funx(t)
# # set1=set1-set2
# # z=0
# # for i in set1:
# #     z+=dic1[i]
# print(b)
# #print(z)
#

#
#
# import os
# import sys
#
# # 请在此输入您的代码
# """
# 在纸上画一下它们的父子关系图，画成一个二叉树的形式，要得到的种子作为根节点，其他的作为子节点
# 这样可以形成明显的层次关系，在每一层找到最大的时间，然后把这些最大的时间相加就能得到最终的最短时间
# """
# N, M, K, T = map(int, input().split())
# growtime = list(map(int, input().split()))
# growtime.insert(0, 0)  # 让编号和下标对应
# existseed = list(map(int, input().split()))
# relation = [list(map(int, input().split())) for i in range(K)]
#
# """定义一个列表用于存放种子的双亲,以及双亲培育出目标种子的时间"""
# parent = [[] for i in range(N + 1)]
# for elem in relation:
#     """能生成种子t的双亲可能不知2个，也可能4个，8个...."""
#     a = [elem[0],elem[1],max(growtime[elem[0]],growtime[elem[1]])]
#     parent[elem[2]].append(a)
#
# """定义一个存放得到各个种子最短时间的数组"""
# dp = [float('inf') for i in range(N + 1)]  # 编号和下标对应
#
# for i in existseed:  # 已经拥有的种子生成时间是0
#     dp[i] = 0
#
#
# def dns(t):  # t:种子编号是t
#     """计算培育出t号种子的最短时间"""
#
#     if dp[t] != float('inf'):  # 如果t号种子不等于无穷大，就已经求出t号种子的最短时间了
#         return dp[t]
#
#     """如果还没有求出来，就是t号种子的双亲培育t号的时间+培育t号双亲的时间"""
#     for item in parent[t]:
#         dp[t] = min(dp[t],max(dns(item[0]),dns(item[1]))+item[2])
#
#     return dp[t]
#
#
# print(dns(T))

#
# for i in range(1,1000000007):
#     if i*2021%1000000007== 999999999:
#         print(i)
#         break
#
#
# n=int(input())
# if n==4:
#     print('bbaa')
# if n==100:
#     print('jihgfeeddccbbaa')



# n=int(input())
# l=list(map(int,input().strip().split()))
# l.sort()
# ls=[]
# set1=set([l[0]])
# for i in l[1:]:
#     for j in list(set1):
#         set1.add(i)
#         set1.add(i+j)
#         set1.add(abs(i-j))
#
# if 0 in set1:
#     print(len(set1)-1)
# else:
#     print(len(set1))

#
# l
# str1='''5650 4542 3554 473 946 4114 3871 9073 90 4329
# 2758 7949 6113 5659 5245 7432 3051 4434 6704 3594
# 9937 1173 6866 3397 4759 7557 3070 2287 1453 9899
# 1486 5722 3135 1170 4014 5510 5120 729 2880 9019
# 2049 698 4582 4346 4427 646 9742 7340 1230 7683
# 5693 7015 6887 7381 4172 4341 2909 2027 7355 5649
# 6701 6645 1671 5978 2704 9926 295 3125 3878 6785
# 2066 4247 4800 1578 6652 4616 1113 6205 3264 2915
# 3966 5291 2904 1285 2193 1428 2265 8730 9436 7074
# 689 5510 8243 6114 337 4096 8199 7313 3685 211 '''.replace('\n','')
# #str1='5650 4542 3554 473 946 4114 3871 9073 90 4329 2758 7949 6113 5659 5245 7432 3051 4434 6704 3594 9937 1173 6866 3397 4759 7557 3070 2287 1453 9899 1486 5722 3135 1170 4014 5510 5120 729 2880 9019 2049 698 4582 4346 4427 646 9742 7340 1230 7683 5693 7015 6887 7381 4172 4341 2909 2027 7355 5649 6701 6645 1671 5978 2704 9926 295 3125 3878 6785 2066 4247 4800 1578 6652 4616 1113 6205 3264 2915 3966 5291 2904 1285 2193 1428 2265 8730 9436 7074 689 5510 8243 6114 337 4096 8199 7313 3685 211 '
# s1=str1.split()
# count=0
# j=1
# for i in s1:
#     j*=int(i)
# for k in str(j)[::-1]:
#     if k=='0':
#         count+=1
#     else:
#         break
# print(count)
#

# 请在此输入您的代码
# count=0#方案数
# def queen(A,n=0):#现在行（从行开始，一行一行放）
#   global count#全局变量
#   if n==len(A):
#     count+=1
#     return
#   for col in range(len(A)):#现在列（遍历该行的每一列）
#     A[n]=col#存放该列为当前答案
#     flag=1
#     for row in range(n):#遍历之前行
#       if A[row]==col or (abs(col-A[row])==n-row and n-row<3):#不满足，撤回
#         flag=0
#         break
#     if flag==1:#满足
#       queen(A,n+1)#开始下一行
# queen([0]*int(input()))
# print(count)
# import itertools
#
# n=int(input())
# l=list(map(int,input().strip().split()))
# sx=0
# for i in itertools.combinations(l,2):
#     sx+=i[0]*i[1]
#
# print(sx)


# n=int(input()) #会超时，下面有个更好的解法
# l=list(map(int,input().strip().split()))
# sum=0
# for i in range(n-1):
#     for j in range(i+1,n):
#         sum+=l[i]*l[j]
#
# print(sum)

# n=int(input())
# l=list(map(int,input().strip().split()))
# s=0
# sx=sum(l)
# for i in range(n):
#     sx-=l[i]
#     s+=l[i]*sx
# print(s)
#


# l=list('WHERETHEREISAWILLTHEREISAWAY')
# str=''
# l.sort()
# for i in l:
#     str+=i
# print(str)
#
# import itertools
# l=input()
# n=int(input())
# str=''
# for i in min(itertools.combinations(l,len(l)-n)):
#     str+=i
#
# print(str)

# n=int(input())
# sum=n
# while n//3>0:
#     sum+=n//3
#     n=n%3+n//3
#
#
# print(sum)

# n=input()
# l=list(map(int,input().strip().split()))
# l.sort()
# for i in l:
#     print(i,end=' ')
# print()
# for i in l[::-1]:
#     print(i,end=' ')
#
# sum=0
# for i in range(1,2020):
#     if str(i).count('2')>0 or str(i).count('0')>0 or str(i).count('1')>0 or str(i).count('9')>0 :
#         sum+=i**2
# print(sum)
# i=1
# x=1
# while True:
#     flag=1
#     i+=2
#     x=2019*i
#     for j in range(len(str(x))):
#         if int(str(x)[j]) %2==0:
#             flag=0
#             break
#     if flag==1:
#         print(x)
#         break
#
# def funx(x):
#     l=len(str(x))
#     for i in range(l):
#         if str(x)[i]!=str(x)[l-1]:
#             return False
#     return True
#
# def func(x):
#
#

# ls=[[x,y] for x in range(20) for y in range(21)]
# set1=set()
# set2=set()
# for x1,y1 in ls:
#     for x2,y2 in ls:
#         if x1==x2:
#             set1.add((x1,x2))
#             continue
#         else:
#             k=(y2-y1)/(x2-x1)
#             b=(y2*x1-y1*x2)/(x1-x2)
#             set2.add((k,b))
# print(len(set1)+len(set2))

# n,k=map(int,input().strip().split())
# l=[input().strip().split() for i in range(n)]
# l1=[0,0]*n
# for i in range(n):
#     l[i][0],l[i][1]=int(l[i][0]),int(l[i][1])
#     l1[i]=int(l[i][0])*int(l[i][1])
# c=1
# for i in range(int(math.sqrt(sum(l1)//k))+1,0,-1):
#     z=0
#     for j in l1:
#         z+=j//(i*i)
#     if z>=k:
#         c=i
#         break
# print(c)


# 分巧克力 用二分法，依次从1~100000试哪个值最大且合适

# h = []
# w = []
# def check(d):   #  一次只是检查一种边长的切法
#     res = 0
#     for i in range(len(w)):  # i 从0到d-1 它会检测所有h、w集合中的值
#         res += (h[i]//d) * (w[i]//d)    # 计算所有巧克力的长宽 按这个边长切结果能切处几个
#     if res >= k:
#         return True
#     return False
#
#
# n, k = map(int, input().split())
# for i in range(n):
#     a, b = map(int, input().split())
#     h.append(a)
#     w.append(b)
# # 二分法依次试 用找合适或者后继的二分法
# L, R = 1, 1000000
# while L < R:
#     mid = (L+R)//2
#     if check(mid):
#         L = mid+1
#     else:
#         R = mid
# # 只要符合， L就会+1 所以停止的时候 L大于刚刚好的时候
# print(L-1)
#

#
# l=[0,31,28,31,30,31,30,31,31,30,31,30,31]
# sx=0
# w=['012','123','234','345','456','567','678','789']
# for i in range(1,13):
#     for j in range(1,l[i]+1):
#         print(i,j)
#         str1=''
#         if i<10:
#             if j <10:
#                 str1='20220'+str(i)+'0'+str(j)
#             else:
#                 str1= '20220' + str(i) + str(j)
#         else :
#             if j<10:
#                 str1= '2022' + str(i) +'0'+ str(j)
#             else:
#                 str1= '2022' + str(i) + '0'+str(j)
#         for k in w:
#             if str1.find(k)!=-1:
#                 sx+=1
#                 break
#
# print(sx)

#
# x=0
# y=pow(2,19)
# for i in range(20):
#     x+=2**i
# print(str(x)+'/'+str(y))
#



#
# sum=0
# for i  in range(20):
#   sum+=2**i
# print("{}/{}".format(sum,2**19))
#
#

#
#
# n,m=map(int,input().strip().split())
# l=[[4 for i in range(m+2)] for j in range(n+2)]
# w=[[9 for i in range(m)] for j in range(n)]
# for i in range(1,n+1):
#     str2=input().replace(' ','')
#     for j in range(1,m+1):
#         l[i][j]=int(str2[j-1])
#
# def funx(i,j):
#     if l[i][j]==1:
#         return
#     str1=str(l[i][j-1])+str(l[i-1][j-1])+str(l[i+1][j-1])+str(l[i][j+1])+str(l[i-1][j+1])+str(l[i+1][j+1])+str(l[i-1][j])+str(l[i+1][j])
#     w[i-1][j-1]=str1.count('1')
#     return
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         funx(i,j)
#
# for i in w:
#     for j in i:
#         print(j,end=' ')
#     print()

# import datetime
# start=datetime.date(1901,1,1)
# end=datetime.date(2000,12,31)
# print((end-start)//7)
#



# n=int(input())
# l=list(map(int,input().strip().split()))



# n=int(input())
# l=list(map(int,input().strip().split()))
# l=list(set(l))
# l.sort()
#
# print(len(l))
# for i in l:
#     print(i,end=' ')
#


# n,k,m=map(int,input().strip().split()) 错误解法
# l=[int(i+1) for i in range(n)]
# i = k % n
# j = i + (m - 1) % n
# while n!=1:
#     print(j)
#     l.remove(j)
#     i = (j+1) % n
#     j = i + (m - 1) % n
#     n = n - 1
#
# print(l[0])

#正确解法
# n,k,m=map(int,input().strip().split())
# a=list(range(1,n+1))
# i=k-1
# while len(a)>0:
#     i=(i+m-1)%len(a)
#     print(a.pop(i))


# n=int(input())
# l=[[int(x) for x in input().strip().split()] for i in range(n)]
#
# for i in range(1,n):
#     for j in range(i+1):
#         if j==0 or j==i:
#             if j==0:
#                     l[i][j]+=l[i-1][j]
#             else:
#                 l[i][j]+=l[i-1][j-1]
#         else :
#             l[i][j]+=max(l[i-1][j-1],l[i-1][j])
#
# print(max(l[-1]))
# l=[0 for i in range(10**4)]
# x=1
# c=x
# k=int(input())
# while x<=k:
#     for i in range(1,c+1):
#         l[x]=l[x-1]+c
#         x+=1
#     c+=1
#
# print(l[k])
#

# m=int(input())
# dict1=dict()
# for i in range(m):
#     n=int(input())
#     if n in dict1:
#         dict1[n]+=1
#     else:
#         dict1[n]=1
#
# for i in dict.fromkeys(sorted(dict1.keys())):
#     print(i,dict1[i])




# import itertools
# n=int(input())
# l=input().strip().split()
# lst=list()
# for i in itertools.permutations(l):
#     lst.append(''.join(i))
# print(max(lst))

# import itertools
# n=int(input())
# m=int(input())
# l=input().strip().split()
# c=str(''.join(l))
# j=0
# for i in itertools.permutations(l):
#     if j==3:
#         print(' '.join(i))
#         break
#     j=j+1


# lst.sort()
# x=m+lst.index(c)
# str2=str(lst[x])
# print(' '.join(str2))
#
# n=int(input())
# m=int(input())
# nums=list(map(int,input().strip().split()))
# def find_next(nums):
#     for i in range(n-1,0,-1):
#         if nums[i]>nums[i-1]:
#             for j in range(n-1,i-1,-1):
#                 if nums[j]>nums[i-1]:
#                     nums[j],nums[i-1]=nums[i-1],nums[j]
#                     return nums[:i]+nums[:i-1:-1]
# for i in range(m):
#     nums=find_next(nums)
# print("".join([str(i) for i in nums]))
#


# while True:
#     try:
#         n,k = map(int,input().split())
#         s = list(input())   #此时的列表数据都是str类型
#         dp = [[0 for i in range(k+1)]for j in range(n+1)]    #动规的数组
#         dp[1][0] = int(s[0])
#         for i in range(2, n+1):
#             dp[i][0] = int(s[i-1])+int(dp[i-1][0])*10    #往动规数组放的时候要转化成int类型，输入数组的第一列
#         for y in range(1,k+1):     #y个乘号
#             for x in range(1,n+1):   #x位数
#                 if x>y:
#                     for z in range(1,x):  #乘号，动态地在数字之间跑
#                         dp[x][y] = max(dp[x][y], dp[z][y-1]*(dp[x][0]-dp[z][0]*10**(x-z)))
#         print(dp[n][k])
#     except:
#         break

#
# n=int(input())
# dict1=dict()
# def takeSecond(elem):
#     return elem[1]
# l=[list(map(int,input().strip().split())) for i in range(n)]
# lst=set()
# # print(l)
# for i in range(len(l)):
#     lst.add(sum(l[i]))
#     if sum(l[i]) in dict1:
#         dict1[sum(l[i])].append([i,l[i][0]])
#     else:
#         dict1[sum(l[i])]=[[i,l[i][0]]]
# # print(dict1)
# lst=list(lst)
# lst.sort(reverse=True)
# z=0
# for i in range(len(lst)):
#     dict1[lst[i]].sort(key=takeSecond,reverse=True)
#     if z==5:
#         break
#     for j in dict1[lst[i]]:
#         if z==5:
#             break
#         print(j[0]+1,lst[i])
#         z+=1
#


#高效解法
# import os
# import sys
#
# # 请在此输入您的代码
# n = int(input())
# l = []
# # 先总分高到低，再语文高到低，最后学号最小
# # 优先级最高的最后排序
# for i in range(1,n+1):
#     x = list(map(int,input().split()))
#     l.append([i,sum(x),x[0]]) #学号，总分，语文
# # print(l)
# l.sort(key=lambda x:x[0])#学号
# l.sort(key=lambda x:x[2],reverse=True)#语文
# l.sort(key=lambda x:x[1],reverse=True)#总分
#
# for i in range(5):
#     print(l[i][0],l[i][1])
#
#


# def takes(ls,i):          方法有缺陷
#     ls[i]=ls[i]+ls[i+1]
#     for j in range(i+1,len(ls)-1):
#         ls[j]=ls[j+1]
#     del ls[len(ls)-1]
#     # print(ls)
# l,n,m=map(int,input().strip().split())
# z=0
# lst=[0 for i in range(n+1)]
# x=0
# while z<5:
#     b=int(input())
#     x=b-x
#     lst[z]=x
#     z=z+1
#     x=b
# lst[n]=l-sum(lst)
# lsz=list(lst)
# lsz.sort()
# for i in range(m):
#     j=lst.index(lsz[i])
#     takes(lst,j)
# print(min(lst))


# def check(d):
#     num=0
#     pos=0
#     for i in range(n):
#         if a[i]-pos<d:
#             num+=1
#         else:
#             pos=a[i]
#     if num<=m:
#         return True
#     else:
#         return False
#
# l,n,m=map(int,input().strip().split())
# left=0
# right=l
# a=[]
# ans=0
# for i in range(n):
#     a.append(int(input()))
#
# while left<=right:
#     mid=(left+right)//2
#     if check(mid):
#         left=mid+1
#         ans=mid
#     else:
#         right=mid-1
# print(ans)
#

# s=input()
# print(len(s.replace(' ','')))



# s=input()
# l=s.strip().split('-')
# s1=''
# sum=0
# for i in range(len(l)-1):
#     s1+=l[i]
# for i in range(len(s1)):
#     sum+=(i+1)*int(s1[i])
#
# if sum%11==10:
#     if 'X'==l[3]:
#         print('Right')
#     else:
#         print(s[0:len(s)-1]+str(sum%11))
# else:
#     if sum%11==int(l[3]):
#         print('Right')
#     else:
#         print()
#

# def funx(n):
#     if n==0 or n==1:
#         return 1
#     else :
#         sum=0
#         for i in range(n//2+1):
#             sum+=funx(i)
#         return sum
#
#
# n=int(input())
# print(funx(n))
#

#
# s=input()
# flag=1
# j=0
# str1=''
# if int(s)<0:
#     flag=-1
#     s=str(abs(int(s)))
# for i in range(len(s)-1,0,-1):
#     if s[i]!=0:
#         j=i
#         break
# for i in range(j,-1,-1):
#     str1+=s[i]
# print(flag*int(str1))
#
# def isPrime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0:
#             return False
#     return True
#
#
# s=input()
# dict1={}
# for i in s:
#     if i in dict1:
#         dict1[i]+=1
#     else:
#         dict1[i]=1
#
# if isPrime(max(dict1.values())-min(dict1.values())):
#     print("Lucky Word")
#     print(max(dict1.values())-min(dict1.values()))
# else:
#     print("No Answer")
#     print(0)

#
#
# n=int(input())
# l=[input() for i in range(n)]
#


# n=int(input())
# l1=['jia',"yi","bing",'ding','wu','ji','geng','xin','ren','gui']
# l2=['zi','chou','yin','mao','chen','si','wu','wei','shen','you','xu','hai']
# n=n-4
# x=n%10
# y=n%12
# print(l1[x]+l2[y])
#

# n=int(input())
# s=set()
# d=dict()           一半正确率，错误解法
# while n>0:
#     x,y=map(int,input().strip().split())
#     if x in d:
#         if y not in d[x]:
#             d[x].append(y)
#     else:
#         d[x]=[y]
#     n-=1
# sum=0
# for i in d.values():
#     sum+=len(i)+1
# print(sum)
#
# def isintersect(k1,b1,k2,b2):
#     if k1!=k2:
#         return True
#     else:
#         return False
#
#
# def getpoint(k1,b1,k2,b2):
#     x=(b2-b1)/(k1-k2)
#     y=(k2*b1-k1*b2)/(k2-k1)
#     return (x,y)
#
# def isin(x,y,k,b):
#     if y==k*x+b:
#         return True
#     else:
#         return False
#
# N=int(input())
# li=[list(map(int,input().strip().split())) for i in range(N)]
# exist=[]
# res=1
# for item in li:
#     points=[]
#     if item in exist:
#         continue
#     for e in exist:
#         if isintersect(item[0],item[1],e[0],e[1]):
#             new=getpoint(item[0],item[1],e[0],e[1])
#             if new not in points:
#                 points.append(new)
#     res+=len(points)+1
#     exist.append(item)
# print(res)
#
#
# import itertools           错误解法
# def isPrime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0:
#             return False
#     return True
# l=['2','3','5','7']
# l.sort(reverse=True)
# l1=[]
# for i in range(1,len(l)+1):
#     for j in itertools.permutations(l,i):
#         str1=''.join(j)
#         if isPrime(int(str1)):
#             c1=0
#             for i in range(0,len(str1)):
#                 flag=0
#                 for j in range(0,len(str1)-i):
#                     x=int(str1[j:j+i+1])
#                     if isPrime(x)!=True:
#                         flag=1
#                         break
#                 if flag==1:
#                     c1=1
#                     break
#             if c1==1:
#                 break
#             l1.append(int(str1))
#
# print(max(l1))
#
# sma_zi=['2','3','5','7']
#
# def devison(num):
#     for i in num:
#         if i not in sma_zi:
#             return 0
#     n=int(num)
#     for i in range(2,int(n**0.5)):
#         if n%i==0:
#             return 0
#     return 1
# def child(num):
#     children=[]
#     for i in range(0,len(num)-1):
#         for j in range(i+1,len(num)):
#             children.append(num[i:j+1])
#     for ch in children:
#         div=devison(ch)
#         if div==0:
#             return 0
#         return 1
# maxnum=0
# for num in range(2,99999):
#     num=str(num)
#     d1=devison(num)
#     d2=child(num)
#     if d1 and d2:
#         maxnum=int(num)
# print(maxnum)
#
#
# sma_zi = ['2', '3', '5', '7']  # 10以内的质数
# def devision(num):
#     # 判断每一个数字
#     for i in num:
#         if i not in sma_zi:
#             return 0
#     # 判断整个数字
#     n = int(num)
#     for i in range(2, int(n ** 0.5)):
#         if n % i == 0:
#             return 0
#     return 1
#
# def child(num):  # 取出num中的子串
#     children = []
#     for i in range(0, len(num) - 1):
#         for j in range(i + 1, len(num)):
#             children.append(num[i:j + 1])
#     for ch in children:
#         div = devision(ch)
#         if div == 0:
#             return 0
#     return 1
#
# for num in range(2, 99999):
#     num = str(num)
#     d1 = devision(num)
#     d2 = child(num)
#     if d1 ==1 and int(d2) == 1:
#         maxnum = int(num)
# print(maxnum)

# x=0
# for i in range(0,20):
#     x+=2**i
#
# print('{}/{}'.format(x,2**19))


#
# count=0
# for i in range(1,1200001):
#     if 1200000%i==0:
#         count+=1
# print(count)
#

# n,m=map(int,input().strip().split())
# l=[i+1 for i in range(n)]
#
# def fdown(l,i):
#     x=l[0:i]
#     x.sort()
#     l[0:i]=x[::-1]
# def fup(l,i):
#     x=l[i-1:n]
#     x.sort()
#     l[i-1:n]=x
#
#
#
# while m>0:
#     x,y=map(int,input().strip().split())
#     if x==0:
#         fdown(l,y)
#     else:
#         fup(l,y)
#     m-=1
# for i in l:
#     print(i,end=' ')

#
# from math import gcd
# from time import time
# n=21
# m=1<<n
#
# dp=[[0 for j in range(n)] for i in range(m)]
# load=[[False for a in range(n)] for b in range(n)]
# start_time=time()
# for a in range(1,n+1):
#     for b in range(1,n+1):
#         if gcd(a,b)==1:
#             load[a-1][b-1]=True
# dp[1][0]=1
# for a in range(1,m):
#     for b in range(1,m):
#         if a>>b&1:
#             for k in range(n):
#                 if a-(a<<b)>>k &a and load[k][b]:
#                     dp[a][b]+=dp[a-(1<<b)][k]
# end_time=time()
# print("耗费时间",end_time-start_time)
# print(sum(dp[m-1]-dp[m-1][0]))
#






#
# def funx(x,y,z,l):
#     for i in y:
#         for j in z:
#             if i+j in x:
#                 if (sum(y)-i)==(sum(z)-j):
#                     l.append(4)
#                 else :
#                     l.append(6)
#                     return
# n=int(input())
# for x in range(n):
#     a1,b1,a2,b2,a3,b3=map(int,input().strip().split())
#     l=[8]
#     l1=[a1,b1]
#     l2=[a2,b2]
#     l3=[a3,b3]
#     funx(l1,l2,l3,l)
#     funx(l2,l1,l3,l)
#     funx(l3,l1,l2,l)
#     print(min(l))
#
#






#
#
#
# def check4(x1,x2,x3,a):
#     if x1==x2+x3 and a[2]+a[3]-x2==a[4]+a[5]-x3:
#         return True
#     if x2==x1+x3 and a[0]+a[1]-x1==a[4]+a[5]-x3:
#         return True
#     if x3==x2+x1 and a[0]+a[1]-x1==a[2]+a[3]-x2:
#         return True
#     return False
# def check6(x1,x2,x3):
#     if x1==x2+x3 or x2==x1+x3 or x3==x2+x1:
#         return True
#     return False
# if __name__=='__main__':
#     #3个矩阵拼接一共有3种情况，情况最好拼接完成有4条边，情况最差拼接出来有8条边，中间情况为6条边
#     N=int(input())
#     for n in range(N):
#         edge = 8  # 最多是8条边
#         a=list(map(int,input().strip().split()))
#         for i in range(0,2):#取第一个矩阵的边
#             for j in range(2,4):#取第二个矩阵的边
#                 for k in range(4,6):#取第三个矩阵的边
#                     x1,x2,x3=a[i],a[j],a[k]#取出后的边进行分别判断情况
#                     if x1==x2 and x2==x3:#第一种情况，比较完美也就是三个矩阵都有一条边相等，这种情况就是4条边
#                         edge=min(edge,4)
#                     if check4(x1,x2,x3,a):
#                         #第二种情况，当有一个矩阵的边等于另外两个矩阵边的合，比如x1=x2+x3，这样就把第二个矩阵的x2边和第三个矩阵的x3边拼接在第一个矩阵x1上
#                         #如果第二个矩阵除去x2这条边可以和第三个矩阵除去x3这条边可以重合也就是题给的第一个例子那么就是4条边
#                         edge=min(edge,4)
#                     if x1==x2 or x2==x3 or x1==x3:#第三种情况如果有两个矩阵有一条边相等，那么合并后就是6条边
#                         edge=min(edge,6)
#                     if check6(x1,x2,x3):
#                         #第四种情况，其实就是第二种情况的弱化，有一个矩阵的边等于另外两个矩阵边的合，比如x1=x2+x3但是仅仅满足这个条件
#                         #也就是题目给的第二种情况，这样的情况就是6条边
#                         edge=min(edge,6)
#         print(edge)
#
# count=0
#
# for i in range(1,2022):
#     if i*2021/math.gcd(i,2021)==4042:
#         count+=1
# print(count)



# t,a,p=map(int,input().strip().split())
# x=t/a
# m=a*p
# n=a*(p-1)+1
# if p<=x:
#     print(n,m)
# else:
#     print(1+(p-1)*a,t)
#
#
# def funx(s):
#     for i in range(len(s) - 1):
#         if s[i] >= s[i + 1]:
#             return 0
#     return 1
#
#
# s=input()
# if funx(s):
#     print("YES")
# else:
#     print("NO")
# i=1
# while True:
#     if 3**i>1000:
#         print(i)
#         break
#     i=i+1

# i=8
# while True:
#     i=i+1
#     z=i
#     for j in range(1,5):
#         # if z%5!=i:
#         #     break
#         z=z-j-(z-j)/5
#
#     if z%5==0 and z>=5:
#         print(z,i)
#         break


#
# s=input()
# x=s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u')
# y=len(s)-x
#
# print(x)
# print(y)
# import datetime
# data1=datetime.date(19000101)
#

# def isprime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0:
#             return False
#     return True
# count=0
# for i in range(2,2019//2+1):
#     if isprime(2019-i):
#         count+=1
#
# print(count)
#
# import os
# import sys
#
# dp = [0 for i in range(2020)]
# p = []
# # 先收集所有的质数
# for i in range(2, 2020):
#     isprime = True
#     if i <= 2:
#         p.append(i)
#     else:
#         for j in range(2, i):
#             if i % j == 0:
#                 isprime = False
#                 break
#         if isprime:
#             p.append(i)
#
# num = 2019
# s = len(p)
# dp[0] = 1
# # 进行初始化
# for i in range(s):
#     for j in range(num, p[i] - 1, -1):
#         # 质数要求两两不同，所以装下p[i]后就不能再用了，所以直接除去它
#         dp[j] += dp[j - p[i]]
# print(int(dp[2019]))
# # 我们希望获得是2019拆分的
# # 请在此输入您的代码
#

#
# def funx(i, j, k):
#     if k == 0:
#         return 0
#     if i<=0 or j<=0 or i>n or j>m:
#         return 0
#     if i-1>=1 and j>=1:
#         lst[i-1][j]=1
#         funx(i-1,j,k-1)
#     if i>=1 and j-1>=1:
#         lst[i][j-1]=1
#         funx(i , j-1, k - 1)
#     if i >= 1 and i<=n and j + 1 >= 1 and j+1<=m:
#         lst[i][j+1]=1
#         funx(i , j+1, k - 1)
#     if i+1>=1  and i+1<=n and j>=1:
#         lst[i+1][j]=1
#         funx(i +1, j, k - 1)
#
#
#
# n,m=map(int,input().strip().split())
# t=int(input())
# lst=[[0]*(m+1) for i in range(n+1)]
# l=[]
# for i in range(t):
#     l.append(list(map(int,input().strip().split())))
# k=int(input())
# for i in l:
#     lst[i[0]][i[1]]=1
#     funx(i[0],i[1],k)
#
# count=0
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if lst[i][j]==1:
#             count+=1
# print(count)
#
#

#
# n=int(input())
# la=list(map(int,input().strip().split()))
# lb=list(map(int,input().strip().split()))
# lc=list(map(int,input().strip().split()))
# count=0
# for i in la:
#     for j in lb:
#         for z in lc:
#             if i<j<z:
#                 count+=1
#
# print(count)
#
#

# n=int(input())
# la=list(map(int,input().strip().split()))
# lb=list(map(int,input().strip().split()))
# lc=list(map(int,input().strip().split()))
# la.sort()
# lb.sort()
# lc.sort()
# i=0
# k=0
# count=0
# for j in range(n):
#     while i<n and la[i]<lb[j]:
#         i+=1
#     while k<n and lb[j]>=lc[k]:
#         k+=1
#     count+=i*(n-k)
# print(count)
#



# i=1
# j=3
# z=1
# while  round(i/j,6)!=0.618034:
#     i,j=j,i+j
#     print(i,j)
#     z+=1
# print(z)




#
# n,m,t=map(int,input().strip().split())
# l=[0]*(n+1)
# s=set()
# d=dict()
# for i in range(m):
#     x,y=map(int,input().strip().split())
#     if y not in d:
#         d[y]=[x]
#     else:
#         d[y].append(x)
# # print(d)
#
# for i in d:
#     d[i]=list(set(d[i]))
#     d[i].sort()
# # print(d)
#
# for i in range(1,t):
#     for j in range(1,n+1):
#         if i in d[j]:
#             l[j]+=2
#             if l[j]>5:
#                 s.add(j)
#         else:
#             if l[j]>=1:
#                 l[j]-=1
#
#         # if i in :
#         #     l[i]+=2
#         # else:
#         #     l[i]-=1
# count=0
#
# for i in range(1,n+1):
#     if l[i]>3 and i in s:
#         count+=1
# print(count)
# # print(l)
# # print(s)
# #
# i=1
# def funx(s):
#     for j in range(len(s)//2):
#         if s[j]==s[len(s)-j-1]:
#             continue
#         else:
#             return 0
#     return 1
#
# while True:
#     n=i*(i+1)//2
#     if n-int(n)==0 and n>20220514 and funx(str(n)):
#         print(n)
#         break
#     i=i+1
#

# n=int(input())
# for i in range(int(math.sqrt(n))+1):



# matrix=[list(input()) for i in range(300)]
#
# def funx1(s):
#     count1=0
#     for i in s:
#         y=''.join(i)
#         count1+=y.count('2020')
#     return count1
#
# def funx2(s):
#     count2=0
#     for i in range(len(s[0])):
#         for j in range(len(s)):
#             if j+3<len(s):
#                 if str(s[j][i])+str(s[j+1][i])+str(s[j+2][i])+str(s[j+3][i])=='2020':
#                     count2+=1
#     return count2
#
# def funx3(s):
#     count3=0
#     for j in range(len(s[0])):
#         for i in range(len(s)-j):
#             if i+3<(len(s)-j):
#                 if s[i][i+j]+s[i+1][i+j+1]+s[i+2][i+j+2]+s[i+3][i+j+3]=='2020':
#                     count3+=1
#     return count3
# print(funx3(matrix)+funx2(matrix)+funx1(matrix))
#
#

# l=[1,2,3,4,5,6,7,8,9]
# s=set()
# for i in l:
#     for j in l:
#         for z in l:
#             if i!=j and i!=z and z!=i:
#                 s.add(str(i)+str(j)+str(z))
# s=list(s)
# def fux(st):
#     for i in range(1,10):
#         if str(i) not in st:
#             return 0
#     return 1
#
# s.sort()
# count=0
# for i in s:
#     for j in s:
#         z=str(int(i)+int(j))
#         if z in s and fux(i+j+z):
#             count+=1
# print(count)

# n=int(input())
# l=[]
# for i in range(n):
#     l.append(int(input()))
# x=min(l)
# y=max(l)
# for i in range(x,y+1):
#     for j in l:
#
# def funx(k):
#     k=str(k)
#     bk=0
#     for i in k:
#         bk+=int(i)
#     return bk;
#
# n=int(input())
# m=int(input())
# d=dict()
# for i in range(1,n+1):
#     d[i]=sum(list(map(int,str(i))))
# print(d)
# l=list(d.items())
# print(l)
# l.sort(key=lambda x:x[1])
# print(l)
# print(l[m-1][0])

# def f(s):
#     d=set()
#     for i in range(1,len(s)-1):
#         if s[i]==s[i-1] and s[i]!=s[i+1]:
#             d.add(i)
#             d.add(i+1)
#         if s[i]==s[i+1] and s[i]!=s[i-1]:
#             d.add(i)
#             d.add(i-1)
#     s=list(s)
#     for i in d:
#             s[i]=''
#     print(s)
#     return ''.join(s)
#
# s=input()
# for i in range(2**64):
#     temp=s
#     s=f(s)
#     if s==temp:
#         print(s)
#         break
#     if len(s)==0:
#         print('EMPTY')
#         break


# from itertools import *
# n=int(input())
# count=0
# l=[int(i+1) for i in range(n)]
# for i in itertools.permutations(l):
#     for j in range(1,n):
#         for k in range(0,j):
#             if i[k]<i[j]:
#                 count+=1
# print(count)

# n,m=map(int,input().split())
# a=[list(map(int,input().split())) for i in range(n)]
# ans=0
# while m>0:
#     a=sorted(a,key=lambda x:x[0],reverse=True)
#     ans+=a[0][0]
#     a[0][0]-=a[0][1]
#     m-=1
# print(ans)


# n,m=map(int,input().split())
# a=[list(map(int,input().split())) for i in range(n)]
# ans=0
# while m>0:
#     a=sorted(a,key=lambda x:x[0],reverse=True)#每次都从大到小排序
#     ans+=a[0][0]
#     a[0][0]-=a[0][1]
#     m-=1
# print(ans)



n,k=map(int,input().strip().split())
a=list(map(int,input().strip().split()))
i,c=0,0
while True:
    r=i+k
    if r<=n:
        if 0 not in a[i:r]:
            a[i:r] = map(lambda x: x - 1, a[i:r])
            print(a)
            c += 1
        else:
            i = a[i:r].index(0) + i + 1
    else:
        break
print(a)
c+=sum(a)
print(c)











