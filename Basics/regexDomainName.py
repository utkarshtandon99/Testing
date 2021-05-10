import re

def isValidDomain(str):
 
    regex = "^((?!-)[A-Za-z0-9-]{1,63}(?!-)\\.)+[A-Za-z]{2,6}\\b([a-zA-Z0-9]*)"

    p = re.compile(regex)
 
    if (str == None):
        return False

    if(re.search(p, str)):
        return True
    else:
        return False

if __name__=="__main__":
    s = "google.com"    #true
    print(isValidDomain(s))
    s = "google.drive.mail.com"  #true
    print(isValidDomain(s))
    s = "2google1.com"  #true
    print(isValidDomain(s))
    s = "-google.com"   #false
    print(isValidDomain(s))
    s = "google-.com"   #true  
    print(isValidDomain(s))
    s = "google.m"      #false
    print(isValidDomain(s))
    s = ".com"          #false
    print(isValidDomain(s))
    s = "google.com-"   #false
    print(isValidDomain(s))
    s = "google.google.com/abc"   #true
    print(isValidDomain(s))
