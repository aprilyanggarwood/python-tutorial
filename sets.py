thisset = {"apple", "banana", "cherry"}


item = "banana"
if item in thisset:
    thisset.remove(item)

set_list = list(thisset)

print(set_list)
set_list[0] = "kiwi"

new_set = set(set_list)

print(new_set)