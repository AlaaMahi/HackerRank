#!/usr/bin/env python

"""combinations.py: computing combinations."""

__author__      = "Alaa Eddine MAHI"
__copyright__   = "Copyright 2020, Quantitative Interviews"
__license__ = "GNU"
__version__ = "3.0"

import sys
data = sys.stdin.readlines()

def minimal_path_sum(data):
  matrix = [line.rstrip('\n') for line in data[1:]]
  matrix = [list(map(int, row.split())) for row in matrix]

  size = int(data[0])
  # calculate minimal sums for bottom row and last column
  # as they don't have any other way to be reached
  for i in reversed(range(0, size - 1)):
    matrix[size - 1][i] += matrix[size - 1][i + 1]
    matrix[i][size - 1] += matrix[i + 1][size - 1]

  for i in reversed(range(0, size - 1)):
    for j in reversed(range(0, size - 1)):
      matrix[i][j] += min(matrix[i + 1][j], matrix[i][j + 1])

  return matrix[0][0]

print(minimal_path_sum(data))