# Hsuan-You Lin Module 10 Problem Set Question 1.
def counting_Sort(nums):
    numDict = dict()
    for i in range(len(nums)):
        currNum = nums[i]
        if currNum not in numDict:
            numDict[currNum] = 0
        numDict[currNum] += 1

    numList = list(numDict.keys())
    numList.sort()

    for i in range(1, len(numList)):
        lastNum, currNum = numList[i - 1], numList[i]
        numDict[currNum] += numDict[lastNum]

    result = [None] * len(nums)

    for num in nums:
        index = numDict[num] - 1
        numDict[num] -= 1
        result[index] = num
    return result

if __name__ == "__main__" :
    arr = [4, 2, 2, 8, 3, 3, 1]
    results = counting_Sort(arr)
    print(results)