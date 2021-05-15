"""
Find the maximum no. of elements in a given positive integer
array such that their sum is less given number k.
"""

if __name__ == "__main__":
    arr = [3,4,7,2,6,5,1,1]
    k = 8
    arr.sort()
    n = len(arr)
    s, count, res = 0, 0, []
    for i in range(n):
        s += arr[i]
        if(s >= k):
            count = i
            break
        res.append(arr[i])
    print(res)
# [1, 1, 2, 3]