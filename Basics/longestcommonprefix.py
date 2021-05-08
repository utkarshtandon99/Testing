if __name__ == "__main__":
    s = ["coincidence", "coincidance", "coincidonce", "coincidunce"]
    n = len(s)
    minlen = len(s[0])
    for i in range(n):
        if(len(s[i]) < minlen):
            minlen = len(s[i])
    ans = ""
    for i in range(minlen):
        for j in range(1, n):
            if(s[j][i] !=  s[0][i]):
                print(ans)
                exit()
        ans += s[j][i]
    print(ans)
    
