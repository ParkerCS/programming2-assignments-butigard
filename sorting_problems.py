# Sorting problems (28pts)

# Problem 1 - Value Swap (2pts)
# Swap the values 18 and 38 in the list below
my_list = [27, 32, 18,  2, 11, 57, 14, 38, 19, 91]

temp = my_list[2]
my_list[2] = my_list[7]
my_list[7] = temp
print(my_list)


# Problem 2 - Selection Sort (8 pts)
# Make a selection sort FUNCTION which takes in 1 parameter (the list),
# sorts it and RETURNS the sorted list.  Then sort and print the result
# of the following list.
sort_me = [655, 722, 736, 314, 59, 778, 632, 477, 230, 556, 353, 769, 622, 731, 683, 233, 524, 186, 694, 507, 443, 833, 270, 373, 567, 775, 34]


def sort(list):
    BIG_LOOP = 0
    little_loop = 0
    for cur_pos in range(len(list)):
        BIG_LOOP += 1
        print("\nBIG LOOP:", BIG_LOOP, "\n")
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(list)):
            little_loop += 1
            print("Little Loop:", little_loop)
            if list[scan_pos] < list[min_pos]:
                min_pos = scan_pos
        list[min_pos], list[cur_pos] = list[cur_pos], list[min_pos]
    print(list, "\n\n\n\n\n\n\n\n\n\n")

sort(sort_me)


# Problem 3 - Insertion Sort (8 pts)
# Make an insertion sort FUNCTION which takes in 1 parameter (the list),
# sorts it and RETURNS the sorted list.  Then sort and print the result
# of the following list.
sort_me2 = [551, 138, 802, 954, 569, 372, 454, 366, 936, 959, 958, 202, 474, 658, 108, 424, 523, 611, 557, 0, 733, 903, 788, 850, 11, 12, 975]

def sort2(list):
    BIG_LOOP = 0
    little_loop = 0
    for key_pos in range(1, len(list)):
        BIG_LOOP += 1
        print("\nBIG LOOP:", BIG_LOOP, "\n")
        key_value = list[key_pos]
        scan_pos = key_pos - 1
        while (scan_pos >= 0) and (list[scan_pos] > key_value):
            little_loop += 1
            print("Little Loop:", little_loop)
            list[scan_pos + 1] = list[scan_pos]
            scan_pos -= 1
        list[scan_pos + 1] = key_value
    print(list, "\n\n\n\n\n\n\n\n\n\n")

sort2(sort_me2)

#################################################
# DO ONE OR THE OTHER FROM THE NEXT TWO PROBLEMS#
#################################################

# Problem 4 - Efficiency Challenge (10 pts)
# Modify your two functions so that they track the number of times
# you iterate through the big loop, and the inner loop of the sort.
# Make the functions print each value.  Run the sorts on the lists below.

sort_me3 = [77, 29, 59, 69, 86, 40, 47, 40, 74, 44, 58, 78, 9, 8, 13, 99, 3, 57, 19, 48, 55, 50, 94, 69, 98, 30, 37, 29, 40, 29, 36, 32, 26, 85, 61, 51, 70, 96, 90, 89, 91, 88, 68, 4, 4, 74, 15, 72, 5, 91, 76, 6, 56, 80, 72, 87, 63, 86, 48, 24, 17, 23, 30, 41, 7, 64, 16, 19, 40, 63, 14, 95, 44, 58, 1, 6, 45, 55, 52, 54, 44, 36, 50, 6, 96, 66, 8, 46, 48, 48, 75, 25, 39, 30, 70, 44, 38, 90, 49, 70]
sort2(sort_me3)
sort(sort_me3)

sort_me4 = [50, 61, 96, 72, 67, 12, 14, 1, 35, 51, 38, 32, 34, 29, 95, 75, 74, 83, 33, 3, 70, 0, 41, 4, 32, 1, 93, 39, 4, 20, 14, 11, 24, 69, 36, 36, 54, 90, 95, 36, 25, 24, 76, 30, 92, 95, 24, 6, 72, 78, 95, 73, 94, 33, 36, 30, 19, 23, 52, 28, 17, 82, 98, 74, 67, 43, 2, 89, 87, 8, 91, 7, 22, 78, 74, 84, 74, 87, 67, 93, 47, 74, 95, 92, 25, 46, 8, 74, 58, 80, 33, 31, 69, 2, 21, 93, 96, 72, 50, 61]
sort2(sort_me4)
sort(sort_me4)

#  ---- OR ----


# Problem 4 - All time NBA Scorers (10 pts)
#You are provided the top 50 scorers in NBA history in file/nba_scoring_leaders.txt
# It is a randomly ordered list.  Sort them by their total points scored.
# You may wish to put it in a 2d list first.  Look to Search assignment (split_line)
# This is a little different from the sorts done in class as you will likely be sorting a 2d list
# You will need to sort nba_leader_list[i] by using the score located at nba_leader_list[i][2].
#  Feel free to use either sorting method to accomplish this.  You can make a function, but it is not required.
# This is designed to test your understanding of the sort by applying it to slightly more messy list.
# Solving MALFORMED PROBLEMS leads to deeper understanding.  Good luck.
