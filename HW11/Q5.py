# Hsuan-You Lin Module 11 Problem Set Question 5.
def Q5_1(wordlist,word):
    dic = {}
    for i in range(len(wordlist)):
        for j in range(i, len(wordlist)):
            dic[wordlist[i: j+1]] = dic.get(wordlist[i: j+1], 0) + 1
    
    if word in dic:
        return True
        
    return False

def dict(word):
    dictionary = [ "it", "was", "the", "best", "of", "times", "it", "it", "was", "the", "worst"]
    size = len(dictionary)
    for i in range(size):
        if (dictionary[i] == word):
            return True
            
    return False
    
def Q5_2(worldlist):
    dp = [0 for i in range(len(worldlist))]
    dp_index = len(worldlist)-1
    dp1_index = []
    ans = []
    for i in range(len(worldlist)):
        for j in range(i):
            if dict(worldlist[: i+1]):
                dp[i] = i
            if dp[j] != 0 and dict(worldlist[j+1: i+1]):
                dp[i] = j
    
    while dp_index != dp[dp_index]:
        dp1_index = dp[dp_index]
        ans.append(worldlist[dp1_index+1: dp_index+1])
        dp_index = dp1_index
    ans.append(worldlist[: dp_index+1])
    ans.reverse()
    
    return ans

if __name__ == "__main__" :
    wordlist = "itwasthebestoftimesitwastheworst"
    ans = Q5_2(wordlist)
    print("Input: ", wordlist)
    print("Output: ", ans)
