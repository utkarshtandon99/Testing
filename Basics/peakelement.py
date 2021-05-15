"""Find the greatest peak element in the array"""

def checkmax(x, max):
    if(x > max):
        max = x
    return(max)

def maxpeak(arr, n):
    max = 0
    if(n == 1 or n == 2):   #if len(arr) is 1 or 2, then does not exist
        print("Does not exist")
        exit()
    if(arr[0] > arr[1] and arr[0] > arr[n-1]):
        max = checkmax(arr[0], max)
    if(arr[n-1] > arr[n-2] and arr[n-1] > arr[0]):
        max = checkmax(arr[n-1], max)
    for i in range(1, n-1):
        if(arr[i] > arr[i-1] and arr[i] > arr[i+1]):
            max = checkmax(arr[i], max)
    print("Max peak element: ", max)

def binary(arr, n):
    low = 0
    high = n-1
    mid = 0
    ele = 0
    while(low <= high):
        mid = low + (high - low)/2
        mid = int(mid)
        if((mid == 0 or arr[mid-1]<arr[mid]) and (mid == n-1 or arr[mid+1]<arr[mid])):
            ele = checkmax(arr[mid], ele)
            print("Using binary search method: ", ele, " (Not max)")
            break
        elif(arr[mid-1] > arr[mid]):
            high = mid - 1
        else:
            low = mid + 1



if __name__ == "__main__":
    arr = [10, 20, 25, 2, 23, 90, 120, 70, 80, 40, 110]    #120
    n = len(arr)
    maxpeak(arr, n)   # This approach is O(n) and can find max peak element in array. Answer = 120
    binary(arr, n)  # This approach cannot find max peak element, but can find a peak element in O(logn). Answer = 80

"""
Max peak element:  120
Using binary search method:  80  (Not max)
"""