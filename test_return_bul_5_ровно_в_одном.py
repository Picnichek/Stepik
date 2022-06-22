
def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        counter = 0
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    counter += 1

    if len(word1) - counter == 1:
        return True
    elif counter - len(word1) == 1:
        return True
    else:
        return False

    pass

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))