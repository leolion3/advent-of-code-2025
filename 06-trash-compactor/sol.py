#!/usr/bin/env python3
import argparse
from typing import List, Set
import copy


parser = argparse.ArgumentParser()
parser.add_argument('--file', help='Input file name', required=True)
args = vars(parser.parse_args())

input_file = args['file']


with open(input_file, 'r') as f:
	lines = list(filter(len, [x.replace('\n', '') for x in f.readlines()]))
	indexes = []
	idx = 0
	for i, char in enumerate(list(lines[-1])):
		if char in ['*', '+', '/', '-']:
			if i != 0:
				indexes.append((idx, i-1))
				idx = i
	indexes.append((idx, len(list(lines[-1])) + 1))
	matrix = []
	for start, finish in indexes:
		_row = []
		for row in lines[:-1]:
			_row.append(row[start:finish])
		matrix.append(_row)
	matrix.append(list(filter(len, lines[-1].split(' '))))


def solve(matrix: List[List[str]], part_2: bool = False) -> int:
	if part_2:
		_matrix = []
		for row in matrix[:-1]:
			new_cols = []
			for col in row:
				chars = list(col)
				if not len(new_cols):
					new_cols = chars
				else:
					for i, char in enumerate(chars):
						new_cols[i] += char
			_matrix.append(new_cols[::-1])
		_matrix.append(matrix[-1])
		matrix = _matrix
	return sum([eval(f'{matrix[-1][i]}'.join(list(row))) for i, row in enumerate(matrix[:-1])])


print('Solution 1:', solve(matrix))
print('Solution 2:', solve(matrix, part_2=True))
