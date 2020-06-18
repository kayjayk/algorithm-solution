N = int(input())

# for i in range(N):
#     for j in range(i):
#         print('*'*(j+1))
#
# for i in range(N, 0):
#     for j in range(i, 0):
#         print('*'*(j+1))

for i in range(N):
    print('*'*(i+1))
for i in range(N-1, 0, -1):
    print('*'*(i))