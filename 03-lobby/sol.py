#!/usr/bin/env python3
import argparse
from typing import List

parser = argparse.ArgumentParser()
parser.add_argument('--file', help='Input file name', required=True)
args = vars(parser.parse_args())

input_file = args['file']
data: List[str] = []

with open(input_file, 'r') as f:
	data = list(filter(len, [l.strip() for l in f.readlines()]))


def _compute_joltage(batteries: str, total_nums: int = 2) -> int:
	_numbers: List[str] = []
	idx = 0
	for j in range(1, total_nums + 1)[::-1]:
		_largest = -1
		for i in range(idx, len(batteries) + 1 - j):
			if int(batteries[i]) > _largest:
				_largest = int(batteries[i])
				idx = i
			if _largest == 9:
				break
		_numbers.append(str(_largest))
		idx += 1
	return int(''.join(_numbers))


def solve(data, part_2: bool = False) -> int:
	_sum = 0
	for arr in data:
		total_nums = 12 if part_2 else 2
		num = _compute_joltage(arr, total_nums=total_nums)
		_sum += num
	return _sum


print('Solution 1:', solve(data))
print('Solution 2:', solve(data, part_2=True))
