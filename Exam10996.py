N = int(input())
star = '*'
stars = '* '
stars2 = ' *'

for i in range(N):
    if N%2==0:
        print(stars*(N//2))
        print(stars2*(N//2))
    else:
        print(star + stars2*(N//2))
        print(stars2*(N//2))