import math
T = int(input())

cases = []
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dist_btw_centers = math.sqrt(math.pow(abs(x1-x2), 2) + math.pow(abs(y1-y2), 2))

    if r1 > r2:
        rs = r2
        rl = r1
    else:
        rs = r1
        rl = r2

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if dist_btw_centers == r1 + r2:
            print(1)
        elif dist_btw_centers > r1 + r2:
            print(0)
        else:
            if dist_btw_centers + rs == rl:
                print(1)
            elif dist_btw_centers + rs < rl:
                print(0)
            else:
                print(2)