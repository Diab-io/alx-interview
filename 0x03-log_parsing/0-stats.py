#!/usr/bin/python3
"""
module contains a script that reads stdin line by line and computes metrics
"""
import sys


http_codes = {
    "200": 0, "301": 0,
    "400": 0, "401": 0,
    "403": 0, "404": 0,
    "405": 0, "500": 0
}

total_size = 0


def show_information():
    """prints of the logs"""
    print("File size: {}".format(total_size))
    for status in sorted(http_codes.keys()):
        if http_codes[status]:
            print("{}: {}".format(status, http_codes[status]))


if __name__ == "__main__":
    count = 0
    try:
        for line in sys.stdin:
            try:
                elems = line.split()
                total_size += int(elems[-1])
                if elems[-2] in http_codes:
                    http_codes[elems[-2]] += 1
            except Exception:
                pass
            if count == 9:
                show_information()
                count = -1
            count += 1
    except KeyboardInterrupt:
        show_information()
        raise
    show_information()
