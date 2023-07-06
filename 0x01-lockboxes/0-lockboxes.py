#!/usr/bin/python3
"""
Method that determines if all boxes are open
"""


def canUnlockAll(boxes):
    """Check if all boxes can be opened."""
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()

        # Check all the keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box that hasn't been visited
            if key < num_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    # Check if all boxes have been visited
    return all(visited)
