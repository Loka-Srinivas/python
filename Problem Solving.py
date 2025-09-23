# 22/08/2025
# Task:- Problem Sloving


# # Find a factorial of a given number, by using input must be passed using input()

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
    print("The factorial of", num, "is", fact)
    
    
    
# #Print fibonacci series upto the value num pass num value, using input()
    
num=int(input("enter a value:"))
a=0
b=1
for i in range(num):
    print(a) 
    a,b=b,a+b   
    
    
    
# #Check weather a number is perfect square or not, use input()    

num = int(input("Enter a number: "))

a = int(num ** 0.5)

if a * a == num:
    print(num, "is a perfect square",a)
else:
    print(num, "is not a perfect square")


# #Print sum of digits of a number,use input()

# #Example:- num=123 then sum=6


num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print(sum)



# #Find the count number of digits in a number
# #Eample:- num=156 then count=3

num = int(input("Enter a number: "))
count = 0
while num > 0:

    num //= 10
    count += 1
print("the count of", count)


# #Print reverse of a number, use input()


num=int(input("enter a number:"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)  



# #Check whether a given number is palindrome or not, use input()


num = int(input("Enter a number: "))
temp = num  
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")







