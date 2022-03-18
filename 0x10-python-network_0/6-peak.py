#!/usr/bin/python3
"""defines a function that finds the peak of a
list of integers"""


def find_peak(nums: list) -> int:
    """finds the highest integer"""
    if nums is None or len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]

    mid = len(nums) // 2
    if (mid == 0 or nums[mid - 1] < nums[mid]) and\
       (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
        return nums[mid]
    if (mid - 1 >= 0) and (nums[mid - 1] >= nums[mid]):
        return find_peak(nums[:mid])

    return find_peak(nums[mid + 1:])
