def replace(s):
    n = len(s)
    new_string = ""
    for i in range(0 , n):
        if( i%2 == 0 ):
            new_string = new_string + s[i]
        else:
            new_string = new_string + ''
    return new_string

s = "hello team"
print(replace(s))