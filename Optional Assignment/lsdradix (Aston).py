# Implement LSB radix sort for strings
import sys

def count_sort_letters(array, size, col, base, max_len):
  # """ Helper routine for performing a count sort based upon column col """
    output   = [0] * size
    count    = [0] * (base + 13) # 1 addition cell to account for dummy letter, 1 for space, 1 for '\x00', 10 for number zero to nine
    alp_base = ord('a') - 13 
    num_base = ord('0') - 1 # 1 addition cell for '\x00'

    for item in array: # generate Counts
        # get column letter if within string, else use dummy position of 0
        if col < len(item):
            if item[col] == " ":
                letter = 0
            elif item[col] == '\x00':
                letter = 1
            elif item[col].isdigit():
                letter = ord(item[col]) - num_base
            else:
                letter = ord(item[col]) - alp_base
        else:
            letter = 2
        # letter = ord(item[col]) - min_base if col < len(item) else 1
        count[letter] += 1

    for i in range(len(count)-1):   # Accumulate counts
        count[i + 1] += count[i]

    for item in reversed(array):
        # Get index of current letter of item at index col in count array
        if col < len(item):
            if item[col] == " ":
                letter = 0
            #  if item[col] is null character \x00 then use dummy position of 0
            elif item[col] == '\x00':
                letter = 1
            elif item[col].isdigit():
                letter = ord(item[col]) - num_base
            else:
                letter = ord(item[col]) - alp_base
        else:
            letter = 2
        # letter = ord(item[col]) - min_base if col < len(item) else 1
        output[count[letter] - 1] = item
        count[letter] -= 1

    return output


def lsb_radix(array, max_col = None):
    if not max_col:
        max_col = len(max(array, key = len)) # edit to max length

    for col in range(max_col-1, -1, -1): # max_len-1, max_len-2, ...0
        array = count_sort_letters(array, len(array), col, 26, max_col)

    return array
#
# Run your program as follows:
#
#    python3 lsdradix.py < SOME_TEST_INPUT_FILE
#
# Output will be printed to your screen
#
if __name__ == '__main__':
    for l in lsb_radix([l[:-1] for l in sys.stdin.readlines()]):
        print(l)