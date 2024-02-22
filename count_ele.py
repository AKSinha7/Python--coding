def count_frequency(numbers):
    frequency={}
    for num in numbers:
        if num in frequency:
            frequency[num] +=1
        else:
            frequency[num]=1
    return frequency

#Test the function
nums = [1,2,3,4,5,6,7,6,5,4,,6,7,8,9,1,23,54,6,6]
frequency_count=count_frequency(numn
print(frequency_count)