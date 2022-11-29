# Hsuan-You Lin Module 8 Problem Set Question 8.

if __name__ == "__main__":
    hashMap = [[] for _ in range(11)]
    nums = [12, 14, 34, 88, 23, 94, 11, 39, 20, 16, 5]
    for num in nums:
        key = (2 * num + 5) % 11
        hashMap[key].append(num)
        print("\nAfter hash:", hashMap)
