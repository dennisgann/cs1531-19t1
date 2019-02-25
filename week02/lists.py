'''
The most versatile data structure, written as a list of comma separated values within square brackets. Lists might contain items of the same or different data types, e.g.,

 - primes = [2,3,5,7,11,13]
 - mixed_basket = [1,[apples,3,3.45],2,[oranges,4.05]]

Given a list of numbers find the median of the numbers. You may assume that the input list contains at least one number.

Think about why you many want to use sorted(numbers) instead of numbers.sort()
1,2,3
median = 2

1,2,3,4
median = 2.5
(2+3) / 2
indeces: 1,2

'''
numbers = [2, 4, -23, 2, 95, 21]

def median(num_array):
    sorted_nums = sorted(num_array)
    middle1 = (len(sorted_nums) - 1) // 2
    middle2 = len(sorted_nums) // 2
    return (sorted_nums[middle1] + sorted_nums[middle2]) / 2

print(median(numbers))