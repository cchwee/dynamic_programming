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

 <br />
 
---this is a seperation line---

 <br />


## Background info - Task 2: Greenhouse

You are a gardener in charge of a greenhouse. You are growing a variety of exotic plants as
decoration for a party. You want to maximise the chance that all the plants are grown by the
day of the party. In order to cause plants to grow more quickly, you can put sun lamps above
the plants to give them more nutrients.

You have calculated the probability that each plant will be ready on time, based on the number
of lamps you assign to it. You cannot move the lamps around once you assign them to a plant.
You want to maximise the chance that all the plants are fully grown by the day of the party.

## Input
**num_p** and **num_l **are positive integers representing the number of plants and lamps respectively.

**probs** is a list of lists, where probs[i][j] represents the probability that plant i will be ready in time if it is allocated j lamps. Values in probs are floats between 0 and 1 inclusive.

Plants do not always grow faster with more light, so it is possible for the probabilities to decrease as well as increase, as the number of lamps increases. In other words, the lists within probs may not be sorted ascending.

## Output
**best_lamp_allocation** returns an float, which is the highest probability of all plants being ready by the party that can be obtained by allocating lamps to plants optimally.

## Example
```
probs = [[0.5, 0.5, 1],[0.25,0.1,0.75]]
best_lamp_allocation(2,2,probs)
>>> 0.375

probs = [[0.5, 0.75, 0.25],[0.75,0.25,0.8]]
print(best_lamp_allocation(2,2,probs))
>>> 0.5625

```
- In the first example, we have 2 lamps to use. If we assign 0 lamps to plant 0, it has a 0.5
probability of being ready. We would need to assign the full 2 lamps to it to improve its chance
(to 1). We have 2 lamps left, so the best thing to do is assign both to plant 1, for a probability
of 0.75. This gives an overall probability of 0.75*0.5=0.375.

- In the second example, we again have 2 lamps and 2 plants, but with different probabilities. This time, the most
efficient thing is to not use all the lamps! Giving 1 lamp to plant 0 and 0 lamps to plant 1 give
a probability of 0.5625. It would be ideal to give 1 lamp to plant 0 and 2 lamps to plant 1, but
we do not have 3 lamps so this is impossible.

## Complexity
**best_lamp_allocation** should run in O(P L^2) time and O(P L) space, where P is num_p, and L is num_l.

 <br />
 
 ---end of tasks---
 
  <br />
 
#### Disclaimer
- This is a school assignment question. 
