
i=0
while i<10:
    i=i+1
    print(i,end="#")
    print()
#basic while condition
count=0
while count<=5:
    print("The condition is true")
    count+=1
print("End of loop")

#print input of user  upto the cpmdition is false 
while True:
     print("please type your name")
     name=input()
     if name=="bhanu":
         break
print("Thank You ,you typed the correct name.")
     
#lcm of 4 and 7
x=0
while True:
    x+= 1
    if not(x%4 or x%7):
        break
print(x,'is divisible by both 4 and 7')   

#continue statement
i=0
while i<=10:
    i+=1
    if i==6:
        print("skipped")
        continue
    print(i)


#Else statement
i=1
while i<5:
    print(i)
    i+=1
else:
    print("i is not less than 5")

#popping elements in the list
a=[1,2,3,4,5,6,7,8,9]
while a:
    print(a.pop())
else:
    print("There are no elements in the list")
  
#average of positive numbers
num=0
count=0
sum=0
while num>=0:
    num=int(input("enter any positive number: "))
    if num>0:
        count+=1
        sum+=num
avg=sum/count
print("Total sum of numbers:" ,sum, 'Average:',avg)

#Guessing game in python
import random
n=random.randint(1,100)
print(n)
guess=int(input("enter an integer between 1to 100: "))
while n!= 'guess':
    if guess<n:
        print("Your guess is low")
        guess=int(input("enter an integer between 1to 100: "))
    elif guess>n:
        print("Your guess is High")
        guess=int(input("enter an integer between 1to 100: "))
    else:
        print("You Won!")
        break
    print()


