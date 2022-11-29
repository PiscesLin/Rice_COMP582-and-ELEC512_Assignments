# Hsuan-You Lin Module 9 Problem Set Question 5.
import time
import heapq as hq
  
def update_priority(arr, new_element):
    i, j = 0, 0
    hq.heapify(arr)
    print(arr, "\n")
    while len(arr) != 0:
        print("The ", arr[0][1], " with priority ",
              arr[0][0], " in progress", end="")
      
        for _ in range(0, 5):
            print(".", end="")
            time.sleep(0.5)
        hq.heappop(arr)
      
        if j < len(new_element):
            hq.heappush(arr, new_element[j])
            print("\n\nNew element uptate:", new_element[j])
            print()
            j = j+1
      
        print("\n New Queue:", arr)
        print("\n")
      
    print("\nUpdate Priority Queue completed.")

if __name__ == "__main__" :
    arr = [(2, 'A'), (5, 'B'), (1, 'D'),
            (4, 'E'), (3, 'C'), (6, 'F')]
      
    new_element = [(1, 'B')]
    update_priority(arr, new_element)
