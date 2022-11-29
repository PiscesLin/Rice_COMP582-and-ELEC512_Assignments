# Hsuan-You Lin Module 8 Problem Set Question 9.
def Q9(H, J, K):
    HashMap = set(H)
    for i in J:
        if K - i in HashMap:
            return "yes, giving -9 (In H) + 100 (in K)."
    return "no"

if __name__ == "__main__":
    H = [4, 5, 7, -1, -9, 22]
    J = [0, -5, 10, 44, 100, -12]
    K = 91
    print(Q9(H, J, K))
    K = 92
    print(Q9(H, J, K))
