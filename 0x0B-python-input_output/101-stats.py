#!/usr/bin/python3
'''reads the stdin and generates stats based on the input'''
import sys
import traceback
from time import sleep


def print_stats(counts_dict, size):
    print(f"File size: {size}")
    for k, v in counts_dict.items():
        if v > 0:
            print(f"{k}: {v}", end='')


status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
lines = 0
counts = dict()
for status in status_codes:
    counts[status] = 0

size = 0
numInterrupt = 0
while True:
    try:
        for i in range(10):
            line = sys.stdin.readline()
            if len(line) == 0:
                break
            line_list = line.split(" ")
            status = line_list[-2]
            size += int(line_list[-1])
            counts[status] += 1
        print_stats(counts, size)
    except KeyboardInterrupt as e:
        print_stats(counts, size)
        sleep(2)
        raise
