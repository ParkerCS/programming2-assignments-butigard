import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open('search_files/dictionary.txt')
dic = []


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


for i in range(len(AliceWords)):
    word = AliceWords[i]
    u = 0
    while u < len(dic) and word.upper() != dic[u]:
        u += 1

    if u < len(dic):
        print("Found", word, "at position", u)
    else:
        print("Word", word, "not found in dictionary")
