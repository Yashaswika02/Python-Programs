#wap to read a name from the user change the even indexed chars to its  next alphabet in an alphabetical order

##def evn_char(name):
##    for i in range(len(name)):
##      if i%2 ==0 and name[i].isalpha:
##        if name[i]=='z':
##            print("a")
##        elif name[i]=='Z':
##            print("A")
##        else:
##            print(chr(ord(name[i])+1),end="")
##      else:
##          print(name[i],end='')
##name=input("Enter name:")
##evn_char(name)


#wap to move all zeroes in a list to right or left side


##def mov_zeroes(nums):
##    for i in nums:
##      if i==0 :
##          z.append(i)
##      else:
##          nz.append(i)
##    nz.extend(z)
##    print(nz)
##           
##nums=list(map(int,input("Enter numbers:").split()))
##nz=[]
##z=[]
##mov_zeroes(nums)



##def separate_data():
##    l=[1,3,5,"hi","mom","dad",True,False]
##    a=[]
##    n=[]
##    b=[]
##    for el in l:
##        if type(el)==int and el%2!=0:
##            a.append(el)
##        elif type(el)==str and el==el[::-1]:  
##            n.append(el)
##        elif type(el)==bool and el==True or el==False:
##            b.append(el)
##    print(a,n,b)
## 
##separate_data()


## 
##for i in range(5):
##    for j in range(5):
##        if j==i:
##            print(j,end='  ')
##        else:
##            print("*",end=" ")
##     
##    print()



##l=[2,46,5,-34,785,57,90,5678,0,-1,654]
##n= 5
##for i in l:
##    for j in range(len(n)):
##   if i > n and  :
##       print(i)



def num_guess():
    import random
    num=random.randint(1,30)
    ch=5
    points=0
    while ch>0:
        g_num=int(input())
        if ch==5 and g_n==num:
              points+=10
              break
        elif ch==4 and g_n==num:
              points+=8
              break
        elif ch==3 and g_n==num:
              points+=6 
              break
        elif ch==2 and g_n==num:
              points+=4 
              break
        elif ch==1 and g_n==num:
              points+=2  
              break
        else:
             ch-=1
try:
    num_guess()
except:
    print("enter only numbers")

        

















