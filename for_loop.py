# Use for loop in a String
S= "bhanu"
for i in S:
    print(i)
#Using end operator to print side by side
a="bhanu"
for i in a:
    print(i,end=" ")
#Use for loop in a list
programming=["python","java","HTML","C++"]
for i in  programming:
    print(i)
#Find the avg of a list of numbers
list_num=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in list_num:
    sum+=i
print("sum=:",sum)
print("average:",sum/len(list_num))
#for  loop using a tuple
tuple=(1,2,3,4,5,6,7,8,9)
sum=0
for i in tuple:
    sum+=i
print("sum:",sum)
print("average:",sum/len(tuple))
#for loop using range function
for i in range(1,10):
    print(i,end=" ")
#stepping
for i in range(0,16,2):
    print(i,end="")
#program to print table of a given number
n=int(input("enter the number"))
for i in range(1,11):
    mul=n*i
    print(n,"*",i,"=",mul)
#printing values in list by using range function
list2=["java","python","c++","HTML","CSS"]
for i in range(len(list2)):
    print(list2[i])
#NESTED FOR LOOP
companies=["Google","Apple","PWC","Uber"]
for i in companies:
    print("We will display each letter of"+i)
    for letter in i:
        print(letter)

#For Loop With else Clause
for i in range(0,10,3):
    print(i)
else:
    print("The Loop has completed execution")
#Break Statement
for i in range(1,10):
    if(i==6):
        break
    print(i)
#Continue Statement
for i in range(1,10):
    if(i==6):
        print("skipped")
        continue
    print(i)

#Program to display the total goals a player has  scored

player_name="Caremelo"
goals={'Edison':14,'Caremelo':15,'bhanu':20}
for player in goals:
    if(player==player_name):
        print(goals[player])
        break
else:
    print("No player with that name Found")    

#cube of number
num=[2,5,7,4,8,6]
cube=[]
for i in num:
    cube.append(i**3)
print(cube)

#pattern printing
n=int(input("enter the number of rows"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()
  