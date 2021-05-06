def diamond(n):
    ans, ans1, ans2 = "", "", ""
    for i in range(n):
        ans1 += "* "*(n-i)
        ans2 += "* "*(n-i)
        for _ in range(2*(i)):
            ans += "  "
        print(ans1 + ans + ans2)
        ans, ans1, ans2 = "", "", ""
        
    for i in range(n):
        ans += "* "*(i+1)
        ans2 += "* "*(i+1)
        for _ in range(2*(n-i-1),0,-1):
            ans1 += "  "
        print(ans + ans1 + ans2)
        ans1, ans, ans2 = "", "", ""

def christmastree(n):
    ans, ans1 = "", ""
    c = n
    space = c*4
    a = 0
    for _ in range(1, n+1):
        for i in range(a, c):
            ans += " "*(space-i)
            for _ in range(i+1):
                ans1 += "* "
            print(ans + ans1)
            ans, ans1 = "", ""
        a += 2
        c += 2
    for i in range(n):
        print(" "*((n*4)-3) + "* "*4)

def arrow(n):
    ans, ans1 = "", ""
    for i in range(n):
        ans += " "*(n-i)
        for _ in range(i+1):
            ans1 += "* "
        print(ans + ans1)
        ans, ans1 = "", ""
    for i in range(n):
        print(" "*(n) + "*")

if __name__ == "__main__":
    while True:
        print("1. Diamond:\n2. Christmas Tree:\n3. Arrow:")
        c=input()
        if(c == '1'):
            print("N:")
            n=int(input())
            print(diamond(n))
        elif(c == '2'):
            print("N:")
            n=int(input())
            print(christmastree(n))
        elif(c == '3'):
            print("N:")
            n=int(input())
            print(arrow(n))
        if(c == 'Q' or c == 'q'):
            exit()