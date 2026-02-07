#Global Variable and Local variable
'''
A variable inside and outside the function is called global and local variable.
A variable is defined above the function and accessable to the entire global space is called global variable and
A variable inside the function is called local variable.
'''
#first case of global variable
'''
a=3
def check():
    print("inside value is",a)
check()
print("outside value is",a)
'''


#second case of global variable
'''
a=2
def check1():
    a=5
    a=a**2
    print("inside value is",a)
check1()
print("outside value is",a)
'''

#third case of global and local variable
'''
a=4
b=7
def check2():
    a=5
    print("inside value is",a)
    a=10
    print("updated value:",a+5)
    b=13    #local variable
    b=b+a
    print("value of b is",b)
check2()
print("a value is",a)
print("b value is",b)
'''

'''
Usage of Global keyword:
When user wants to access the global variable inside the function directly
and carry forward the updated value even outside the function then we need
to use global keyword.
'''
#fourth case of global and local variable


a=8
def final():
    global a,b
    print("inside value is",a)
    a=4
    print("updated value:",a)
    b=15   #global b
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)




























