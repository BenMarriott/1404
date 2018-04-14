a_list = [1, 2, 3]
b_list = [4, 6, 7, 8]

new_list = []
for i, (a, b) in enumerate(zip(a_list, b_list)):
    # print(i, a, b)
    print(b)
    new_list.append(a + b)
print(new_list)