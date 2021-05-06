memo = {}
def howSum(target, numbers):
    if(target in memo):
        return(memo[target])
    if(target == 0):
        return []
    if(target < 0):
        return None
    
    shortestCombination = None

    for n in numbers:
        remainder = target - n
        result = howSum(remainder, numbers)
        if(result != None):
            combination = [n, *result]
            memo[target] = combination
            if(shortestCombination == None or len(combination) < len(shortestCombination)):
                shortestCombination = combination
    memo[target] = shortestCombination
    return shortestCombination

if __name__ == "__main__":
    print(howSum(200, [1,4,5,7,8,21]))
