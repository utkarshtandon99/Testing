memo = {}
def howSum(target, numbers):
    if(target in memo):
        return(memo[target])
    if(target == 0):
        return []
    if(target < 0):
        return None
    for n in numbers:
        remainder = target - n
        result = howSum(remainder, numbers)
        if(result != None):
            memo[target] = [n, *result] #used splat(*) operator to add number to existing list
            return(memo[target])
    memo[target] = None
    return None

if __name__ == "__main__":
    print(howSum(300, [13,7,14]))
