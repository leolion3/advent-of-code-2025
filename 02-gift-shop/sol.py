#!/usr/bin/env python3
import argparse
from typing import List

parser = argparse.ArgumentParser()
parser.add_argument('--file', help='Input file name', required=True)
args = vars(parser.parse_args())

input_file = args['file']
data: List[str] = []

with open(input_file, 'r') as f:
	data = f.read().strip().replace('\n', '').split(',')


def is_invalid_id(s: str) -> bool:
    return s in (s + s)[1:-1]


def solve(data, part_2: bool = False) -> int:
	_sum = 0
	for val in data:
		_start, _end = [int(i) for i in val.split('-')]
		for num in range(_start, _end + 1):
			num = str(num)
			pivot = int(len(num) / 2)
			if num.startswith('0'):
				_sum += int(num)
			elif num[0:pivot] == num[pivot:] and not part_2:
				_sum += int(num)
			elif part_2 and is_invalid_id(num):
				_sum += int(num)
	return _sum


print('Solution 1:', solve(data))
print('Solution 2:', solve(data, part_2=True))
