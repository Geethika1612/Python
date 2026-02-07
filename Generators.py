#Generators
'''
No tuple comprehension in above cases if we remove those braces and
keep paranthesis then the outcome is Generator.
'''
#list comprehension
#a=[expr for var in collection/range]
'''
a=[i for i in range(16)]
print(a)
print(type(a))
'''
'''
a=(i for i in range(16))     #Generator
print(a)
print(*a)
print(type(a))
'''

'''
a=(i for i in range(16))
print(a)
print(list(a))         # converts into list but datatype will be generator 
print(type(a))
'''

'''
a=(i for i in range(16))
print(a)
print(tuple(a))         # converts into tuple but datatype will be generator 
print(type(a))
'''

'''
a=(i for i in range(16))
print(a)
print(set(a))         # converts into set but datatype will be generator 
print(type(a))
'''

'''
a=(i for i in range(16))
print(a)
print(dict(a))         # gives error
print(type(a))
'''



#GENERATORS Definition
'''
A Generator is also a function which can be used as an iterator(loop)
by producing grp of values where yield is keyword.

Return and Yield diff:
it will terminate the function whereas yield can pass the function and go on with every sucessive iteration

'''
'''
a,b=[int(x) for x in input("Enter the value").split(",")]
def check(a,b):               #output:    2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 11
    while(a<b):      
        yield a               # it's passing before increment so it gives values 2 times 
        a=a+1
        yield a
print(*check(a,b))
'''
'''
a,b=[int(x) for x in input("Enter the value").split(",")]
def check(a,b):               #output:   3 4 5 6 7 8 9 10 11
    while(a<b):
        #yield a
        a=a+1
        yield a
print(*check(a,b))
'''

'''
a,b=[int(x) for x in input("Enter the value").split(",")]
def check(a,b):               #output:   Enter the value2,11
    while(a<b):                #           3   prints only 3 because return terminates 
        #yield a
        a=a+1
        return a
print(check(a,b))
'''

#diff btw return and yield
'''
def mygen():
   # return "python"        #prints only python as return terminates 
    #return"java"
    #return"c"
   return "python","java","c"      
print(*mygen())               #don't  give error even we use * argument because return has more than one to return 
'''
'''
def mygen():
    yield "python"        #prints all 
    yield"java"
    yield"c"
print(*mygen())
'''


def mygen():
    yield "python"       
    yield"java"
    yield"c"

d=mygen()
print(next(d))           #prints only python here(1st word)
print(next(d))
print(next(d))




























