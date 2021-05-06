memo = {}
def tarSum(target, numbers):
    if(target in memo):
        return(memo[target])
    if(target == 0):
        return True
    if(target < 0):
        return False
    for n in numbers:
        remainder = target - n
        if(tarSum(remainder,numbers) == True):
            memo[target] = True
            return True
    memo[target] = False
    return False

if __name__ == "__main__":
    print(tarSum(300, [7,14,101,8]))
    