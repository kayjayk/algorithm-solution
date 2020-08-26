import math

T = int(input())
n_list = []

for i in range(T):
    n_list.append(int(input()))

N = sorted(n_list, reverse=True)[0]
is_prime = [True for i in range(N+1)]
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(math.sqrt(N+1))+1):
    for j in range(i, N+1, i):
        if j==i: continue
        is_prime[j] = False

for n in n_list:
    for j in range(int(n/2), 0, -1):
        if is_prime[j] and is_prime[n-j]:
            print(j, n-j)
            break
