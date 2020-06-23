num = input().split(" ")

def switch(str):
    str = list(str)
    tmp = str[0]
    str[0] = str[2]
    str[2] = tmp
    return ''.join(str)

A = int(switch(num[0]))
B = int(switch(num[1]))


print(A if A>B else B)
