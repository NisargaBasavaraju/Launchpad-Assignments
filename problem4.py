def Remove(duplicate):
    new_list = []
    for i in duplicate:
        if i not in new_list:
            new_list.append(i)
    return new_list
duplicate = [1, 1, 2, 3, 4, 64, 35, 93, 35, 87, 4, 3]
print(Remove(duplicate))
