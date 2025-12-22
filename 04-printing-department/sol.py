#!/usr/bin/env python3
import argparse
from typing import List
import copy

parser = argparse.ArgumentParser()
parser.add_argument('--file', help='Input file name', required=True)
args = vars(parser.parse_args())

input_file = args['file']
data: List[str] = []

with open(input_file, 'r') as f:
	data = list(filter(len, [l.strip() for l in f.readlines()]))


def get_adjacent(x: int, y: int, data) -> int:
	squares = []
	for i in range(max(x - 1, 0), min(len(data), x + 2)):
		for j in range(max(y - 1, 0), min(len(data[x]), y + 2)):
			if i == x and j == y:
				continue
			squares.append(data[i][j])
	return squares


def solve(data, part_2: bool = False) -> int:
	data2 = copy.deepcopy(data)
	total = 0
	done = False
	indexes = []
	while not done:
		count = 0
		for i in range(len(data)):
			for j in range(len(data[i])):
				adjacent = get_adjacent(i, j, data)
				if adjacent.count('@') < 4 and data[i][j] == '@':
					indexes.append((i, j))
					data2[i] = data2[i][:j] + 'x' + data2[i][j+1:]
					count += 1
		if count == 0 or not part_2:
			done = True
		if part_2:
			for x, y in indexes:
				data[x] = data2[x][:y] + '.' + data2[x][y+1:]
		total += count
	return total


print('Solution 1:', solve(data))
print('Solution 2:', solve(data, part_2=True))
