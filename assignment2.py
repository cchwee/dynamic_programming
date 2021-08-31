def counting_sort(a_list: list, base: int, exp: int) -> list:

    # initialise the count_array
    count_array = [[] for i in range(base+1)]

    # put in the item as linked list into count_array
    for i in range(len(a_list)):
        digit = (a_list[i][1] // base ** exp) % base 
        count_array[digit].append(a_list[i])

    # iterate through count_array and return output
    output_lst = []
    for lst in count_array:
        for item in lst:
            output_lst.append(item)

    # returns a sorted list
    return output_lst


# Radix sort
def radix_sort(lst: list) -> list:
    
    # get the max val in lst
    if len(lst) > 0:
        max_val = lst[0][1]
        for i in range(1, len(lst)):
            if lst[i][1] > max_val:
                max_val = lst[i][1]

        exp = 0
        while (max_val // 10**exp) > 0:
            lst = counting_sort(lst, 10, exp)
            exp += 1

    # returns a sorted list nums in asc order
    return lst


def count_encounters(target_difficulty: int, monster_list: list) -> int:

    # pre-process monster list - sort in asc
    sorted_monster_list = radix_sort(monster_list)

    # create a 2D matrix memo with default "inifinity" values
    memo = [[float('inf') for _ in range(target_difficulty + 1)] for _ in range(len(sorted_monster_list) + 1)]

    # set base case, when target_difficulty == 0 
    # there's only 1 way to achieve that, which is by not selecting any monsters
    for i in range(len(sorted_monster_list) + 1):
        memo[i][0] = 1

    # base case when target != 0, but monster list is empty
    for j in range(1, target_difficulty + 1):
        memo[0][j] = 0

    # memoization, do by row then column, ie: first row --> 1st, 2nd, 3rd... column
    # i is the index for row, j is the index for column
    for i in range(1, len(sorted_monster_list) + 1):

        # start from column 1 ... target since 0 is handled as base case alrd
        for j in range(1, target_difficulty + 1):  

            # if the monster's difficulty is higher than target
            if sorted_monster_list[i-1][1] > j:

                # it means this monster is not selected, simply copy the previous row's column value
                memo[i][j] = memo[i-1][j]
            
            # else if monster's difficulty is lower than target
            # we need to check if this "new" monster should be selected
            else:

                # memo[i][j] = top val + memo[i][target column value - monster difficulty]
                memo[i][j] = memo[i-1][j] + memo[i][j - sorted_monster_list[i-1][1]]

    # returns the num of monsters whose difficulties sum to target_difficulty
    return memo[len(sorted_monster_list)][target_difficulty]


'''
Driver code
'''
target_difficulty = 15
monster_list = [("bear", 5), ("imp", 2), ("kobold", 3), ("dragon", 10)]
print(count_encounters(target_difficulty, monster_list))
