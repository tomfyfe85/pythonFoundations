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
  newList = filter(lambda int: int < num, lyst)
  return list(newList)

print(less_than([9, 3, 6, 44, 1, 7, 7], 6))

def all_above(lyst, num):
    newList = list(map(lambda int: True if num < int else False, lyst))
    # return True if True in newList else False
    return list(newList)

print(all_above([9, 3, 6, 44, 1, 7, 7], 6))

def add_key_value_pair(dic, key, val):
    dic[key] = val
    return dic

def where_value_below(dic, num):
    newDic = {}
    for key, val in dic.items():
        if val < num:
            newDic[key] = val
    return newDic

print(where_value_below({'cat': 4, 'person': 2, 'centipede': 100}, 5))

class Greeter():
    def hello(self, name):
        return f"Hello, {name}!"
    
    def goodbye(self, name):
        return f"Goodbye, {name}!"
    
    def good_night(self, name):
        return f"Good night, {name}!"
    
    def good_morning(self, name):
        return f"Good morning, {name}!"
    
class Basket():
    def __init__(self): 
        self.lyst = []
    
    def add(self, item):
        self.lyst.append(item)

    def list_items(self):
        return self.lyst
