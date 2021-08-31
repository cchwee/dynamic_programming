def counting_sort(a_list: list, base: int, exp: int) -> list:

    count_array = [[] for i in range(base+1)]

    # item as linked list in count_array
    for i in range(len(a_list)):
        digit = (a_list[i][1] // base ** exp) % base 
        count_array[digit].append(a_list[i])

    output_lst = []
    for lst in count_array:
        for item in lst:
            output_lst.append(item)

    return output_lst


def radix_sort(lst: list) -> list:
    
    if len(lst) > 0:
        max_val = lst[0][1]
        for i in range(1, len(lst)):
            if lst[i][1] > max_val:
                max_val = lst[i][1]

        exp = 0
        while (max_val // 10**exp) > 0:
            lst = counting_sort(lst, 10, exp)
            exp += 1

    return lst


def count_encounters(target_difficulty: int, monster_list: list) -> int:

    sorted_monster_list = radix_sort(monster_list)

    # 2D matrix memo with default "inifinity" values
    memo = [[float('inf') for _ in range(target_difficulty + 1)] for _ in range(len(sorted_monster_list) + 1)]

    # target_difficulty == 0, 1 way: not selecting any
    for i in range(len(sorted_monster_list) + 1):
        memo[i][0] = 1

    # target != 0, monster list is empty, 0 ways to select
    for j in range(1, target_difficulty + 1):
        memo[0][j] = 0

    for i in range(1, len(sorted_monster_list) + 1):
        for j in range(1, target_difficulty + 1):  

            # if the monster's difficulty > target
            if sorted_monster_list[i-1][1] > j:
                previous = memo[i-1][j]
                memo[i][j] = previous
            
            else:
                previous = memo[i-1][j]
                memo[i][j] = previous + memo[i][j - sorted_monster_list[i-1][1]]

    # returns the num of monsters whose difficulties sum to target_difficulty
    return memo[len(sorted_monster_list)][target_difficulty]


'''
Driver code
'''
target_difficulty = 15
monster_list = [("bear", 5), ("imp", 2), ("kobold", 3), ("dragon", 10)]
print(count_encounters(target_difficulty, monster_list))
