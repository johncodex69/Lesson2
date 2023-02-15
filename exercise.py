#Exercise 
# even_nums = [2, 4, 6, 8, 10]
# for num in range(20):
#     if(num % 2 == 0):
#         even_nums.append(4)

# for i in even_nums:
#     print(even_nums[i])

#Exercise 3
# nums = [8, 9, 10]
# nums[1] = 17
# nums. insert(4, 4)
# for i in range(len(nums)):
#     print(nums[i])
# nums. insert(5, 5)
# for i in range(len(nums)):
#     print(nums[i])
# nums. insert(6, 6)
# for i in range(len(nums)):
#     print(nums[i])

# nums.remove(8)
# print(nums)

# for i in range(len(nums)):
#     print(nums[i])
# nums.sort()
# print(nums)

# double = nums*2
# print(double)

# double.insert(3, 25)
# print(double)

#Exercise 2
#Write a program that generates a list of 20 random numbers btw 1 and 100

# from random import randint
# nums = []

# a)Create the list
for i in range(20):
    n = randint(0, 100)

    nums.append(n)

# b)Print the list
# for num in nums:
#     print(num)

# # c)Find the average of the list
# for num in nums:
#     sum += num

#Average = total/no. of items
#average = sum/len(nums)
# print(average)

# # d)Print the largest value
# nums.max()

# # e)Print the smallest value
# nums.min()

# # f)Second largest and second smallest
# #you have to sort the list
# nums.sort()

#second largest
# nums[1]
# #second smallest
# nums[len(nums) - 1]

# # g)Number of even values
# for num in nums:
#     if num % 2 == 0:    #Check whether it is using the modulo operator
#         count += 1

# #Count now contains number of even values on the list
# print(count)

