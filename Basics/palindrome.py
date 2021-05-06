def palindrome(n):
    s = str(n)
    s = s.lower()
    if(len(s) == 1):
        return(True)
    for i in range(len(s)//2):
        if(s[i] != s[len(s) - i - 1]):
            return(False)
    return(True)
if __name__ == "__main__":
    while True:
        n=input()
        if(n == 'Q' or n == 'q'):
            exit()
        print(palindrome(n))