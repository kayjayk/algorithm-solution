M = int(input())
N = int(input())

is_prime = [True for i in range(0, 10001)]
for i in range(2, 101):
    for j in range(i, 10001, i):
        if j==i:
            continue
        else:
            is_prime[j] = False

is_prime[1] = False

count = 0
min_prime = -1
for i in range(M, N+1):
        count += is_prime[i]*i
        if is_prime[i] and min_prime==-1:
            min_prime = i

if min_prime != -1:
    print(count)
print(min_prime)