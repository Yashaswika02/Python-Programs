##def is_prime(n):
##   for i in range(2,n):
##      if n%i==0 :
##          return False
##   else:
##       return True
##try:
##    n=int(input("Enter number:"))
##    if is_prime(n) and is_prime(n+2) or is_prime(n-2):
##        print("twin prime")
##    else:
##        print("not twin prime")
##except:
##    print("enter only integers")


#RECURSION: It is a special technique to execute block of code number of times
#without using loops
#recursion contains 3 components:recursion block,termination block,value update
#recursion max limit of recursion is 1023

##def factorial(n):
##    if n<=1:
##        return 1
##    else:
##        return n*factorial(n-1)
##print(factorial(6))

#wap to calculate the time taken by program adding two numbers:
##import time
##st=time.time()
##def add(n,m):
##    return n+m
##n=int(input("enter num:"))
##m=int(input("enter num:"))
##print(add(n,m))
##et=time.time()
##print(et-st)

 

##l=int(input("enter litres:"))
##if can1==1litre :
##   r=l//1
##   print(r)
##elif can2==2litre:
##   r=l//2
##   print(r)
##elif can3==5litre:
##   r=l//5
##   print(r)
##elif can4==10litre:
##   r=l//10
##   print(r)



#wap for ticket booking system
import random
import time
cn=input("enter number:")
st="9876"
def cell_number(cn):
   if cn[0] in st: 
     if len(cn)==10 and cn.isdigit():
        print("entered cell number")
        otp=random.randint(1000,9999)
        print(otp)
        enter=int(input("enter otp:"))
        if otp == enter:
           print("Proceed to bookings")
        else:
           print("invalid cell number")
     else:
         print("only 10digits allowed")
   else:
         print("not ind-num")

def seats():
   l=[0,0,0,0,0,0,0,0,0,0]
   av=10
   print("\tWELCOME TO MAX CINEMAS")
   print(f"available seats are {l}")
   s=int(input("Enter number of seats:"))
   if s<av and s>0:
      for i in range(s):
         l[i]=1
      print("tickets booked")
      print(f"Reamaining seats are{l}")

def ticket_price():
     payment=input("Select\n1.UPI\n2.Credit/Debit Card\n3.bankaccount")
     if payment=='1':
        print("payment success through UPI")
     elif payment=='2':
        print("payment success through Credit/Debit Card")
     elif payment=='3':
        print("payment success through bank account") 
     else:
        print("Payment Failed")
cell_number(cn)
seats()
ticket_price()



    
              
     

































   



 
    








