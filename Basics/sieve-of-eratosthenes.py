def soe(n):
    lst = [*range(2, n+1)]  #method to create list with range
    p = 2
    while(p*p <= n):
        for j in range(p*p, n+1, p):
            if(j in lst):
                lst[lst.index(j)] = -1
        p+=1
    lst.sort(reverse=True)
    ind = lst.index(-1)
    return(lst[:ind])

if __name__ == "__main__":
    while True:
        n=input()
        if(n == 'Q' or n == 'q'):
            exit()
        n = int(n)
        print(soe(n))