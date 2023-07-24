square_dict = {}
for num in range(1,11):
    square_dict[num] = num*num

print(square_dict)

square_dict2 = {num: num*num for  num in range(1,11)}
print(square_dict2)

person = {'name' : 'jo', 'age' : 43, 'height' : '170'}
for item in person:
    print(f"key value pair: {item} -> {person[item]}")

friends = ["Will", "Bernie", "Garth", "Suze"]
card_suit = ["Spades", "Clubs", "Diamonds", "Hearts"]
from random import shuffle
shuffle(card_suit)
card_friends = {friend: card for (friend, card) in zip(friends, card_suit)}
print(card_friends)
shuffle(card_suit)
card_friends = {friend: card for (friend, card) in zip(friends, card_suit)}
print(card_friends)

tourny_dict = {'Dan': 10, 'Wolfgang': 20, 'June': 53, 'Tany': 37, 'Sharon': 14, 'Will': 0}

next_round = {}
next_round = dict(filter(lambda player: player[1] > 20, tourny_dict.items()))
print(next_round)

new_round = {key:value for (key, value) in tourny_dict.items() if value > 20 }
print(new_round)

# What are dictionaries
# Dictionaries are groups of key:value pair
# 
# How dictionaries can be manipulated?
# Using loops and comprehension, and updating and deleting

# How this differs from list manipulation
# Lists are made up of single elements

# What is more "pythonic", advanced methods or simple loops?
#Simple loops