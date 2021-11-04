def checkMagazine(magazine, note):
    words_dict = {}
    for word in magazine:
        if(words_dict.get(word) == None):
            words_dict[word] = 1
        else:
            words_dict[word] = words_dict[word] + 1
    for word in note:
        if word not in words_dict or words_dict[word] == 0:
                print("No")
                return
        else:
        #I've forgotten this part at first, lol.
            words_dict[word] += -1
    print("Yes")
