#BINARY SEARCH:binary search takes only sorted list
##def binary_search(ls,target):
##    low=0
##    high=len(ls)-1
##    while low<=high:
##        mid=(low+high)//2
##        if ls[mid]==target:
##            return mid
##        elif ls[mid]<target:
##            low=mid+1
##        else:
##            high=mid-1
##    return -1
##
##ls=[1,2,3,4,5,6,7,8,9]
##print(binary_search(ls,9))   #time complexity is o(n)/2 ==o(log n)


#TERNARY SEARCH:
def ternary_search(l,target):
    low=0
    high=len(l)-1
    while(low<=high):
        m1=low+((high-low)//3)
        m2=high-((high-low)//3)
        if target==l[m1]:
            return m1
        if target==l[m2]:
            return m2
        
        if (l[m1]<target and l[m2]>target) :
             low=m1+1
             high=m2-1
        elif l[m1]>target:
             low=0
             high=m1-1 
        else:
           low=m2+1
    return -1
l=[2,4,5,23,56,67,87]
print(ternary_search(l,5))
        
     






















#wap to count the occurence of given character in given name
##
##def ch_ct(name):
##    count=0
##    for i in name: 
##        if i in "aA":
##            count+=1
##    print(count)
##ch_ct("Akaksha")


#wap to count the occurence of each chr in given name
##d={}
##name=input("enter name:")
##for ch in name:
##    if ch not in d:
##        d[ch]=1
##    else:
##        d[ch]+=1
##print(d)











            
            
    
