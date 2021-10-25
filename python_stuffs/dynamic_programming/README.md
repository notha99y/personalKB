# Dynamic Programming
Tutorial Video: [link](https://www.youtube.com/watch?v=oBt53YbR9Kk)
## Memoization
Break down the problem into sub problems and store the results for future use

Recipe:
1. Make it work (brute force)
- visualize the problem as tree
- implement the tree using recursion (think about the tree as a base case)
- test it

2. Make it efficient
- add a memo object
- check keys in memo
- store return values into the memo

### Fibonacci
---
Write a function `fib(b)` that takes in a number as an argument. The function should return the n-th number of the Fibonacci sequence

the 1st and 2nd number of the sequence is 1. To generate the next number of sequence, we sum the previous two


### Traveler on 2D grid
---
Say that you are a traveler on a 2D grid. You begin the the top-left corner and yout goal is to travel to the bottom-right corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions x*y?


### Can Sum
---
Write a function `can_sum(target_sum, numbers)` that takes in a `target_sum` and an array of numbers as arguments.

The function should return a boolean indicating whether or not it is possible to generate the `target_sum` using numbers from the array.

You may use an elemrnt of the array as many times as need.

You may assume that all inout numbers are non negative


### How Sum
---
Write a function `how_sum(target_sum, numbers)` that takes in a `target_sum` and an array of numbers as arguments.

The function should return an array containing any combination of elements that add up to exactly the `target_sum`. If there is no combination that adds up to the `target_sum`, then return null.

If there are multiple combinations possible, you may return any single one.
## Tabulation