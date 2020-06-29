A, B, V = map(int, input().split())
how_long_days = (V-A)//(A-B) + 1
if (V-A)%(A-B) == 0:
    print(how_long_days)
else:
    print(how_long_days+1)