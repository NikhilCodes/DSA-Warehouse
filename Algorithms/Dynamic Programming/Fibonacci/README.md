In mathematics, the Fibonacci numbers, commonly denoted Fn form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F_0=0,   F_1=1,

and

F_n=F_{n-1}+F_{n-2}, F_n=F_{n-1}+F_{n-2},
for n > 1.

One has F_2 = 1. In some books, and particularly in old ones, F_0, the "0" is omitted, and the Fibonacci sequence starts with F1 = F2 = 1. 

The beginning of the sequence is thus:

`0 1 1 2 3 5 8 13 21 34 55 89 144 ...`


The function `fibonacci_vanilla(n)` is the most simple implementation, and `fibonacci(n)` is the same as that of its vanilla implementation but with `memoization` which speeds up this function by atleast **x1000**.

### Inference of the performance Experiment
```
[In]:  print('Vanilla Fibonacci:', timeit.timeit('fibonacci_vanilla(30)', globals=globals(), number=1), 'seconds')
       print('Memoized Fibonacci:', timeit.timeit('fibonacci(30)', globals=globals(), number=1), 'seconds')
      
[Out]: Vanilla Fibonacci: 4.2228784 seconds
       Memoized Fibonacci: 0.0003140999999997618 seconds
```
