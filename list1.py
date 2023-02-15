#My first list
numbers = (45,87,90,24)
len(numbers)#get the length of my list

for i in range(len(numbers)):
    print(numbers[i])
#List methods

#index
print(numbers.index(90))

#Append - adds an element to the end of a list
#before appending
for i in range (len(numbers)):
    print(numbers[i])

print("\n")
numbers.append(90)

 #after appending   
for i in range(len(numbers)):
    print(numbers[i])

#count - returns the number of times
#an element occurrs in a list
print(numbers.count(87))

#pop - removes an element at a given index
#and returns that element
print(numbers.pop(2))

#Insert - inserts an element x at an index y
numbers.insert(2, 100)

for i in range (len(numbers)):
    print(numbers[i])

#Remove - removes the first occurrence of an
#element from the list

numbers.remove(87)

#Sort - arranges/sorts the list in ascending order
for i in range(len(numbers)):
    print(numbers[i])

#sort the list
numbers.sort()

#add a new line of formatted output
print("\n")
for i in range(len(numbers)):
    print(numbers[i])

#Tips and tricks

#multiplying a list
zeros = [0]*10
zeros

ones = [1]*5
ones

#Adding a list
list1 = [86,90]
list2 = [76,40]
final_list = list1 + list2

#Slicing a list
numbers = [23, 45, 78, 42]
numbers[2:]
[78,42]

#Get the max value in a list
max[numbers]

#Creating lists
numbers = []#empty list
for i in range(10):
    #Insert elements into the list
    numbers.append(i)

for i in range(len(numbers)):
    print(numbers[i])
