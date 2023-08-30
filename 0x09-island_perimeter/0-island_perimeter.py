#!/usr/bin/python3
"""
Module for island perimeter calculation
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.

    Args:
        grid: The grid representing the island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                perimeter += 4  # Add 4 to the perimter of each land cell

                # Check left cell
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Subtract 2 if the left cell is land

                # Check top cell
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Subtract 2 if the top cell is land

    return perimeter
