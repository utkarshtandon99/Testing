"""Sqrt without using library functions"""

if __name__ == "__main__":
    i = 1
    n = 30
    flag = 0
    while(i*i <= n):
        if(i*i == n):
            print(i)
            flag = 1
            exit()
        i+=1
    low = i-1
    high = i
    # Binary Search between i-1 and i
    while(low <= high):
        mid = (low + high)/2
        sq = mid*mid
        if((sq == n) or (abs(sq - n) < 0.00001)):
            print("{0:.5f}".format(mid))    # Format output to max 5 decimal places
            exit()
        elif(sq < n):
            low = mid
        else:
            high = mid

# 5.47723