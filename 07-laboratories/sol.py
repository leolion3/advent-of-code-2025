#!/usr/bin/env python3
import argparse
from typing import List, Tuple
import copy
from functools import lru_cache

parser = argparse.ArgumentParser()
parser.add_argument('--file', help='Input file name', required=True)
args = vars(parser.parse_args())

input_file = args['file']
data: List[str] = []
seen = []

with open(input_file, 'r') as f:
	data = list(filter(len, [l.strip() for l in f.readlines()]))


@lru_cache(maxsize=None)
def shine_beam(pos_x: int, pos_y: int, part_2: bool) -> int:
	if not part_2:
		shine_beam.cache_clear()
	pos_y += 1
	if not part_2 and (pos_x, pos_y) in seen:
		return 0
	if not part_2:
		seen.append((pos_x, pos_y))
	if pos_y >= len(data):
		if part_2:
			return 1
		return 0
	if pos_x < 0 or pos_x >= len(data[pos_y]):
		if part_2:
			return 1
		return 0
	if data[pos_y][pos_x] != '.':
		_sum = 1
		if part_2:
			_sum = 0
		return _sum + shine_beam(pos_x - 1, pos_y, part_2) + shine_beam(pos_x + 1, pos_y, part_2)
	return shine_beam(pos_x, pos_y, part_2)


def find_start(data: List[str]) -> Tuple[int, int]:
	for y, row in enumerate(data):
		for x, char in enumerate(list(row)):
			if char == 'S':
				return (x, y)
	return -1


def solve(data, part_2: bool) -> int:
	pos_x, pos_y = find_start(data)
	return shine_beam(pos_x, pos_y, part_2)


print('Solution 1:', solve(data, part_2=False))
print('Solution 2:', solve(data, part_2=True))
