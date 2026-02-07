#vriable length arguments
'''
def check(*a):                  #length arugement automatically stores as tuple
    print(a)
    print(type(a))
check()
check(2,6,2,4,4)
b=[3,4,2,6,1]
check(*b)
c={4,55,6,7,8,9}
check(*c)
d={"year":2026,"day":"fri"}
check(*d)
'''
'''
def check1(*a):
    d=2    #creating variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):             #only int and float values will print
             d=d+i
             print(d)
            
       
        
check1()
check1(2,3,4,5,6)
check1(2,3,4,5,2.5,3.2)
check1(2,3,4.2,3.5,"geethika",5+9j,True,False)
'''


#kwargs(**)                                 #Gives Dictionary
'''
def Details(**a):
    print(a)
    print(type(a))
Details()
d={"idnos":[10,20,30],
   "names":["geethika","sunitha","chetana"],
   "place":["vij","vzg","hyd"]
   }
Details(**d)
'''

'''
def Details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():          #prints keys 
        print(i)
    for i in a:
        print(a[i])             #print keys
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
Details()
d={"idnos":[10,20,30],
   "names":["geethika","sunitha","chetana"],
   "place":["vij","vzg","hyd"]
   }
Details(**d)
'''


def final(*a,**b):
    d=1
    print(a)                #  ()
    print(b)                #{}
    print(type(a))          # tuple
    print(type(b))          # dict
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is", i)
        print("value is",j)
final()
data=(2,3,4,3.2,6.2)
final(*data)                #function call i.e d=d+i

details={"idnos":[10,20,30],
   "names":["geethika","sunitha","chetana"],
   "place":["vij","vzg","hyd"]
   }
final(**details)
final(*data,**details)
















