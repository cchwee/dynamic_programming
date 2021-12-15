# Dynamic Programming 

## Background info - Task 1: Game Master

You are the game master for a table-top role-playing game that you and your friends are playing.

You want to create an encounter, and you want to hit a certain level of difficulty.

You will have a monster list, and you want to select a group of monsters whose difficulty ratings sum up to the target difficulty.

## Input
**target_difficulty** is a non-negative integer.

**monster_list** is a list of tuples. Each tuple represents a type of monster. 
The first value in each tuple is a string, which is the name of the type of monster. 
The second value is a positive integer, representing the difficulty of that particular type of monster.

## Output
**count_encounters** returns an integer, which is the number of different sets of monsters whose difficulties sum to target_difficulty. 

Note that a type of monster may be used more than once in an encounter.

## Example
```
target_difficulty = 15
monster_list = [("bear", 5), ("imp", 2), ("kobold", 3), ("dragon", 10)]
print(count_encounters(target_difficulty, monster_list))
>>> 9

```
In the above example, the possible encounters are:
- 1 dragon, 1 bear
- 1 dragon, 1 kobold, 1 imp
- 3 bear
- 2 bear, 1 kobold, 1 imp
- 1 bear, 2 kobold, 2 imp
- 1 bear, 5 imp
- 5 kobold
- 3 kobold, 3 imp
- 1 kobold, 6 imp

## Complexity 
**count_encounters** should run in O(DM) where:

- D is the value of target_difficulty
- M is the length of monster_list

## Background info - Task 2: Greenhouse

#### Disclaimer
- This is a school assignment question. 
