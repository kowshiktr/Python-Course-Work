
for row in range(6):
    for col in range(10):
        print('#',end=' ')
    print()
'''
output    
# # # # # # # # # # 
# # # # # # # # # # 
# # # # # # # # # # 
# # # # # # # # # # 
# # # # # # # # # # 
# # # # # # # # # # 
'''

for row in range(5):
    for col in range(3):
        print(row,end=' ')
    print()
'''
output
0 0 0 
1 1 1 
2 2 2 
3 3 3 
4 4 4
'''



for row in range(5):
    for col in range(row+1):
        print(row,end=' ')
    print()
'''
output    
0 
1 1 
2 2 2
3 3 3 3
4 4 4 4 4
'''
    

n=int(input("enter the size:"))
for row in range(5):
    for col in range(3):
        print('*',end=' ')
    print()
'''
output   
input enter the size:5
* * * 
* * *
* * *
* * *
* * *

'''

n=int(input("enter the size:"))
for row in range(n):
    for space in range(n-row-1):
        print('*',end=' ')
    print()
'''
output
input enter the size:5
* * * * 
* * *
* *
*
'''
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(row+1):
        print(row,end=' ')
    print()  
'''  
output
input Enter the size:10
0 
1 1
2 2 2
3 3 3 3
4 4 4 4 4
5 5 5 5 5 5
6 6 6 6 6 6 6
7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9 
'''

n=int(input("Enter the size :"))
for row in range(n):
    for col in range(n-row):
        print("#",end=" ")
    print()
''''
output
input Enter the size :10
# # # # # # # # # # 
# # # # # # # # #
# # # # # # # #
# # # # # # #
# # # # # #
# # # # #
# # # #
# # #
# #
#
'''

n=int(input("enter the size :"))
for row in range(n):
    for spa in range (n-row-1):
        print(" ",end=" ")
    for col in range(row+1):
        print("#",end=" ")
    print()
'''0

output
input enter the size :10
                  # 
                # #
              # # #
            # # # #
          # # # # #
        # # # # # #
      # # # # # # #
    # # # # # # # #
  # # # # # # # # #
# # # # # # # # # #
'''
