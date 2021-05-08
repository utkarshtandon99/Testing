if __name__ == "__main__":
    s = input().split(" ")
    s.sort(key=len)
    print("method 1: ", s[0])
    #T.C. = O(N.logN)

    l = 10000
    ans = ""
    for i in s:
        if(len(i) < l):
            l = len(i)
            ans = i
    print("method 2: ", ans)
    #T.C. = O(N)