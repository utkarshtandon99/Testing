"""
Check if there exist two elements in an array whose sum is equal to the sum of rest of the array.
"""
if __name__ == "__main__":
    arr = [2, 11, 5, 1, 4, 7]
    sarr = sum(arr)
    s = set()
    if(sarr%2 == 1):
        print(False)
        exit()
    sarr /= 2
    for i in range(len(arr)):
        rem = sarr - arr[i]
        if(arr[i] not in s):
            s.add(arr[i])
        if(rem in s):
            print(arr[i], " ", int(rem))
            exit()
    print(False)
    
"""
[1, 2, 3, 4, 6]       -->     2 6
[2, 11, 5, 1, 4, 7]   -->     11 4
[2, 4, 2, 1, 11, 15]  -->     False

"""
