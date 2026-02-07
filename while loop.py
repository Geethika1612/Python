#while loop
'''a=1
while a<10:
    print(a)
    a+=1'''
'''a=20
while a>1:
    print(a)
    a-=1'''
#voting
'''while True:
    age = int(input("Enter age: "))
    if age >= 18:
        print("eligible to vote.")
    else:
        print("not eligible to vote.")'''
#tasks in loops
#vowel or consonant
'''char = input("enter a character: ").lower() #convert to lower case
vowels = "aeiouAEIOU"
if char in vowels:
    print(char, "is a vowel.")
else:
    print(char, "is a consonant.")'''


#different type of cakes
##price 1200, redvelvet cake
##price 1000, chocolate cake
##price 800, choco-almond cake
##price 600, butterscotch cake
##any other price range entered cake is not available

'''while True:
    price = int(input("Enter price: "))
    if price == 1200:
        print("red velvet cake")
        break
    elif price == 1000:
        print("chocolate cake")
        break
    elif price == 800:
        print("choco-almond cake")
        break
    elif price == 600:
        print("butterscotch cake")
        break
    else:
        print("Cake not available")
        break'''

#range() -> the range funcation returns a sequence of numbers, starting from zero by default
#and increments by one by one and stops before a specified number.
#start-stop-step
'''for i in range(10):
    print(i)'''
'''for i in range(5,15):
    print(i)'''
#task
#1 - (2,4,6,8,10,12,14,16,18)
'''for i in range(2,20,2):
    print(i,end=",")'''
#2 - (5,10,15,20,25,30,35,40,45)
'''for i in range(5,50,5):
    print(i,end=",")'''

#3 = (0,3,6,9,12,15,18,21,24,27)
'''for i in range(0,30,3):
    print(i,end=",")'''
#task
#marks, grades
#91-101 - grade A , 81-91 - grade B, 71-81 - grade c, 50-71 - grade D, 50 below - fail
'''while(1):
    a = int(input("Enter your marks: "))
    if a in range(91,101):
        print("GRADE A")
    elif a in range(81,91):
        print("gRADE B")
    elif a in range(71,81):
        print("GRADE C")
    elif a in range(50,71):
        print("GRADE D")
    elif a in range(0,50):
        print("Fail")
    else:
        print("result not available")'''

#break-continue-pass 
#break is used to terminate the enitre loop
#continue is used to skip the current iteration and rest of the code will continue
#pass is a null stmt. It does nothing but syntatically we need it.

#break
'''a=10
while a>1:
    print(a)
    a=a-1
    if a == 8:
        break'''
'''a=10
    while a>1:
        a=a-1
        if a==9:
            break
        print(a)'''

'''for i in range(20):
    if i == 12:
        break
    print(i)'''


'''a="geethika"
for i in a:
    if i=="a":
        break
    print(i)'''

#continue
'''a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        continue'''
'''a=20
while a>5:
    a=a-1
    if a==10:
        continue
    print(a)'''
'''
for i in range(15):
    if i==7:
        continue
    print(i)'''
'''a="word"
for i in a:
    if i == "d":
        continue
    print(i)'''
    
#pass
'''a=25
while a>10:
    print(a)
    a=a-1
    if a==10:
        pass'''
'''for i in range(30):
    if i==15:
        pass
    print(i)'''

'''a="geethika"
for i in a:
    if i == "s":
        pass
    print(i)'''










