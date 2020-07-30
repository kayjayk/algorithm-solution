import math

def Eratos(M, N):
    count = 0
    is_prime = [True for i in range(N+1)]
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(math.sqrt(N+1))+1):
        for j in range(i, N+1, i):
            if j==i: continue
            is_prime[j] = False

    for i in range(M+1, N+1):
        if is_prime[i]:
            count += 1

    return count

while(True):
    M = int(input())
    if M==0:
        break
    else:
        print(Eratos(M, 2*M))