#!/usr/bin/python3
""" Module that helps compute stats of a log """
import sys


http_codes = {
    '200': 0, '301': 0, '400': 0,
    '401': 0, '403': 0, '404': 0,
    '405': 0, '500': 0
}

total_size = 0


def show_information() -> None:
    """ This function displays the stats got from the logs """
    print(f"File size: {total_size}")
    for code in sorted(http_codes.keys()):
        if http_codes[code]:
            print(f"{code}: {http_codes[code]}")


if __name__ == '__main__':
    count = 1
    try:
        for line in sys.stdin:
            try:
                info = line.split()
                code, size = info[-2], info[-1]
                total_size += int(size)
                if code in http_codes.keys():
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
