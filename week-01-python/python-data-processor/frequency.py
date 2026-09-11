def count_frequency(numbers):

    frequency = {}

    for num in numbers:

        if num in frequency:
            frequency[num] += 1

        else:
            frequency[num]=1
    return frequency
        
               


numbers = [10, 20, 10, 30, 20, 10]
print(count_frequency([10, 20, 10, 30, 20, 10]))
print(count_frequency([]))
print(count_frequency([5]))
print(count_frequency([1, 1, 1, 1]))
