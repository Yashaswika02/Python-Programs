n=input()
count=0
print(bin(int(n)))
for i in range(len(n)):
  if n[i]==1 :
      count+=1
  elif count%2==0 :
      print("Evil number")
  else:
      print("Not evil")
        
      
