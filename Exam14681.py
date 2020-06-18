x = int(input())
y = int(input())

quad_num = 0

if x > 0:
    if y > 0:
        quad_num = 1
    else:
        quad_num = 4
else:
    if y > 0:
        quad_num = 2
    else:
        quad_num = 3

print(quad_num)