S = input()
res_str = ''
for i in range(ord('a'), ord('z')+1):
    res_str += str(S.find(chr(i)))
    if i == ord('z'):
        break
    res_str += (' ')

print(res_str)