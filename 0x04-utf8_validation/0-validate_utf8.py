#!/usr/bin/python3
"""
Validates if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    # Helper function to check if a byte is a valid UTF-8 start byte
    def is_start_byte(byte):
        return (byte >> 7) == 0 or (byte >> 5) == 0b110 or (byte >> 4) == 0b1110 or (byte >> 3) == 0b11110

    # Helper function to check if a byte is a valid UTF-8 following byte
    def is_following_byte(byte):
        return (byte >> 6) == 0b10

    # Iterate through each byte in the data
    i = 0
    while i < len(data):
        byte = data[i]

        # Check if it's a valid start byte
        if not is_start_byte(byte):
            return False

        # Determine the number of bytes in the character
        if (byte >> 7) == 0:      # 1-byte character
            length = 1
        elif (byte >> 5) == 0b110:  # 2-byte character
            length = 2
        elif (byte >> 4) == 0b1110:  # 3-byte character
            length = 3
        elif (byte >> 3) == 0b11110:  # 4-byte character
            length = 4
        else:
            return False  # Invalid start byte

        # Check the following bytes
        for j in range(1, length):
            i += 1
            if i >= len(data) or not is_following_byte(data[i]):
                return False

        i += 1

    return True
