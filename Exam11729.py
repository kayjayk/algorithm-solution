N = int(input())
#
# stacks = {1:list(range(N, 0, -1)),
#           2:[],
#           3:[]}

global result
global count
result = ""
count = 0

def swap(base, to):
    global count
    global result
    # stacks[to].append(stacks[base].pop())
    count += 1
    # result += "{} {}\n".format(base, to)
    print(base, to)

def hanoi(N, base, assist, to):

    if N==1:
        swap(base, to)

    else:
        hanoi(N-1, base, to, assist)
        swap(base, to)
        hanoi(N - 1, assist, base, to)


# print(count)
sum = 1
for i in range(N - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(N, 1, 2, 3)