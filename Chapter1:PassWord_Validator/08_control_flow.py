# # # The generic syntax for range is range(start_at, stop_before, step_by

# # >>> name = "Eric"
# # >>> for char in name:
# # ...     print("Give me a " + char + " !") 
# # >>> #???

# # Give me a E !
# # Give me a r !
# # Give me a i !
# # Give me a c !


# #>>> # This next line imports a function from a Python library.
# >>> # Don't worry about it too much for now.
# >>> from random import randint
# >>> fav_number = 77
# >>> guess_correct = False
# >>>
# >>> while not guess_correct:
# ...     guess = randint(0, 100)
# ...     if guess == fav_number:
# ...         print("You guessed right: 77!")
# ...         guess_correct = True
# ...     else:
# ...         print(f"{guess} is wrong! Try again.")