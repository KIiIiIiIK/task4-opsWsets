list1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

set1 = set(list1)  # making set out of list
print(set1)

list2 = [2, 3, 1, 1, 4, 4, 4, 4, 4, 4]

set2 = set(list2)
print(set2)

set3 = set.difference(set2, set1)  # set of different items between set1 & set2
print(set3)

set4 = set.intersection(set2, set1)  # set of common items between set1 & set2
print(set4)
