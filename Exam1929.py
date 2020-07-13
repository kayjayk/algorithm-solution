import math
M, N = map(int, input().split(' '))
is_prime = [True for i in range(N+1)]
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(math.sqrt(N+1))+1):
    for j in range(i, N+1, i):
        if j==i: continue
        is_prime[j] = False

for i in range(M, N+1):
    if is_prime[i]:
        print(i)
