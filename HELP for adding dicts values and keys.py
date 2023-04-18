# --------#
#HELP to adding dictionary values and keys

dict_example = {'a': 1, 'b': 2}

print("original dictionary: ", dict_example)

dict_example['a'] = 100  # existing key, overwrite
dict_example['c'] = 3  # new key, add
dict_example['d'] = 4  # new key, add 

print("updated dictionary: ", dict_example)

# add the following if statements

if 'c' not in dict_example.keys():
    dict_example['c'] = 300

if 'e' not in dict_example.keys():
    dict_example['e'] = 5

print("conditionally updated dictionary: ", dict_example)