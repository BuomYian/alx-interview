#!/usr/bin/env python3
"""
A script that reads stdin line by line and computes metrics:
"""
import sys


def print_stats(file_size, status_counts):
    """
    Module that print stats

    Args:
        file_size: total file size
        status_counts: count number of status

    Returns:
        None
    """
    print("File size:", file_size)
    for status_code, count in sorted(status_counts.items()):
        print("{}: {}".format(status_code, count))


def main():
    """
    main function
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
