multigraphs = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
sum = len(word)

for i in multigraphs:
    for j in range(len(word)-2):
        if word[j:j+len(i)] == i:
            sum -= 1
    if i != 'dz=' and i == word[len(word)-2:len(word)]:
        sum -= 1

print(sum)