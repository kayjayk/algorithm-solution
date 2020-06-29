list5 = [0, -1, -2, 0, -1, 1, 0, -1, 1, 0]
list3 = [0, 2, 4, 1, 3]
N = int(input())
envelopes = 0

if N in (4, 7):
    envelopes = -1
else:
    envelopes = (N//10)*2
    N %= 10
    envelopes += list5[N] + list3[N%5]

print(envelopes)