
data=('xyz@gmail.com','xyz@123')
def login(username,mail,password):
    if mail==data[0]and password==data[1]:
        print(f"{username}-login succesful")
    else:
        print(f"{username}-invaild login")

username=input("enter the username:")
mail=input("enter the mail:")
password=input("enter the password:")
login(mail,password,username)
'''
OUTPUT
enter the username:xyz
enter the mail:xyz@gmail.com
enter the password:xyz123
xyz@gmail.com-invaild login
'''
data=('xyz@gmail.com','xyz@123')
def login(password,mail,username):
    if mail==data[0]and password==data[1]:
        print(f"{username}-login succesful")
    else:
        print(f"{username}-invaild login")

username=input("enter the username:")
mail=input("enter the mail:")
password=input("enter the password:")
login(mail,password,username)
'''
output
enter the username:xyz
enter the mail:xyz@gmail.com
enter the password:xyz123
xyz-vail login
'''
def sum(*l):
    s=0
    for i in l:
        s=s+i
    return l
print(sum(1,2,3,4,5,6,7))
print(sum(1,2,3))
print(sum(1,2))
'''
output
(1, 2, 3, 4, 5, 6, 7)
(1, 2, 3)
(1, 2)
'''

def display(**l):
    
    return l
print(display(python=34,sql=56,htm=75))
print(display(python=34,sql=66))
print(display(python=94))
'''
output
{'python': 34, 'sql': 56, 'htm': 75}
{'python': 34, 'sql': 66}
{'python': 94}
'''
def outer_fun():
    course='python'
    def inner_fun():
        batch=30
        print("inside_function:",batch,course)
    inner_fun() 
    print("inside function:",course)
outer_fun()

'''
output
inside_function: 30 python
'''
def outer_fun():
    course='python'
    def inner_fun():
        nonlocal course
        course='java'
        print("student modification :",course)
        
    inner_fun() 
    print(":",course)
outer_fun()
#print("outside function",course)
'''
output
student modification : java
: java
'''
def add(a,b):
    return a+b
print(add(2,3))
def sub(a,b):
    print(a-b)
sub(10,5)
'''

output
5
5
'''

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
'''
output

5+541+6516-5645464
-5638402
45649861+80484654
126134515
165498489*4465489
739031682146121
844548951/6
140758158.5
'''

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
exp=input("enter the experssion:")
op=None
for i in exp:
    if not i.isdigit():
        op=i
        break
a,b=exp.split(op)
a,b=int(a),int(b)
if op=='+':
    print(add(a,b))
elif op=='-':
    print(sub(a,b))
elif op=='*':
    print(mul(a,b))
elif op=='/':
    print(div(a,b))
elif op=='%':
    print(mod(a,b))
'''
output
enter the experssion:549451694+489879
549941573
84694169498-95498049879
-10803880381
92789480/984980489
0.09420438377840802
498248549%659+842795984289
842795984685
84949844+849824294-849884454
84889684
8484894849%89428484-845984094
-767366741
'''

def update(val):
    val.append(5)
    print("inside the function:",val)
val=[1,2,3,4,5]
update(val)
print("outside function:",val)
'''
output

inside the function: [1, 2, 3, 4, 5, 5]
outside function: [1, 2, 3, 4, 5, 5]

'''

def update(val):
    val=val.copy()
    val.append(20)
    print("inside the function:",val)
val=[1,2,3,4,5]
update(val)
print("outside function:",val)
'''
output
inside the function: [1, 2, 3, 4, 5, 20]
outside function: [1, 2, 3, 4, 5]
'''
