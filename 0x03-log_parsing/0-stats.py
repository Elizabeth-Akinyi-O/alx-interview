#!/usr/bin/python3

"""
Log Parsing
Write a script that reads stdin line by line and computes metrics:
"""

import sys

def print_stats(total_size, status_codes):
    """Prints the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def process_line(line, total_size, status_codes):
    """Processes a single line of input."""
    try:
        parts = line.split()
        # Get the status code and file size from the end of the line
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        
        # Update total file size
        total_size += file_size
        
        # Update status code count if it's one of the expected codes
        if status_code in status_codes:
            status_codes[status_code] += 1
            
    except (IndexError, ValueError):
        # If the line doesn't match the format, skip it
        pass
    
    return total_size

def main():
    total_size = 0
    line_count = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            total_size = process_line(line, total_size, status_codes)
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
