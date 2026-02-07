amount=int(input("Enter amount"))
card=input("Insert card")
username=input("enter username")
if(card=="c"):
    print("Welcome",username)
    pwd=int(input("Enter password"))
    if(pwd==1234):
            print("Enter 1 for Balence Enquiery")
            print("Enter 2 for Withdraw")
            choice=int(input())
            if(choice==2):
                withdraw=int(input("Enter amount to withdraw:"))
                a=amount-withdraw
                print("Total amount :",a)        
            else:
                print("Your Balence:",amount)          
    else:
        print("Incorrect Password")
else:
    print("Invalid Card")
   
        
