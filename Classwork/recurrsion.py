
def numbers(n):
    if n==0:
        return 
    print(n)
    return numbers(n-1)
numbers(12)
'''
output:
12
11
10
9
8
7
6
5
4
3
2
1
'''

def numbers(n):
    if n==15:
        return
    print(n)
    return numbers(n+1)
numbers(1)
'''
output:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
'''

def numbers(n):
    if n==0:
        return 
    print(n,end=" ")
    return numbers(n-1)
numbers(10)
'''
output:
10 9 8 7 6 5 4 3 2 1 

'''

def product(n):
    if n==1:
        return n
    return n*product(n-1)
print(product(10))
'''
output:
3628800
'''

def display(s,ind):
    if ind==len(s):
        return
    print(s[ind])
    display(s,ind+1)
s='python programming'
display(s,0)
'''
output:
p
y
t
h
o
n
 
p
r
o
g
r
a
m
m
i
n
g
'''

def display(s,ind):
    if ind==len(s):
        return
    print("before:",s[ind],end='\t')
    display(s,ind+1)
    print("before:",s[ind],end='\t')
s='python programming'
display(s,0)
'''
output:
    before: p	before: y	before: t	before: h	before: o	before: n	before:  	before: p	before: r	before: o	before: g	before: r	before: a	before: m	before: m	before: i	before: n	before: g	before: g	before: n	before: i	before: m	before: m	before: a	before: r	before: g	before: o	before: r	before: p	before:  	before: n	before: o	before: h	before: t	before: y	before: p	

'''

def display(s,ind):
    if ind==len(s):
        return
    print(s[ind],end='\t')
    display(s,ind+1)
    print(s[ind],end='\t')
s='python programming'
display(s,0)
'''
output:
    p	y	t	h	o	n	 	p	r	o	g	r	a	m	m	i	n	g	g	n	i	m	m	a	r	g	o	r	p	 	n	o	h	t	y	p	

'''

n=int(input("enter the number:"))
sumofdigit=0
while n>0:
    sumofdigit+=(n%10)
    n=n//10
print(sumofdigit)
'''
output:
    enter the number:234545
23
'''

def sumofdigits(n):
    if n<=0:
        return n
    return (n%10)+sumofdigits(n//10)
n=int(input("enter the numbers:"))
print(sumofdigits(n))
'''
output:
    enter the numbers:45678
30
'''

def sumofdigits(n):
    if n<=0:
        return n
    return (n%10)+sumofdigits(n//10)
n=int(input("enter the numbers:"))
print(sumofdigits(n))

'''
output:
    enter the numbers:62779
31
'''


