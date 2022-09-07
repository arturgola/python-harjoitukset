
def odd_list(integers_list):
    odd_num = []
    for i in integers_list:
        if i % 2 != 0:
            odd_num.append(i)
    return odd_num


mass_int = [1, 2, 3, 4]
print(mass_int)
print(odd_list(mass_int))

