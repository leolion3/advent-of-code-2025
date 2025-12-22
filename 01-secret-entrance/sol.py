#!/usr/bin/env python3
import argparse
from typing import List

parser = argparse.ArgumentParser()
parser.add_argument('--file', help='Input file name', required=True)
args = vars(parser.parse_args())

input_file = args['file']
data: List[str] = []

with open(input_file, 'r') as f:
	data = [l.strip() for l in f.readlines()]


def sol_1(rotations: List[str], pos: int = 50, use_other_method: bool = False) -> int:
	zeros = 0
	all_steps = []
	for rotation in rotations:
		left = 'L' in rotation
		for step in range(int(rotation.replace('L', '').replace('R', ''))):
			if left:
				pos -= 1
			else:
				pos += 1
			if pos > 99:
				pos = 0
			elif pos < 0:
				pos = 99
			all_steps.append(pos)
		if not use_other_method and pos == 0:
			zeros += 1
	if use_other_method:
		return all_steps.count(0)
	return zeros


print('Solution 1:', sol_1(data))
print('Solution 2:', sol_1(data, use_other_method=True))
