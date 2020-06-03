import sys

T = int(sys.stdin.readline())

for i in range(T):
    tmp = sys.stdin.readline().split(sep=' ')
    R = int(tmp[0])
    S = tmp[1].rstrip()
    P = ''

    for j in range(len(S)):
        P += S[j]*R

    print(P)