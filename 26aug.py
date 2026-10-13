#CODE ON CARS:
##class Car:
##    wheels=0
##    airbags=0
##    seats=0
##
##    def purpose(self):
##        print("I carry people from one place to another")
##    def start(self):
##        print("The car started moving")
##    def stop(self):
##        print("The car came to a hault")
##
##car1=Car()
##car1.wheels=4
##car1.airbags=3
##car1.seats=5
##print("Car1 details")
##print(car1.wheels)
##print(car1.airbags)
##print(car1.seats)
##car1.purpose()
##car1.start()
##car1.stop()
##
##car2=Car()
##car2.wheels=4
##car2.airbags=7
##car2.seats=10
##print("Car2 details")
##print(car2.wheels)
##print(car2.airbags)
##print(car2.seats)
##car2.purpose()
##car2.start()
##car2.stop()



#CODE ON STUDENTS:
##class Student():
##    name=0
##    rollno=0
##    marks=0
##    def cal_grade(self):
##        if self.marks>=90:
##            print("Grade A")
##        elif self.marks>=50:
##            print("Grade B")
##        else :
##            print("Fail")
##
##
##s1=Student()
##s1.name="supriya"
##s1.rollno=21
##s1.marks=95
##print("---STUDENT1 DETAILS---")
##print(s1.name)
##print(s1.rollno)
##print(s1.marks)
##s1.cal_grade()
##
##s2=Student()
##s2.name="priya"
##s2.rollno=10
##s2.marks=60
##print("---STUDENT2 DETAILS---")
##print(s2.name)
##print(s2.rollno)
##print(s2.marks)
##s2.cal_grade()
##
##s3=Student()
##s3.name="riya"
##s3.rollno=4
##s3.marks=15
##print("---STUDENT3 DETAILS---")
##print(s3.name)
##print(s3.rollno)
##print(s3.marks)
##s3.cal_grade()


#CODE ON BANKACCOUNT:
##class Bankaccount():
##    name=0
##    acc_no=0
##    balance=0
##
##    def display(self):
##        print("name:",self.name)
##        print("acc_no:",self.acc_no)
##        print("balance:",self.balance)
##    def deposit(self):
##        n=int(input("Enter money:"))
##        total=n+self.balance
##        print("Deposit succesful")
##        print("total:",total)
##    def withdrawal(self):
##        m=int(input("Enter money:"))
##        balance_amt=self.balance-m
##        print("Withdraw success")
##        print("Balance:",balance_amt)
##
##person1=Bankaccount()
##person1.name="ayan"
##person1.acc_no=234567
##person1.balance=20000
##person1.display()
##person1.deposit()
##person1.withdrawal()


#CODE ON RENTAL CARS:
##class Rent:
##    car_id=0
##    model=0
##    rent_per_day=0
##    max_no_days=0
##    no_of_days_used=0
##    fine=0
##    def display( self,c,mo,r,m,n,f):
##        self.car_id=c
##        self.model=mo
##        self.rent_per_day=r
##        self.max_no_days=m
##        self.no_of_days_used=n
##        self.fine=f
##        print("Car id:",c)
##        print("model:",mo)
##        print("rent_per_day:",r)
##        print("max_no_days:",m)
##        print("no_of_days:",n)
##        
##    def cal_rent(self):
##        rent=self.max_no_days*self.rent_per_day
##        print("Car Rent:",rent)
##        if self.no_of_days_used>self.max_no_days:
##            print("Fine:",self.fine)
##car1=Rent()
##print("--CAR1--")
##car1.display(2345,5000,50,5,3,100)
##car1.cal_rent()
##car2=Rent()
##print("--CAR2--")
##car2.display(4789,2050,250,5,6,100)
##car2.cal_rent()


class Employee:
    name=0
    id=0
    salary=0
    def __init__(self,n,id,s):
        self.name=n
        self.id=id
        self.salary=s
        print("Name:",n)
        print("Id:",id)
        print("Salary:",s)
        
class Teacher(Employee):
    def display_details(self):
        self.subject="Telugu"
        print("Subject:",self.subject)


t=Teacher("priya",23,4000)
t.display_details()
    




    
        



    




























    
