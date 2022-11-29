from collections import defaultdict as DF
import bisect # If you want to use insertion sort, you can use bisect.insert()

# Creat Jumble hash-map to put sorted words
Jumble = DF(list)

def GroupJumbles(Words):
    for i in Words:
        # Take letters from list words and sorting
        Letter = str(sorted(i))
        Jumble[Letter].append(i)
        
    for Letter in Jumble:
        print("Jumbles:")
        print(" ".join(Jumble[Letter]))
        
Words = ["racing", "secura","saucer", "caring", "random"]
GroupJumbles(Words)