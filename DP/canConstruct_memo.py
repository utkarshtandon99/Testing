memo = {}
def Construct(target, words):
    if(target in memo):
        return memo[target]
    if(target == ''):
        return True
    for w in words:
        if(target.startswith(w) == True):
            newTarget = target.replace(w,'')
            if(Construct(newTarget, words) == True):
                memo[target] = True
                return True
        else:
            continue
    memo[target] = False
    return False


if __name__ == "__main__":
    print(Construct('abcdef', ['ab','abc','cd','def','abcd']))
    print(Construct('skateboard', ['boar','bo','rd','ate','t','ska','sk']))
    print(Construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','f']))