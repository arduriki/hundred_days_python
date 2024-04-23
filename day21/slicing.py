piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_keys[2:5])  # from 0 to 5 position
print(piano_keys[2:])  # from 0 to the end
print(piano_keys[:5])  # from 0 to 5 position
print(piano_keys[2:5:2])  # with increment
print(piano_keys[::2])  # get every 2 positions
print(piano_keys[::-1])  # from the end to the beginning

piano_tuple = ("do", "re", "mi", "fa", "sol", "la", "si")

print(piano_tuple[2:5])  # also works with tuples