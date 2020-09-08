'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here

    new_array = []
    #make variables to create range of inner loop
    k_start = 0
    k_end = k-1

    #make sure we are not at the end of the array
    while k_end < len(nums):
        maximum = nums[k_start]
        #we use the range of k so we are limited to those 3 items
        for i in range(k_start, k_end +1):
            #loop through to find biggest number
            if nums[i] > maximum:
                maximum = nums[i]
        #append biggest number to the new array
        new_array.append(maximum)
        #increment inner loop's range to move over by 1 until we reach the end
        k_start += 1 
        k_end += 1
    #return new array which contains max nums
    return new_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
