"""
Write a function that takes in an array of at least three integers and, without sorting the input array, 
returns a sorted array of the three largest integers in the input array.
The function should return duplicate integers if necessary; 
For example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12]
"""
def findThreeLargestNumbers(array):
    # Write your code here.
    import math
    first_greatest_num = second_greatest_num = third_greatest_num = -math.inf

    """
    iterate the array with a while loop
    if current element is greater than any of the 3 nums, assign it to the appropriate greatest num
    """
    for num in array:
        if num > third_greatest_num:
            if num > second_greatest_num:
                if num > first_greatest_num:
                    third_greatest_num = second_greatest_num
                    second_greatest_num = first_greatest_num
                    first_greatest_num = num
                else:
                    third_greatest_num = second_greatest_num
                    second_greatest_num = num
            else:
                third_greatest_num = num

        # print([third_greatest_num, second_greatest_num, first_greatest_num])
    
    return [third_greatest_num, second_greatest_num, first_greatest_num]

three_largest_nums = findThreeLargestNumbers([10, 5, 9, 10, 12])
print(three_largest_nums)
