# Hsuan-You Lin Module 11 Problem Set Question 4.
def maxSubArray(nums):
    n = len(nums)
    max_sum = nums[0]
    min_sum = 0
    max_idx = min_idx = 0
    
    curr_sum = nums[0]
    for i in range(1, n):
        if curr_sum < min_sum:
            min_sum = curr_sum
            min_idx = i
            
        curr_sum += nums[i]
        if curr_sum> max_sum:
            max_sum = curr_sum
            max_idx = i
            
    return nums[min_idx : max_idx+1]

if __name__ == "__main__" :
    # nums = [-2, 1, -3, 7, -2, 2, 1, -5, 4]
    nums = [5, 15, -30, 10, -5, 40, 10]
    ans = maxSubArray(nums)
    print("Input: ", nums)
    print("Output: ", ans)
