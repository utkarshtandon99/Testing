if __name__ == "__main__":
    s = str(input()).lower()
    vowels = "aeiou"
    s1, s2, vowelstillnow = [], [], 0
    tot_vowels = [each for each in s if each in vowels]
    total = len(tot_vowels)
    if(total % 2 != 0 or total == 0):
        print("No")
        exit()
    for i in range(len(s)):
        if(s[i] in vowels):
            vowelstillnow += 1
        if(total/2 == vowelstillnow):
            print(s[:i+1])
            print("Yes")
            exit()
""" 
#Dictionary method of counting each vowel in string:
    string = "CoIncedencE"
    vowels = "aeiou"

    #.casefold() is used to ignore case for Unicode input.
    #Generally casefold is suitable when input can be from languages other than english.
    string = string.casefold()
    print(string)

    #Forms a dictionary with key as a vowel and the value as 0
    count = {}.fromkeys(vowels, 0)

    # To count the vowels
    for character in string:
        if character in count:
            count[character] += 1   
    print(count)
    #print(sum(count.values())) --> To sum valules in dict
    #output: {a:0, e:3, i:1, o:1, u:0}
"""

