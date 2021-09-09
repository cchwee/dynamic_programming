# counting sort called by radix sort
def counting_sort(a_list: list, base: int, exp: int) -> list:
    '''
    # Input
    a_list = a list of numbers
    base = base to be sorted in
    exp = exponent of the number

    # Output 
    returns a sorted list

    # Complexity
    The complexity is O(N + U), where N is the size of the input array, and U 
    is a value which is dependent on the value of the given base.
    '''
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

# Radix sort for use in count_encounters
def radix_sort(lst: list) -> list:

    '''
    # Inputs: 
    nums --> is a list which consists of only non-negative integers, 
    b --> is any integer value that is larger or equal to 2.

    # Output: 
    The output is a list which has been sorted. 

    # Complexity: 
    The complexity is O(logbM * (N+b)), where b is the base, M would be the largest 
    value in nums, follwed by (N+b) which is contributed by the recursive calls of 
    counting sorts
    '''

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



# Task 1 - finding the number of unique posible encounters given a target difficulty
def count_encounters(target_difficulty: int, monster_list: list) -> int:
    '''
    # Input
    target difficulty = a positive integer 
    monster_list = a list of tuples in the form of ('monster name', monster difficulty)
    
    # Output
    returns an integer which indicates the number of unique encounters.

    # Complexity
    O(DM) where D is the value of target difficulty and M is the length of monster list.
    '''

    # sort the monster list for easy comparison
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

            # if the monster's difficulty > target, we ignore and copy the previous value
            if sorted_monster_list[i-1][1] > j:
                previous = memo[i-1][j]
                memo[i][j] = previous
            
            else:
                previous = memo[i-1][j]
                memo[i][j] = previous + memo[i][j - sorted_monster_list[i-1][1]]

    # returns the num of monsters whose difficulties sum to target_difficulty
    return memo[len(sorted_monster_list)][target_difficulty]



# Task 2 - asset allocation concept
def best_lamp_allocation(num_p, num_l, probs):

    '''
    # Inputs
    num_p: positive int, number of plants
    num_l: positive int, number of lamps
    probs: list of list, probs[i][j] means plant i will be ready in time if j lamps are given

    # Outputs
    returns a float value of the highest probability of all plants being ready.

    # Complexity
    O(P L^2) time because we need to loop through each sum of lamps, 
    and O(P L) space for the memo table, where P is num_p, and L is num_l.


    # Calculation (for self study purpose only)
    eg. probs = [[0.5,  0.5, 1], [0.25, 0.1, 0.75]]
        num_p = 2
        num_l = 2
    memo:
    [   sum of plant =   0    1    2
        sum of lamp = 0 [1] [0.5] [ ]
                      1 [1] [0.5] [ ]
                      2 [1] [1.0] [ ]
     ] 

     memo[0][2] possible combinations: 0.5 x 0.25 (could only choose 0.25 because 0 + 0 = 0)
     memo[1][2] possible combinations: 0.5 x 0.1 (plant 1 - 0, plant 2 - 1) // 0.5 x 0.25 (plant 1 - 1, plant 2 -0)
     memo[2][2] possible combinations: 0.5 x 0.75 (plant 1 - 0, plant 2 - 2) // 0.5 x 0.1 (plant 1 - 1, plant 2 - 1) // 1.0 x 0.25 (plant 1 - 2, plant 2 - 0)
    '''
   
    # when num_p == 0, max_prob is always 1
    if num_p == 0: return 1

    # create a 2D memo array: num_p * num_l
    memo = [[float(0) for i in range(num_p + 1)] for a in range(num_l + 1)]

    # insert base case; when num_p = 0, max probability = 1
    for i in range(num_l + 1):
        memo[i][0] = 1
    
    # start from sum of plant = 1, sum of lamp = 0
    sum_lamp = 0
    sum_plant = 1

    # variable to store max_probability
    max_prob = 0

    while sum_plant <= num_p:

        # record memo row and col
        memo_row = sum_lamp
        memo_col = sum_plant

        # record num of lamps used
        lamp_num = 0 

        # record previous max prob of same of lamp with one less num of plant 
        prev = memo[sum_lamp][sum_plant - 1] 
        
        # ensure memo row does not exceed num of lamp
        while memo_row <= num_l:
            new_val = prev * probs[sum_plant-1][lamp_num]

            # replace only when new val larger than current cell value
            if new_val > memo[memo_row][memo_col]:
                memo[memo_row][memo_col] = new_val
            
            # check if we've reached the last plant to record max prob
            if memo_col == num_p:
                if new_val > max_prob:
                    max_prob = new_val

            memo_row += 1
            lamp_num += 1

        # if we reached the end of sum_lamp, add in new plant, reset sum_lamp
        if sum_lamp == num_l:
            sum_plant += 1
            sum_lamp = 0
        else:
            sum_lamp += 1

    return max_prob
    






