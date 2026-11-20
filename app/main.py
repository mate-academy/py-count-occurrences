def sum_two_lists(list1, list2):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i] + list2[i])
    return new_list
print(sum_two_lists([1, 3, 5], [2, 4, 6]))