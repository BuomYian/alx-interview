#!/usr/bin/python3
"""
A function that returns a lists of integers representing the Pascal's triangle of n:
"""
def pascal_triangle(n):
    # Check if n is less than or equal to 0
    if n <= 0:
        return [] # Return an empty list if n <= 0

    triangle = [[1]] # Initialize the triangle with the first row [1]

    # Generate each subsequent row of the triangle
    for i in range(1, n):
        row = [1] # The first element of each row is always 1

        # Calculate the remaining elements of the row
        for j in range(1, i):
            # Sum the corresponding elements from the previous row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        row.append(1) # The last element of each row is always 1
        triangle.append(row) # Add the row to the triangle

    return triangle    
