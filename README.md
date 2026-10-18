# Homework 1 – Algorithmic Methods of Data Mining

**Hermela Asfaw Birhane** · Data Science, Sapienza University of Rome · 2026

This repository contains my solutions to Homework 1. The goal of the homework was to build up basic Python programming skills through HackerRank challenges (Problem 1) and then use them to implement a few simple algorithms (Problem 2).

All the required challenges are solved and accepted on HackerRank: **91 challenges for Problem 1 and 6 for Problem 2**.

## Repository structure

```
.
├── README.md                          # this file
├── scripts.py                         # all solutions, one function per challenge
└── printouts/
    └── hackerrank_submissions.pdf     # printout of my HackerRank submissions page
```

The PDF in `printouts/` is the printout of my submissions page on HackerRank (hackerrank.com/submissions/all). It lists every submission in the order I made them, with its language, result and score.

## Problem 1 – Python challenges

| Section | Challenges | What it covers |
|---|---|---|
| Introduction | 7 | input/output, conditions, loops, simple functions |
| Basic Data Types | 6 | lists, list comprehensions, tuples, nested lists |
| Strings | 14 | slicing, formatting, alignment, string methods |
| Sets | 13 | set operations (union, intersection, difference, …) and mutations |
| Collections | 8 | `Counter`, `defaultdict`, `namedtuple`, `OrderedDict`, `deque` |
| Date and Time | 2 | `calendar` and `datetime` with time zones |
| Exceptions | 1 | handling `ZeroDivisionError` and `ValueError` |
| Built-ins | 3 | `zip`, sorting with custom keys |
| Python Functionals | 1 | `map` and `lambda` |
| Regex and Parsing | 17 | regular expressions, lookaheads/lookbehinds, `HTMLParser`, input validation |
| XML | 2 | recursion over an XML tree with `ElementTree` |
| Closures and Decorators | 2 | writing decorators that wrap a function |
| NumPy | 15 | arrays, reshaping, element-wise math, linear algebra, statistics |

## Problem 2 – Algorithms

| Challenge | Approach | Time complexity |
|---|---|---|
| Birthday Cake Candles | count how many times the maximum appears | O(n) |
| Number Line Jumps | the kangaroos meet only if the distance between them is a non-negative multiple of their speed difference | O(1) |
| Viral Advertising | simulate the sharing day by day | O(n) |
| Recursive Digit Sum | sum the digits of `n` once and multiply by `k` instead of building the repeated string | O(d), d = digits of `n` |
| Insertion Sort – Part 1 | shift larger elements right until the last element fits, printing each step | O(n) |
| Insertion Sort – Part 2 | full insertion sort, printing the array after each pass | O(n²) |

## How to use `scripts.py`

The file is organized in the same order as the tables above, with a numbered comment before each solution.

On HackerRank the code reads from standard input. Here I rewrote each solution as a function that takes the challenge's input as arguments, so any of them can be imported and tested directly:

```python
from scripts import kangaroo, recursive_digit_sum, insertion_sort_part_2

print(kangaroo(0, 3, 4, 2))             # YES
print(recursive_digit_sum("148", 3))    # 3
insertion_sort_part_2([1, 4, 3, 5, 6, 2])
# 1 4 3 5 6 2
# 1 3 4 5 6 2
# 1 3 4 5 6 2
# 1 3 4 5 6 2
# 1 2 3 4 5 6
```

**Requirements:** Python 3 and NumPy (`pip install numpy`). Everything else comes from the standard library.

## Notes

- Some functions print their result and others return it. I kept the same behaviour as the original HackerRank challenge, which sometimes asks for a printed output and sometimes for a function's return value.
- **Tuples:** Python 3.8 changed the way tuples are hashed, so `hash(t)` no longer matches the expected output on HackerRank. The solution reproduces the older hash algorithm instead.
- **NumPy printing:** a few NumPy challenges use `np.printoptions(legacy="1.13")` or rounding, because HackerRank's expected output uses the older NumPy print format.
