"""Question:
You are given a binary matrix (can have only 1s and 0s as elements) with n rows and m columns initially consisting of all 0s. 
Q queries follow. The queries can be of 4 types:
1 R index
1 C index
2 R index
2 C index
In each query, the first input is the type of the query, the second input is whether we have to consider the row (R) or the column (C) and the third input is the index of the row/column. 
For each type 1 query, we need to flip the elements of the row/column having the given index. 
For each type 2 queries, we have to output the number of zeros present in the row/column having the given index.
"""

def flip_row(ind, mat):
    for i in range(len(mat[ind])):
        mat[ind][i] ^= 1
    return(mat)

def flip_col(ind, mat):
    for i in range(len(mat)):
        mat[i][ind] ^= 1
    return(mat)

def countrowzeros(ind, mat):
    return(mat[ind].count(0))

def countcolzeros(ind, mat):
    count = 0
    for i in range(len(mat)):
        if(mat[i][ind] == 0):
            count+=1
    return(count)

if __name__=="__main__":
    print("Enter number of rows:")
    r = int(input())
    print("Enter number of columns:")
    c = int(input())
    mat = [([0]*c) for i in range(r)]
    print(mat)
    print("Enter number of queries:")
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(input().split(" ")))
        print(query[i])
        if(int(query[i][0]) == 1):
            if(query[i][1] == 'r'):
                mat = flip_row(int(query[i][2]), mat)
                print("After flip row: ", mat)
                continue
            mat = flip_col(int(query[i][2]), mat)
            print("After flip col: ", mat)
        else:
            if(query[i][1] == 'r'):
                count = countrowzeros(int(query[i][2]), mat)
                print("Zeros in row: ", count)
                continue
            count = countcolzeros(int(query[i][2]), mat)
            print("Zeros in col: ", count)

"""

Example input and output -

    Enter number of rows:
    4
    Enter number of columns:
    3
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    Enter number of queries:
    3
    1 r 3
    ['1', 'r', '3']
    After flip row:  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 1, 1]]
    1 c 0
    ['1', 'c', '0']
    After flip col:  [[1, 0, 0], [1, 0, 0], [1, 0, 0], [0, 1, 1]]
    2 c 2
    ['2', 'c', '2']
    Zeros in col:  3



    Enter number of rows:
    4
    Enter number of columns:
    3
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    Enter number of queries:
    3
    1 r 2
    [['1', 'r', '2']]
    After flip row:  [[0, 0, 0], [0, 0, 0], [1, 1, 1], [0, 0, 0]]
    1 c 1
    [['1', 'r', '2'], ['1', 'c', '1']]
    After flip col:  [[0, 1, 0], [0, 1, 0], [1, 0, 1], [0, 1, 0]]
    2 r 2
    [['1', 'r', '2'], ['1', 'c', '1'], ['2', 'r', '2']]
    Zeros in row:  1

"""
    