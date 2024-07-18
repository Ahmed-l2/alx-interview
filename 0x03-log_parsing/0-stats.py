#!/usr/bin/python3
"""Module for stats function"""
import re
import sys


def stats():
    """reads stdin line by line and computes metrics"""
    file_size = 0
    status_codes = {}
    counter = 0

    try:
        for line in sys.stdin:
            pattern = (
                r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \['
                r'(.*?)\] "GET /projects/260 HTTP/1.1" '
                r'(\d{3}) (\d+)'
            )
            match = re.search(pattern, line)
            if match:
                counter += 1
                scode = match.group(3)
                fsize = match.group(4)
                if scode in status_codes:
                    status_codes[scode] += 1
                else:
                    status_codes[scode] = 1
                file_size += int(fsize)

            if counter >= 10:
                print_stats(file_size, status_codes)
                counter = 0

    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise


def print_stats(file_size, status_codes):
    """Prints the statistics"""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    stats()
