#https://www.geeksforgeeks.org/generate-an-n-length-array-a-from-an-array-arr-such-that-arri-is-the-last-index-consisting-of-a-multiple-of-ai/
def soe(n):
    ans = [*range(2, n+1)]
    res = []
    p = 2
    while(p*p <= n):
        for i in range(p*p, n+1, p):
            if(i in ans):
                ans[ans.index(i)] = False
        p+=1
    for i in range(len(ans)):
        if(ans[i] == False):
            continue
        res.append(ans[i])
    return(res)

if __name__ == "__main__":
    print("Enter a large number (example = 50):")
    n=int(input())
    lsoe = soe(n)
    print(lsoe)
    while True:
        N = int(input())
        a = []
        A = [0]*N
        prime, j = 0, 0
        for i in range(N):
            a.append(int(input()))
        for i in range(N):
            if(A[i] != 0):
                continue
            elif(A[a[i]] != 0):
                A[i] = A[a[i]]
            else:
                prime = lsoe[j]
                A[i] = prime
                A[a[i]] = A[i]
                j += 1
        print(A)
        
"""Input: {4, 1, 2, 3, 4}
   Output: 2 3 5 7 2
   
   Input: {0, 1, 2, 3, 4}
   Output: 2 3 5 7 11
"""
