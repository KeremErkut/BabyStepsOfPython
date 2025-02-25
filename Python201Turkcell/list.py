notes = [90, 75, 60, 64]
print(type(notes))

list = ["a", 15.5, 90, -4, notes]
print(len(list)) # -> 5

print(list[4]) 

wholeList = [notes, list]

del wholeList #List can be deleted using 'del'.

print(notes[:2])
print(notes[2:])
print(notes[0:2])
print(list[4][0])