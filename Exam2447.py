N = int(input())
star_frame = []

for i in range(N):
    star_frame.append([True]*N)

def unstar(N, x, y):
    threshold = int(N/3)

    for i in range(x + threshold, x + threshold*2):
        for j in range(y + threshold, y + threshold * 2):
            star_frame[i][j] = False

    for i in range(x, x + N, threshold):
        for j in range(y, y + N, threshold):
            if i == x + threshold and j == y + threshold:
                continue
            if threshold > 1:
                unstar(threshold, i, j)

unstar(N, 0, 0)

for i in range(len(star_frame)):
    starline = ''
    for j in range(len(star_frame)):
        if star_frame[i][j]:
            starline += '*'
        else:
            starline += ' '
    print(starline)