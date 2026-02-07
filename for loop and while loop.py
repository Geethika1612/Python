
#for,while,range,break,continue,pass
#for loop()

'''a=[10,20,30,40,50]
for i in a:
    print(i)'''


'''a=[10,20,30,40,50]
for i in a:
    print(a)'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=" ")                    #list
    print(type(a))
    print(type(i))'''

'''a=(10,20,30,40,50)
for i in a:                             #tuple
    print(i)
    print(type(a))
    print(type(i))'''

'''a={10,20,30,40,50}                     #set is unordered 
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a={"name":"geethika","age":20,"year":2004}
for i in a:                              #dictionary
    print(i)                             #inbulit it print keys 
    print(type(a))
    print(type(i))'''

'''a={"name":"geethika","age":20,"year":2004}
for i in a.values:
    print(i)                             #print keys 
    print(type(a))
    print(type(i))'''


'''fruits=["apple",20,2.0]
for i in fruits:
    print(i)                             
    print(type(fruits))
    print(type(i))'''

'''a=[10.2,2.0,32.0,41.0,5.0]                     
for i in a:
    print(i)
    print(type(a))                     #float
    print(type(i))'''


'''a=[5+9j,2+9j]
for i in a:
    print(i)                    #complex
    print(type(a))
    print(type(i))'''




'''a=[True,False,True]
for i in a:
    print(i)                    #bool
    print(type(a))
    print(type(i))'''


'''a=["python","java","html"]   #[Python,Java,Html]
for i in a:                   
    print(a.title())   #give error as list dont have title attribute
'''


'''a=["python","java","html"]   #[Python,Java,Html]
for i in a:                   
    print(i.title())            #i is string
'''

'''a=["python","java","html"]   #[Python,Java,Html]
b=str(a)
c=b.title()             #without for
print(c)
    '''


#while loop
'''
a=10                      #infinity
while a>1:
    print(a)'''




'''a=10                     
while a>1:
    print(a)            #print from 10-2 as decrement is after print statement
    a=a-1'''



'''a=10                     
while a>1:
    a=a-1               #print from 9-1 as decrement is before print statement
    print(a)'''

'''
a=10                     
while a>1:
print(a)            #syntax error
    a=a-1'''



'''
a=10                      #infinity
while a>1:
    print(a)
    a+=1
'''

'''a=1                      #a=less num then increment operator
while a<10:
    print(a)
    a+=1'''

'''
a=20                      #a=big num then decrement operator
while a>1:
    print(a)
    a-=1
'''

'''
while True:
    age=int(input("enter age"))
    if(age>=18):
        print("eligible for vote")
    else:
        print("not eligible for vote")
'''





