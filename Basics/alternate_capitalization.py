def alt_cap():
    str = "I am a boy who has 3 siblings"
    print(str)
    res = ""
    c=0
    for i in range(len(str)):
        if(str[i]==" " or str[i].isdigit()):
            res+=str[i]
            continue
        elif(c%2 == 0): #to check if string --> str[i].isalpha()
            res += str[i].upper()
            c+=1
        else:
            res += str[i].lower()
            c+=1
    print(res)
    return(res)

if __name__ == "__main__":
    res = alt_cap()
    ans = "I aM a BoY wHo HaS 3 sIbLiNgS"
    if(res == ans):
        print(True)