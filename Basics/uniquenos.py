"""
Given an array of numbers, print the unique numbers in it in
the decreasing order of frequency of those numbers.
"""
if __name__ == "__main__":
    arr = [1, 3, 1, 2, 3, 2, 3, 3, 1, 4, 4, 4, 4, 4]
    freq = {}
    for n in arr:
        if(n in freq):
            freq[n] += 1
        else:
            freq[n] = 1
    d = {k:v for k,v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
    print(d)
    l = d.keys()
    print(*l)   # print list without brackets and commas

"""
{4: 5, 3: 4, 1: 3, 2: 2}
4 3 1 2
"""
