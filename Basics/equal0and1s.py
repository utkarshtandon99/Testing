"""
Divide array into max sets containing equal no of 1s and 0s
"""

if __name__ == "__main__":
    s = str(input())
    ct, c0, c1 = 0, 0, 0
    if(s.count('0') != s.count('1')):
        ct = -1
        print(ct)
        exit()
    for i in range(0, len(s)):
        if(s[i] == '0'):
            c0 += 1
        elif(s[i] == '1'):
            c1 += 1
        if(c0 > 0 and c1 > 0 and c0==c1):
            print(c0, c1)
            ct += 1
            c0, c1 = 0, 0
    print(ct)
 #input: 0100010101     output: -1
 #input: 0100110101     output: 4
 #input: 0111100001     output: 3
