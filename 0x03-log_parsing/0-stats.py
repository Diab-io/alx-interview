#!/usr/bin/python3
"""
Tis script computes metric based on logs passed
into the stdin
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
    """This prints the computed info got from the logs"""
    print("File size: {}".format(total_size))
    for code in sorted(http_codes.keys()):
        if http_codes[code]:
            print("{}: {}".format(code, http_codes[code]))


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
