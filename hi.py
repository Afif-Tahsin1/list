def match_words(words):
    ctr = 0
    list = []
    for i in words:
        if len(i) > 1 and i[0] == i[-1]:
            ctr += 1
            list.append(i)
    print(f"List of words with last and first character same\n{list}")
    return ctr
count = match_words(['abc', 'cfc', 'xyz', 'abba', '1221'])
print(f"Number of words having last and first character same: {count}")
