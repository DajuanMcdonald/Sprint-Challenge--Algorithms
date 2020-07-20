#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
An example of O(1) runtime:
```python
a = 0
    while (a < n1 * n2 * n3):
      a = a + n4 * n5 # this matters
````
If we examine we can rule out O(n), because we are not dependent on
 an input size of n. 
 
This will run the same no matter what `n2, n1` or `n3` are.

pretend `n` is an integer that `a` will turn itself into.
Since `a` always starts out less than `n1 * n2 * n3`, 
we never really use this part, 

so `a` will simply equal to whatever is stored in `n4 * n5`'s product


b)
An example of O(n) runtime:
```python
sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
        print(f'{sum}, {j}, {i}')
``` 


c)
An example of O(2^n) 

```python
def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
## Exercise II


