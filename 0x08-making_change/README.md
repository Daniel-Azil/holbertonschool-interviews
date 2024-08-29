# Making Change

Welcome to the Making Change project! This repository features coding challenges centered around optimizing coin usage to achieve specific monetary values.

## Overview

The goal of this project is to develop an efficient solution to determine the minimum number of coins required to make up a given amount. This is a classic problem in algorithm design and dynamic programming, often encountered in technical interviews and coding assessments.

## Task Details

+ [x] **0. Change comes from within**<br/>In the file [0-making_change.py](0-making_change.py), you'll find a function designed to compute the least number of coins needed to reach a specified total amount. The function should conform to the following requirements:

  + **Function Prototype**: `def makeChange(coins, total)`
  
  + **Function Output**: The function should return the minimum number of coins necessary to meet the `total` amount. The details are:
    + If the `total` amount is `0` or a negative number, the function should return `0` since no coins are needed.
    + If it is not possible to reach the exact `total` using the given coins, the function should return `-1`.

  + **Function Input**:
    - `coins`: This parameter is a list of integers where each integer represents a coin denomination. Every denomination is a positive integer greater than `0`.
    - The function assumes an infinite supply of each type of coin provided in the list, meaning there is no limit to how many coins of each denomination you can use.

  + **Performance Considerations**: The efficiency of your solution is crucial. Your implementation will be evaluated based on how well it performs with large inputs. Aim to optimize both time and space complexity to handle a variety of test cases effectively.

## Notes

- Be mindful of edge cases such as when the `total` is smaller than the smallest coin or when the coin denominations cannot combine to meet the `total`.
- Test your function thoroughly with different inputs to ensure it handles all possible scenarios correctly and efficiently.
