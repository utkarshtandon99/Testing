def shrtstdir(s):
    xcoord,ycoord=0,0
    s = s.lower()
    for i in range(0, len(s)):
        if(s[i] == 'n'):
            ycoord+=1
        if(s[i] == 's'):
            ycoord-=1
        if(s[i] == 'e'):
            xcoord+=1
        if(s[i] == 'w'):
            xcoord-=1
    x,y=0,0
    dist = abs(xcoord) + abs(ycoord)
    print(dist)
    ans=""
    while(x > xcoord):
        ans += "W"
        x-=1
    while(x < xcoord):
        ans += "E"
        x+=1
    while(y > ycoord):
        ans += "S"
        y-=1
    while(y < ycoord):
        ans += "N"
        y+=1
    return(ans)
if __name__ == "__main__":
    while True:
        n=input()
        if(n == 'Q' or n == 'q'):
            exit()
        print(shrtstdir(n))