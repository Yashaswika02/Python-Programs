def bs():
    am=50
    qu=int(input("enter quantity"))
    bill=am*qu
    print("----------------------")
    print("amount:",bill)
    print("gst:18")
    print(bill+18)
def van():
    am=30
    qu=int(input("enter quantity"))
    bill=am*qu
    print("----------------------")
    print("amount:",bill)
    print("gst:18")
    print(bill+18)
def sb():
    am=30
    qu=int(input("enter quantity"))
    bill=am*qu
    print("----------------------")
    print("amount:",bill)
    print("gst:18")
    print(bill+18)
def mwa():
    am=12
    qu=int(input("enter quantity"))
    bill=am*qu
    print("----------------------")
    print("amount:",bill)
    print("gst:18")
    print(bill+18)

print("\t**WELCOME TO CHIMTU ICECRMZZ")
op=input("menu\n1.bs---50/-\n2.van---30/-\n3.sb---30/-\n4.mwa---12/-")
if op=='1':
    bs()
elif op=='2':
    van()
elif op=='3':
    sb()
elif op=='4':
    mwa()
else:
    print("invalid option")









    



