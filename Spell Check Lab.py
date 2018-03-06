import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open('search_files/dictionary.txt')
dic = []
largest = "YEET"
large_list = []

for line in file:
    words = split_line(line)
    for word in words:
        dic.append(word)