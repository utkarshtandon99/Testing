if __name__ == "__main__":
    s = str(input())
    revs = "".join(reversed(s))
    c = 0
    for m in range(len(s)):
        if(s[m] != revs[m]):
            c+=1
    print(c)

