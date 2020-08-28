N = int(input())
star_frame = []
for i in range(N):
    star_frame.append([False]*N)
def stars(N, is_star):
    if N == 1:
        if 