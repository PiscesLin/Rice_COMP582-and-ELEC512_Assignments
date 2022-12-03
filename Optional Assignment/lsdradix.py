# Hsuan-You Lin_hl116_Optional Assignment
# Implement LSB radix sort for strings

import sys

def lsb_radix(data):
    length = None
    if not length:
        value = (max(data, key = len))
        length = len(value)
    for num in range(length - 1, -1, -1):
        sorted_output = sort_string(data, num)

    return sorted_output

def sort_string(data, num):
    output_array   = [0] * len(data)
    count_arr    = [0] * (39)

    for key in data:
        letter = get_letters(num, key)
        count_arr[letter] += 1

    for i in range(len(count_arr) - 1):
        count_arr[i + 1] += count_arr[i]

    for key in reversed(data):
        letter = get_letters(num, key)
        output_array[count_arr[letter] - 1] = key
        count_arr[letter] -= 1

    return output_array

def get_letters(num, key):
    if num < len(key):
        if key[num] == " ":
            letter = 0
        elif key[num] == "\x00":
            letter = 1
        elif key[num].isdigit():
            letter = ord(key[num]) - ord('/')
        else:
            letter = ord(key[num]) - ord('T')
    else:
        letter = 2
    return letter
    
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
