#Creating list of even numbers
even_nums = []
for num in range (20):
    if (num%2) == 0:
        even_nums.append(num)
for i in range(len(even_nums)):#or for i in even_nums:
    print(even_nums[i])
    