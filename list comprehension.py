#list comprehension
a=['codegnan','python','course']
#['CODEGNAN','PYTHON',COURSE']
#print(a.upper())
'''b=str(a)
c=b.upper()
print(c)
'''
#syntax
#a=[expre for var in collection/range]
'''
a=[x.upper() for x in a]
print(a)'''

#tak-1
'''a=['vja','vzg','bng']
#['Vij','Vzg','Bng']
                                    #variable can be any letter 
a=[x.title() for x in a]
print(a)
'''
#task-2

'''a=[1,2,4,5,6,8,12,13]
#[1,4,9,16,25,36,64,144,169]

a=[x*x for x in a]
a=[pow(x,2) for x in a]
a=[x**2 for x in a]
print(a)'''


#if-usage in list comprehension

'''
a=[x for x in range(16) if x%2==0 ]              #even
print(a)


a=[x**2 for x in range(16) if x%2==0 ]           #square of even 
print(a) 



a=[x for x in range(16) if x%2!=0 ]              #odd
print(a)


a=[x**2 for x in range(16) if x%2!=0 ]           #square of odd
print(a)
'''

'''
a=["apple","banana","manago","berry","kiwi","dragon"]
#print fruit names having letter a
b=[x for x in a if "a"in x]
print(b)

#print fruit names not having letter a
b=[x for x in a if "a" not in x]      
print(b)

'''

#no elif usage in list comprehension
'''
a=[x**2 if x%2==0 else x*5 for x in range(21) ]                #if and else then range should be at last
print(a)
'''


a=[1,2,3,4,5]
b=[5,4,3,2,1]
#output=   [6,6,6,6,6]


c=[a[i]+b[i] for i in range(5)]   #method-1
c=[a[i]+b[i] for i in range(len(a))]   #method-2
print(c)





