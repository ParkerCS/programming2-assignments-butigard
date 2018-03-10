import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open('search_files/dictionary.txt')
dic = []
wrong_words = []
wrong = 0
right = 0

for line in file:
    words = split_line(line)
    for word in words:
        dic.append(word)
print(dic)

Alice = open('search_files/AliceInWonderLand200.txt')
AliceWords = []

for line in Alice:
    word = split_line(line)
    for words in word:
        AliceWords.append(words)
print(AliceWords)


# LINEAR
for i in range(len(AliceWords)):
    word = AliceWords[i]
    u = 0
    while u < len(dic) and word.upper() != dic[u]:
        u += 1

    if u < len(dic):
        print("Word -->" + word + "<-- is spelled correctly")
        right += 1
    else:
        print("Word -->" + word + "<-- was not found in dictionary")
        wrong += 1
        wrong_words.append(word)


# BINARY
lower_bound = 0
upper_bound = len(dic) - 1
found = False

for i in range(len(AliceWords)):
    word = AliceWords[i]
    while lower_bound <= upper_bound and not found:
        middle_pos = (upper_bound + lower_bound) // 2
        if dic[middle_pos] < word.upper():
            lower_bound = middle_pos + 1
        elif dic[middle_pos] > word.upper():
            upper_bound = middle_pos - 1
        else:
            found = True

    if found:
        print("Word -->" + word + "<-- is spelled correctly")
    else:
        print("Word -->" + word + "<-- was not found in dictionary")

print(right)
print(wrong)
print(wrong_words)
