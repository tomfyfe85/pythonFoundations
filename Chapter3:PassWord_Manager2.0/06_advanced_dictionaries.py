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
