from collections import defaultdict

def filter_only_one(n_list):
    n_dic = defaultdict(int)
    for i in n_list:
        n_dic[i] += 1

    for key in n_dic.keys():
        if n_dic[key] == 1:
            only_one = key
            break

    return only_one

x_list = []
y_list = []
for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

print(filter_only_one(x_list), filter_only_one(y_list))