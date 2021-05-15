"""
Given an array of positive integers. 
All numbers occur an even number of times except one number which occurs an odd number of times. 
Find the number in O(n) time & constant space.

Note: XOR of two elements is 0 if both elements are the same 
and the XOR of a number x with 0 is x.
"""

if __name__ == "__main__":
    arr = [1, 1, 3, 1, 2, 3, 2, 3, 3, 1]
    res = 0
    for i in range(len(arr)):
        res ^= arr[i]
        print(i, " - ", res)
    print(res)

"""
0  -  1
1  -  0
2  -  3
3  -  2
4  -  0
5  -  3
6  -  1
7  -  2
8  -  1
1
 
from collections import Counter
if __name__ == "__main__":
    counter = Counter(arr)
    print(counter)
    for i in range(len(arr)):
        if(counter[arr[i]] % 2 == 1):
            print(arr[i])
            exit()
    print("All number occur even times") 
"""