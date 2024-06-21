#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys
import signal
import re

total_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                      404: 0, 405: 0, 500: 0}
line_count = 0

# Define the regular expression pattern
log_pattern = re.compile(
    r'(\d{1,3}\.){3}\d{1,3} - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
)


def print_stats():
    """Print the statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """Handle the keyboard interruption signal."""
    print_stats()
    sys.exit(0)


# Register the signal handler for (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            try:
                # Extract status code and file size from the matched groups
                status_code = int(match.group(2))
                file_size = int(match.group(3))

                # Update metrics
                total_size += file_size
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

                line_count += 1

                if line_count % 10 == 0:
                    print_stats()

            except ValueError:
                continue

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

# Print final stats if the script ends normally
print_stats()
