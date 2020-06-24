thresholds = []
for i in range(ord('A'), ord('P')+1, 3):
    thresholds.append(i)
thresholds.append(thresholds[len(thresholds)-1]+4)
thresholds.append(thresholds[len(thresholds)-1]+3)
thresholds.append(thresholds[len(thresholds)-1]+4)

word = input()
time_to_dial = 0

for i in list(word):
    for j in range(len(thresholds)-1):
        if thresholds[j] <= ord(i) < thresholds[j+1]:
            time_to_dial += 3 + j

print(time_to_dial)