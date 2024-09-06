# Prime Game - Python Solution

## Table of Contents
- [Introduction](#introduction)
- [Game Description](#game-description)
- [Functionality](#functionality)
- [How the Code Works](#how-the-code-works)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Limitations](#limitations)

## Introduction

This repository contains a Python solution to the Prime Game, a game where two players (Maria and Ben) take turns removing prime numbers and their multiples from a set of numbers. This solution determines the winner of multiple rounds based on optimal play strategies.

## Game Description

Maria and Ben are playing a game using numbers from 1 to `n`. The game is played in rounds, where in each round:

1. Maria always goes first.
2. Players take turns picking a prime number from the set and removing that prime and its multiples.
3. The player who cannot make a move (i.e., no primes left to pick) loses.

The game consists of `x` rounds, with different values of `n` for each round. The goal is to determine who wins more rounds—Maria or Ben.

## Functionality

- **Prime Number Generation**: A helper function generates prime numbers for each round.
- **Game Simulation**: The solution determines the winner by simulating each round with optimal play by both players.

## How the Code Works

1. **Prime Generation**:
   - The `get_prime_numbers(n)` function generates a list of prime numbers between 1 and `n` using the Sieve of Eratosthenes algorithm.

2. **Game Simulation**:
   - The `isWinner(x, nums)` function simulates the Prime Game for `x` rounds.
   - In each round, the number of primes in the set determines the winner:
     - If the count of primes is even, Ben wins the round.
     - If the count of primes is odd, Maria wins the round.
   - After all rounds, the function returns the name of the player who won the most rounds or `None` if the outcome is a tie.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/prime-game.git
   ```

2. Navigate to the project directory:
   ```bash
   cd prime-game
   ```

3. Run the Python script:
   ```bash
   python3 prime_game.py
   ```

## Usage

### Function Signatures:

- **get_prime_numbers(n)**:  
  Generates a list of prime numbers from 1 to `n`.
  ```python
  def get_prime_numbers(n):
      """Generates a list of prime numbers from 1 to n (inclusive)"""
  ```

- **isWinner(x, nums)**:  
  Determines the overall winner after `x` rounds of the Prime Game.
  ```python
  def isWinner(x, nums):
      """
      Determines who wins the Prime Game after x rounds
      Args:
          x (int): number of rounds in the game
          nums (list): the upper limits of numbers used in each round
      Return:
          The name of the player who won the most rounds: 'Maria' or 'Ben'
          If no winner can be determined, returns None
      """
  ```

## Examples

Suppose there are 3 rounds with the upper limits `[4, 5, 1]`. The game will proceed as follows:

```python
x = 3
nums = [4, 5, 1]
winner = isWinner(x, nums)
print(winner)  # Outputs: Ben
```

### First round: n = 4
- Maria picks 2, removes 2 and 4, leaving [1, 3].
- Ben picks 3, removes 3, leaving [1].
- Ben wins because there are no primes left for Maria.

### Second round: n = 5
- Maria picks 2, removes 2 and 4, leaving [1, 3, 5].
- Ben picks 3, removes 3, leaving [1, 5].
- Maria picks 5, removes 5, leaving [1].
- Maria wins because there are no primes left for Ben.

### Third round: n = 1
- Ben wins because there are no primes for Maria to choose.

## Limitations

- The solution assumes optimal play by both Maria and Ben.
- The value of `n` is limited to a maximum of 10,000 to ensure performance.
