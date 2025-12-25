#!/usr/bin/env python3
import argparse
from typing import List, Set
import copy

parser = argparse.ArgumentParser()
parser.add_argument('--file', help='Input file name', required=True)
args = vars(parser.parse_args())

input_file = args['file']
ranges: List[List[int]] = []
inputs: Set[int] = set()


with open(input_file, 'r') as f:
	data = list(filter(len, [l.strip() for l in f.readlines()]))
	for row in data:
		if '-' in row:
			ranges.append([int(x) for x in row.strip().split('-')])
		else:
			inputs.add(int(row.strip()))


def merge_ranges(ranges):
    ranges = sorted(ranges)
    merged = [ranges[0]]
    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1] = [last_start, max(last_end, end)]
        else:
            merged.append([start, end])
    return merged


def solve(ranges: List[List[int]], inputs: List[int], part_2: bool = False) -> int:
	_sum: int = 0
	if part_2:
		for _range in ranges:
			_sum += _range[1] + 1 - _range[0]
		return _sum
	for i in inputs:
		for _range in ranges:
			if _range[0] <= i <= _range[1]:
				_sum += 1
				break
	return _sum


ranges = merge_ranges(ranges)
print('Solution 1:', solve(ranges, inputs))
print('Solution 2:', solve(ranges, inputs, part_2=True))
