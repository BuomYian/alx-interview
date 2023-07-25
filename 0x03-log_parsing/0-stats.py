#!/usr/bin/python3
"""
Metrics Computation Script

This script reads input from standard input (stdin) line by line and computes
metrics based on the provided input format. The metrics include total file size
and the number of lines for each valid status code. The results are printed
every 10 lines or when a keyboard interruption (CTRL + C) occurs.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Required Environment:
- Ubuntu 14.04 LTS
- Python 3.4.3
- PEP 8 style (version 1.7.x)
Usage: ./0-stats.py

Author: Buomkuoth Yian
Date: 20th July
"""
import sys


def print_stats(file_size, status_counts):
    """
    Print the computed statistics.

    Args:
        file_size (int): The total file size.
        status_counts (dict): A dictionary containing the count of each status code.

    Returns:
        None
    """
    print("File size:", file_size)
    for status_code, count in sorted(status_counts.items()):
        print("{}: {}".format(status_code, count))


def main():
    """
    Main function to compute metrics from stdin input.

    Returns:
        None
    """
    total_file_size = 0
    status_counts = {}

    try:
        for line_count, line in enumerate(sys.stdin, 1):
            try:
                _, _, _, status_code, file_size = line.split()[
                    0], line.split()[-2], line.split()[-1]
                file_size = int(file_size)
                status_code = int(status_code)
            except ValueError:
                # Skip invalid lines
                continue

            total_file_size += file_size
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_counts[status_code] = status_counts.get(
                    status_code, 0) + 1

            if line_count % 10 == 0:
                print_stats(total_file_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_file_size, status_counts)
        raise


if __name__ == "__main__":
    main()
