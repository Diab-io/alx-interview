#!/usr/bin/python3
"""
module contains a script that reads stdin line by line and computes metrics
"""
import sys


http_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_size = 0


def show_information():
    """prints of the logs"""
    print("File size: {}".format(total_size))
    for code in sorted(http_codes.keys()):
        if http_codes[code]:
            print(f"{code}: {http_codes[code]}")


if __name__ == "__main__":
    count = 1
    try:
        for line in sys.stdin:
            try:
                info = line.split()
                size, code = info[-1], info[-2]
                total_size += int(size)
                if code in http_codes:
                    http_codes[code] += 1
            except Exception:
                pass
            if count == 10:
                show_information()
                count = 0
            count += 1
    except KeyboardInterrupt:
        show_information()
        raise
    show_information()
