'''n=5
for i in range(n-1):
    print("*",end=" ")            # * * * * *
'''
'''
0 1 2
0 1 2
0 1 2

n=int(input("Enter n value:"))
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()
'''

'''
0 0 0
1 1 1
2 2 2

n=int(input("Enter n value:"))
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()
'''
'''
0 0 0
0 0 1
0 0 2

0 1 0
0 1 1
0 1 2

0 2 0
0 2 1
0 2 2


1 0 0
1 0 1
1 0 2

1 1 0
1 1 1
1 1 2

1 2 0
1 2 1
1 2 2

2 0 0
2 0 1
2 0 2

2 1 0
2 1 1
2 1 2

2 2 0
2 2 1
2 2 2


n=int(input("Enter n value:"))
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i,j,k)
        print()
        '''
'''
* * * 
* * * 
* * *

n=int(input("Enter n value"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
    
'''
