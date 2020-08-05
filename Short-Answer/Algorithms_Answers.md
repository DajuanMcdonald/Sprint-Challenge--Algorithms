#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I
a)
An example of O(n) runtime:
```python
a = 0
    while (a < n1 * n2 * n3):
      a = a + n4 * n5 # this matters
````
If we examine we can rule out O(1), because we dependent on
 an input size of n. 
 
This will run the same no matter what `n2, n1` or `n3` are.

pretend `n` is an integer that `a` will turn itself into.
Since `a` always starts out less than `n1 * n2 * n3`, 
we never really leave this part. 

so `a` will simply equal to whatever is stored in `n4 * n5`'s product
---------------------------------------------------------------------
b)
An example of O(n log(n)) runtime:
```python
sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
        print(f'{sum}, {j}, {i}')
``` 
If we examine we eliminate O(1) because we now have a
range of size n. This loop essentially runs Linear time with input
size. The time grows proportional to the length of the list. 
The while loop runs N/2 (j to n * 2, sum n + 1) thus: N + N + 1 = N^2 or O(n)
c)
An example of O(n)
```python
def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
If we examine we can eliminate O(n^2) 
## Exercise II

Write out your proposed algorithm in plain English or 
pseudocode AND give the runtime complexity of your solution.
