is_prime = [True for i in range(0, 1001)]
for i in range(2, 1001):
    for j in range(i, 1001, i):
        if j==i:
            continue
        else:
            is_prime[j] = False

is_prime[1] = False

N = int(input())
input_num = map(int, input().split())
for i in input_num:
    if not is_prime[i]:
        N -= 1

print(N)