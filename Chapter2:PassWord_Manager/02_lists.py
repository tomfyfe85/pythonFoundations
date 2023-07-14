# 1 - creating lists
print([1,2,3,'hello'])

#2 - adding items to list
list = []
list.append('HI!')
print(list)
list.append('WORLD')
print(list)

#3 - accessing items on a list
print(list[0])
print(list[1])
# print(list[3]) out of range
print(list[-1])

# slicing lists
track_list = ["Sympathy For The Devil", "Leech", "Dragonaut", "Green Machine", "Sound & Vision"]
print(track_list[0])
print(track_list[0:3])
print(track_list[2:5])

practice_list = [1, 17, 10, 1, 20, 22]

print(practice_list.clear())
print(practice_list)
#  => [] mutates list

#4 - list methods
practice_list1 = [1, 17, 10, 1, 20, 22]
practice_list1.reverse()
# doesn't return any thing but reverses list
print(practice_list1.pop())
# => 1
# takes out the last element of an array
print(practice_list1.index(20))
# => 1
# returns index of item in argument
print(practice_list1.sort())
# doesn't return any thing but sorts list in ascending order
print(practice_list1)
# [1, 10, 17, 20, 22]

string_list = ["bear", "anaconda", "cat", "ZEBRAAAAA", "dog", "elephant"]
string_list.sort()
print(string_list)
#['ZEBRAAAAA', 'anaconda', 'bear', 'cat', 'dog', 'elephant']

#5 - A list of Passwords?



def add_to_list(list, el):
    new = list.append(el)
    # list.append(el)
    return new

print(add_to_list(["a", "b", "c"], 'd'))
