if __name__ == "__main__":
    s = input().lower().split(" ")
    pre = str(input()).lower()
    f = -1
    for i in s:
        if(pre == i[:len(pre)]):
            print(True)
            f = 1
            exit()
    print(f)