"""
You are given a 2d grid of `"1"`s and `"0"`s that represents a "map". The
`"1"`s represent land and the `"0"s` represent water.

You need to write a function that, given a "map" as an argument, counts the
number of islands. Islands are defined as adjacent pieces of land that are
connected horizontally or vertically. You can also assume that the edges of the
map are surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from collections import deque

def numIslands(grid):
    # Your code here
    # PLAN
    # start at [0][0]
    # Check the value at [0][0]
    # if it's a "1" (land):
      # ...
      # kick off the BFS
      # why do we want to find all locations connected to the current one?
        # to see if you can skip the next one
        # we want to mark the connected locations as part of the same island so we can skip it/not double count it
        # store all of the locations on the same island in a "visited" array
      # increment our island count
    # if it's a "0" (water):
      # ...
      # don't do anything, check the next spot
    # Repeat for every location in the grid
    # as we repeat, if the new location has already been visited, that means it's part of an island we've already counted
      # --> skip it
    # return the number of islands
  
    # row is the first index (into the outer array)
    # col is the second index (into the inner array)
    num_islands = 0
    visited = []
    for row_idx in range(len(grid)):
      for col_idx in range(len(grid[row_idx])):
        # if it's visited, skip
        if grid[row_idx][col_idx] == 0:
          # skip it
          continue
        if grid[row_idx][col_idx] == 1:
          bfs(...)
          # need to add it to visited
          num_islands += 1

def bfs(grid, starting_location):
  pass
  # starting_location is a tuple (row_idx, col_idx)
  # From starting location, go out in each direction and add to visited array
  # need a que and a visited array
  queue = []
  visited = set()
  # add the current node to queue
  queue.append(starting_location)
  # while the queue is not empty:
  while len(queue) > 0:
    # pop off the queue
    cur_loc = queue.pop(0)
    # if we've already visited, skip it
    if cur_loc in visited:
      continue
    # "process" it / visit it
    visited.add(cur_loc)
    # add the location's outgoing edges to the queue
    row, col = cur_loc # assign first value of the tuple to row, and second to col
    # the possible edges go up, down, left, or right
    # up: [row - 1][col]
    if is_location_land(grid, row - 1, col):
      queue.append((row - 1, col))
    queue.append((row - 1, col))

    # down: [row + 1][col]
    if is_location_land(grid, row + 1, col):
      queue.append((row - 1, col))
    queue.append((row - 1, col))
    # left: [row][col - 1]
    if is_location_land(grid, row, col - 1):
      queue.append((row - 1, col))
    queue.append((row - 1, col))
    # right: [row][col + 1]
    if is_location_land(grid, row, col + 1):
      queue.append((row - 1, col))
    queue.append((row - 1, col))

  def is_location_land(grid, row, col):
    if not (0 <= row < len(grid)):
      return False
    if not (0 <= col < len(grid[row])):
      return False
    if grid[row][col] == 0:
      return False
    return True