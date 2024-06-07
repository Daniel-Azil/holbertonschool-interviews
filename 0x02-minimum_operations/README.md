# 0x02. Minimum Operations

## Tasks

## [0. Minimum Operations](./0-minoperations.py)
In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n H` characters in the file.

* Prototype: `def minOperations(n)`
* Returns an integer
* If n is impossible to achieve, return 0
Example:

`n = 9`

`H` => `Copy All` => `Paste` => `HH` => `Paste` =>`HHH` => `Copy All` => `Paste` => `HHHHHH` => `Paste` => `HHHHHHHHH`

Number of operations: `6`
```
$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
```
