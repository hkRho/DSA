def create_table(n1, n2):
    '''
    Function for initializing/creating a table with specified numbers of columns and rows.
    The number of columns and rows are determined by n1 and n2.

    n1: length of pattern string
    n2: length of wildcard string
    '''
    table = {}
    row = [False for i in range(n2+1)]  # add 1 for the 0th row (empty space)
    
    for i in range(n1+1): # add 1 for the 0th column (empty space)
        table[i] = row
    
    return table


def match_wildcard(str, wildcard, n1, n2):
    '''
    Fuction to check whether a wildcard string can be modified to match the pattern string.

    str: pattern string
    wildcard: wildcard string
    n1: length of pattern string
    n2: length of wildcard string
    '''
    # initialize lookup table
    table = create_table(n1, n2)

    # base case
    table[0][0] = True

    # update the values for the 0th row
    for k in range(n2):
        if wildcard[k] == '*':
            table[0][k+1] = True
        else:
            table[0][k+1] = False

    # build lookup table
    for i in range(n1):
        for j in range(n2):
            
            # case when the letters are the same
            if str[i] == wildcard[j]:
                table[i+1][j+1] = True

            # case when there is an asterisk
            elif wildcard[j] == '*':
                table[i+1][j+1] = table[i+1][j] or table[i][j+1]
            
            # case when the letters are different
            elif str[i] != wildcard[j]:
                table[i+1][j+1] = False
            
            else:
                table[i+1][j+1] = False

    return table[n1][n2]
    

def test1():
    '''
    Test to check DP Solution - True
    '''
    s1 = ""
    s2 = "*"
    print(match_wildcard(s1, s2, len(s1), len(s2)))

def test2():
    '''
    Test to check DP Solution - True
    '''
    s1 = "ab"
    s2 = "a*"
    print(match_wildcard(s1, s2, len(s1), len(s2)))

def test3():
    '''
    Test to check DP Solution - True
    '''
    s1 = ""
    s2 = ""
    print(match_wildcard(s1, s2, len(s1), len(s2)))

def test4():
    '''
    Test to check DP Solution - True
    '''
    s1 = "abcd"
    s2 = "a*d"
    print(match_wildcard(s1, s2, len(s1), len(s2)))

def test5():
    '''
    Test to check DP Solution - False
    '''
    s1 = "abcd"
    s2 = "a*de"
    print(match_wildcard(s1, s2, len(s1), len(s2)))

def test6():
    '''
    Test to check DP Solution - True
    '''
    s1 = "abcdefg"
    s2 = "a*de*"
    print(match_wildcard(s1, s2, len(s1), len(s2)))

def test7():
    '''
    Test to check DP Solution - True
    '''
    s1 = "bcde"
    s2 = "*de"
    print(match_wildcard(s1, s2, len(s1), len(s2)))

def test8():
    '''
    Test to check DP Solution - False
    '''
    s1 = "ac"
    s2 = "*a*b"
    print(match_wildcard(s1, s2, len(s1), len(s2)))


test1() # True
test2() # True
test3() # True
test4() # True
test5() # False
test6() # True
test7() # True
test8() # False