# The Knapsack Problem

The knapsack problem or rucksack problem is a problem in combinatorial optimization: Given a set of items,
each with a weight and a value, determine the number of each item to include in a collection so that the total
weight is less than or equal to a given limit and the total value is as large as possible. It derives its name
from the problem faced by someone who is constrained by a fixed-size knapsack and must fill it with the most
valuable items.

## Example

|Value|Weight|
------|------|
|2|4|
|3|2|
|5|6|
|1|1|
|5|2|

If you could carry not more than weight 10, find the maximum possible values to carry.

Well the answer to that is,

|Value|Weight|
|------|------|
|3|2|
|5|6|
|5|2|

Hence, the maximum value you can carry is `3 + 5 + 5 = 13`.

The most general solution to this problem has **asymptotic complexity** of ![2^x](http://latex.codecogs.com/gif.latex?2%5En).

But if we use **Memoization** (dynamic programming technique) we can reduce the **asymptotic complexity** to *n*