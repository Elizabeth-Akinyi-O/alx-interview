#!/usr/bin/python3
"""Log Parsing
Write a script that reads stdin line by line and computes metrics.
"""
import sys

total_file_size = 0
status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_count = dict.fromkeys(status_codes, 0)


def print_log_stats():
    """Prints accumulated metrics."""
    print("File size: {}".format(total_file_size))
    for key, value in sorted(status_count.items()):
        if value > 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    count = 0
    try:
        for line in sys.stdin:
            line = line.split()
            count += 1
            try:
                # Parse file size
                total_file_size += int(line[-1])

                # Parse and update status code count
                if line[-2] in status_codes:
                    status_count[line[-2]] += 1

            except (IndexError, ValueError):
                # Skip lines that do not conform to the expected format
                pass

            # Every 10 lines, print the current stats
            if count % 10 == 0:
                print_log_stats()
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C) gracefully
        pass
    finally:
        # Print the final log stats
        print_log_stats()
