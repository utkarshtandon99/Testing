#Decimal Equivalent is:     1*inpt[len-1] + base*inpt[len-2] + (base)2*inpt[len-3] + ...
#Example:   n = 11A, b = 16; DEC = 282(256 + 16 + 10 = 16^2 * 1 + 16^1 *1 + 16^0 * 10)
def btd(n,b):
    ans = 0
    s = str(n)
    b = int(b)
    slen = len(s)
    for i in range(slen-1,-1,-1):
        x = conv(s[i])
        if(x < b):
            ans += (b**(slen - i - 1)) * x
    return(ans)

def conv(n):
    if(n.isalpha()):
        val = ord(n) - ord('A') + 10
        return(val)
    return(int(n))

def conv_letter(n):
    val = chr(n - 10 + ord('A'))
    return(val)

#Base Equivalent is:        Divide by base and use the remainder.
def dtb(n,b):
    n = int(n)
    b = int(b)
    ans = ""
    while(n > 0):
        mod = n % b
        if(mod >= 10):
            mod = conv_letter(mod)
        ans += str(mod)
        n //= b
    return("".join(reversed(ans)))


if __name__ == "__main__":
    while True:
        print("1. Base to Decimal:\n2. Decimal to Base:")
        c=input()
        if(c == '1'):
            print("Enter Number:")
            n=input()
            print("Enter Base:")
            b=input()
            print(btd(n,b))
        elif(c == '2'):
            print("Enter Decimal:")
            n=input()
            print("Enter Base to covert to:")
            b=input()
            print(dtb(n,b))
        if(c == 'Q' or c == 'q'):
            exit()