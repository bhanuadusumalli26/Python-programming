#nested for loop
list_fruits=['mango','apple','grapes','banana']
for fruit in list_fruits:
    for i in fruit:
        print(i,end=" @ ")
    print()


color=['red','green','blue']
items=['apple','veggies','shirt']
for x in color:
    for y in items:
        print(x,y)
        print('')

#print right triangle
for i in range(11):
    for j in range(i):
         print("*",end=" ")
    print(' ')
 
#print right triangle using while loop   
i=11
while(i>0):
    j=11
    while(j>i):
        print("*",end=" ")
        j=j-1
    i=i-1
    print()
 
#append 2 lists
list1=[10,20,40]
list2=[30,50,70]
result=[]
for i in list1:
    for j in list2:
        result.append(i+j)
print(result)   

#multiplying 2 lists
list1=[2,3,4]
list2=[5,6,7]
result=[]
for i in list1:
    for j in list2:
        result.append(i*j)
print(result)

#Continue Statement
list1=[2,3,4]
list2=[2,3,4]
for i in list1:
    for j in list2:
        if i==j:
            continue
        print(i,'*',j,'=',i*j)
        
#perfect number
a=1
while a<=100:
    y_sum=0
    for i in range(1,a):
        if a%i==0:
            y_sum+=i
    if y_sum==a:
        print("perfect number:",a)
    a=a+1

fruits=['apple','orange','kiwi']
for fruit in fruits:
    count=0
    while count<6:
        print(fruit,end=" ")
        count=count+1
    print()