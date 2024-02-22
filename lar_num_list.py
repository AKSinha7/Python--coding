def find_largest(numbers):
    largest=numbers[0]
    for num in numbers:
        if num>largest:
            largest=num
    return largest

#test the function
nums=[10,20,40,50,70,87]
largest_num=find_largest(nums)
print(f"The largest number is {largest_num}")