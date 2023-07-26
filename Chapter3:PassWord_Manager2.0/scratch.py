def sort_by_last_letter(list):
    newList = [word[::-1] for word in list]
    newList.sort()
    finList = [word[::-1] for word in newList]
    return finList


print(sort_by_last_letter(["banana", "apple", "carrot", "avocado"]))


def greater_than_5(lis):
    return list(filter(lambda num: num > 5, lis))


print(greater_than_5([1, 6, 7, 5, 3, 2]))


def greater_than(lyst, num):
    newList = []
    for int in lyst:
        if int > num:
            newList.append(int)
    return newList


print(greater_than([9, 3, 6, 44, 7, 7], 6))

def less_than(lyst, num):
  newList = filter(lambda int:  int < num, lyst)
  return list(newList)

print(less_than([9, 3, 6, 44, 1, 7, 7], 6))
