#n=int(input())
#b=bin(n)[2:]
#print(b)
#count=0
#for i in range(len(b)):
 #   if b[i]=='1':
 #      count+=1
#if count%2==0:
 #   print("evil num")
#else:
#    print("Not evil num")




n=19
while(n>0):
     r=n%10
     n=n//10
     sum=r**2+n**2
     n=n-1
     print(sum)
     t=sum
     while (t>0):
         r=t%10
         t=t//10
         sum=r**2+t**2
         t=-8
         print(sum)
         p=sum
         while(p>0):
           r=p%10
           p=p//10
           sum=r**2+p**2
           p=-6
           l=sum
           print(sum)
           while(l>0):
             r=l%100
             l=l//100
             sum=r**2+l**2
             l=-1
             k=sum
             print(sum)
             if sum==1:
                  print("happy num")
             else :
                  print("unhappy num")


















