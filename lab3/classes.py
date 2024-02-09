#task1
class StringManipulator:
    def __init__ (self):
        self.input_string = ""
        

    def getString(self):
        self.input_string = input("Enter a string:")
        
    def printstring(self):
        print("String in a upper case:", self.input_string.upper())
        
string_manipulator = StringManipulator()
string_manipulator.getString()
string_manipulator.printstring()

#task2
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Square(Shape):
    def __init__ (self, length):
        super().__init__()
        self.length = length
        
    def area(self):
        return self.length ** 2
try:
    length_input = float(input("Enter the length of square: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()
    
square_obj = Square(length=length_input)
print("Area of Square:", square_obj.area())
        
#task3
class Shape:
    def __init__(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        
    def compute_area(self):
        return self.length * self.width
    
    
length_input = float(input("Enter the length of the rectangle: "))
width_input = float(input("Enter the width of the rectangle: "))
rectangle_instance = Rectangle(length_input, width_input)
area = rectangle_instance.compute_area()
print(area)

#task4
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_x, other_y):
        return math.sqrt((self.x - other_x)**2 + (self.y - other_y)**2)

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
point1 = Point(x1, y1)

x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))
point2 = Point(x2, y2)

point1.show()
point2.show()

distance = point1.dist(point2.x, point2.y)
print("Distance between the points:", distance)

#task5
class Account:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}, Current balance: ${self.balance}")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ${amount}.Current balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal denied.")
            
owner_name = input("Enter the owner's name: ")
initial_balance = float(input("Enter the initial balance: "))
account1 = Account(owner=owner_name, balance=initial_balance)

deposit_amount = float(input("Enter the deposit amount: "))
account1.deposit(deposit_amount)

withdraw_amount = float(input("Enter the withdrawal amount: "))
account1.withdraw(withdraw_amount)
#ex6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num** 0.5) + 1):
        if num % i == 0:
            return False
        return True
    
input_numbers =  input("Enter a list of numbers separated by commas: ")
numbers = [int(x) for x in input_numbers.split(',')]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Original list:", numbers)
print("Prime numbers:", prime_numbers)