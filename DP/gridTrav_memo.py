memo={}
def gridTravel(m, n):
    key = str(m) + ',' + str(n)
    if(key in memo):
        return(memo[key])
    if(m == 1 and n == 1):
        return(1)
    if(m == 0 or n == 0):
        return(0)
    memo[key] = gridTravel(m - 1, n) + gridTravel(m, n - 1)
    print(memo)
    return(memo[key])

if __name__ == "__main__":
    i = gridTravel(5,3)
    print(i)