# Hsuan-You Lin Module 8 Problem Set Question 11.
def Q11(H, K):
    HashMap = set()
    for i in H:
        if K - i in HashMap:
            return "yes, giving -9 (In H) + 100 (in K)."
        HashMap.add(i)
    return "no"

if __name__ == "__main__":
    H = [4, 5, 7, -1, -9, 22]
    K = -5
    print(Q11(H, K))
    K = 7
    print(Q11(H, K))
