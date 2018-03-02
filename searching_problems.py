'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''
import re

# This function takes in a line of text and returns a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

#1.  (7pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.  (read the file line by line to accomplish this task)
file = open('search_files/dictionary.txt')
dic = []
largest = "YEET"
large_list = []

for line in file:
    words = split_line(line)
    for word in words:
        dic.append(word)

for i in range(len(dic)):
    word = dic[i]
    if len(word) > len(largest):
        largest = word

large_list.append(largest)

for i in range(len(dic)):
    word = dic[i]
    if len(word) == len(largest) and word != largest:
        large_list.append(word)

for i in large_list:
    print(i)

file.close()

#2.  (7pts)  Write code which finds
#  The total word count AND average word length of "AliceInWonderLand.txt"

file = open('search_files/AliceInWonderLand.txt')
all_words = []
all_numbers = []
x = 0

for line in file:
    words = split_line(line)
    for word in words:
        all_words.append(word)
        all_numbers.append(len(word))

print(len(all_words))

for i in range(len(all_words)):
    x += all_numbers[i]
print(x / len(all_numbers))


# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?
cheshire = 0
cat = 0
cheshire_cat = 0


for i in all_words:
    if i.upper() == "CHESHIRE":
        cheshire += 1

for i in all_words:
    if i.upper() == "CAT":
        cat += 1

for i in range(len(all_words)):
    if all_words[i].upper() == "CHESHIRE":
        if all_words[i+1].upper() == "CAT":
            cheshire_cat += 1

print(cheshire)
print(cat)
print(cheshire_cat)

#### OR #####

#3  (13pts)Find the most frequently occurring 
#  seven letter word in "AliceInWonderLand.txt"




# CHALLNENGE PROBLEM  (for fun, not for credit).  
#  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.




