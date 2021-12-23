#!/usr/bin/python3
'''reads the stdin and generates stats based on the input'''
import sys
import traceback
from time import sleep


def print_stats(counts_dict, size):
    print(f"File size: {size}")
    for k, v in counts_dict.items():
        if v > 0:
            print(f"{k}: {v}")


status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
counts = dict()
for status in status_codes:
    counts[status] = 0

size = 0
numInterrupt = 0
lines = 0
while True:
    try:
        line = sys.stdin.readline()
        if len(line) == 0 and lines < 10:
            print_stats(counts, size)
            break
        line_list = line.split(" ")
        status = line_list[-2]
        size += int(line_list[-1])
        counts[status] += 1
        lines += 1
        if lines % 10 == 0:
            print_stats(counts, size)
    except KeyboardInterrupt as e:
        print_stats(counts, size)
        sleep(2)
        raise
