N = int(input())

for i in range(N):
    word = input()
    loop_break = False

    while(len(word)>0):
        char_count = word.count(word[0])

        for j in range(char_count):
            if word[j] != word[0]:
                loop_break = True
                break

        if loop_break:
            N -= 1
            break

        word = word[char_count:]

print(N)
