# Hsuan-You Lin Module 11 Problem Set Question 5.

def dict(word):
    dictionary = [ "it", "was", "the", "best", "of", "times", "it", "it", "was", "the", "worst"]
    size = len(dictionary)
    for i in range(size):
        if (dictionary[i]== word):
            return True
    return False

def check_reconstitution(s):
    n = len(s)
    is_valid = [False for _ in range(n)]
    for i in range(n):
        for j in range(i):
           if is_valid[j] and dict(s[j+1:i+1]):
               is_valid[i] = True
        if dict(s[:i+1]):
           is_valid[i] = True
    return is_valid[n-1]
    
    
def get_reconstitution(s):
    source = [-1 for _ in range(len(s))] # previous source
    for i in range(len(s)):
        for j in range(i):
            if source[j] != -1 and dict(s[j+1:i+1]):
                source[i] = j
            if dict(s[:i+1]):
                source[i] = i
    result = []
    curr_idx = len(s)-1
    while curr_idx != source[curr_idx]:
        prev_idx = source[curr_idx]
        result.append(s[prev_idx+1:curr_idx+1])
        curr_idx = prev_idx
    result.append(s[:curr_idx+1])
    result.reverse()
    return result

if __name__ == "__main__" :
    wordlist = "itwasthebestoftimesitwastheworst"
    ans = get_reconstitution(wordlist)
    print("Input: ", wordlist)
    print("Output: ", ans)
