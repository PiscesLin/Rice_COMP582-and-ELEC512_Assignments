# Hsuan-You Lin Module 11 Problem Set Question 4.
def maxSubArray(nums):
    dp = [0 for i in range(len(nums))]
    dp = nums[0]
    dp1 = 0
    dp2 = dp
    for i in range(0, len(nums)):
        if dp < dp2:
            dp = dp2
            dp_max_id = i
        if dp2 < dp1:
            dp1 = dp2
            dp_min_id = i
        dp2 += nums[i]
            
    subsequence = nums[dp_min_id : dp_max_id + 1]
    total = sum(nums[dp_min_id : dp_max_id + 1])
            
    return subsequence, total

if __name__ == "__main__" :
    nums = [5, 15, -30, 10, -5, 40, 10]
    ans = maxSubArray(nums)
    print("Input: ", nums)
    print("Output: ", ans[0])
    print("Sum of contiguous subsequence: ", ans[1])
