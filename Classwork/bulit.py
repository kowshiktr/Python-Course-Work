
import sys
print(sys.argv)
print(sys.path)
print(sys.version)
print(sys.exit())

'''
ouput:
['d:\\PythonCourseWork\\Classwork', 'C:\\Users\\Kowshik\\AppData\\Local\\Programs\\Python\\Python313\\python313.zip', 'C:\\Users\\Kowshik\\AppData\\Local\\Programs\\Python\\Python313\\DLLs', 'C:\\Users\\Kowshik\\AppData\\Local\\Programs\\Python\\Python313\\Lib', 'C:\\Users\\Kowshik\\AppData\\Local\\Programs\\Python\\Python313', 'C:\\Users\\Kowshik\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages']
3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)]
'''
import sys
a=10
b=20
print(a+b)
sys.exit(1)
print(a-b)

'''
ouput:
30
'''

import platform
print(platform.system())
print(platform.release())
print(platform.processor())

'''
output:
Windows
11
AMD64 Family 25 Model 68 Stepping 1, AuthenticAMD
'''

import math
print(math.sqrt(25))
print(math.pow(2,3))
print(round(12.3))
print(round(12.8))
print(math.ceil(12.3))
print(math.ceil(12.8))
print(math.ceil(12.1))
print(math.floor(12.3))
print(math.floor(12.8))
print(math.floor(12.1))
print(math.fabs(-12))
print(abs(-12))
print(math.factorial(5))
print(math.gcd(8,24))
print(math.log(2))
print(math.sin(45))
print(math.cos(0))
print(math.tan(55))
print(math.degrees(45))
print(math.radians(30))

'''
output:
5.0
8.0
12
13
13
13
13
12
12
12
12.0
12
120
8
0.6931471805599453
0.8509035245341184
1.0
-45.18308791052113
2578.3100780887044
0.5235987755982988
'''

import random
print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))
names=['varun','manju','kiran','adithya','prabhas','kowshik']
print(random.choice(names))
print(random.choices(names,k=3))
random.shuffle(names)
print(names)
'''
ouput:
0.9121898054667139
2
2.0917687719515827
adithya
['manju', 'prabhas', 'varun']
['manju', 'varun', 'prabhas', 'adithya', 'kowshik', 'kiran']

0.22979944734638713
6
1.9767769902228634
kowshik
['adithya', 'kowshik', 'prabhas']
['kowshik', 'kiran', 'adithya', 'manju', 'prabhas', 'varun']

0.26564267165348177
4
5.10245435214314
prabhas
['varun', 'varun', 'varun']
['varun', 'kiran', 'manju', 'prabhas', 'adithya', 'kowshik']
'''







