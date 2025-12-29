#!/usr/bin/env python3
import argparse
from typing import List, Set, Tuple
from functools import lru_cache
import copy
import math


parser = argparse.ArgumentParser()
parser.add_argument('--file', help='Input file name', required=True)
parser.add_argument('--pairs', help='Wire pairs', required=True)
args = vars(parser.parse_args())

input_file = args['file']
pairs = int(args['pairs'])


@lru_cache(maxsize=None)
def compute_distance(x1, y1, z1, x2, y2, z2) -> float:
    return math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2 + (z2-z1) ** 2)


with open(input_file, 'r') as f:
    points = [[int(x), int(y), int(z)] for (x,y,z) in [x.strip().split(',') for x in list(filter(len, f.readlines()))]]


def build_edges(points: List[List[int]]) -> List[Tuple[float, int, int]]:
    edges = []
    n = len(points)

    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            d = compute_distance(x1, y1, z1, x2, y2, z2)
            edges.append((d, i, j))

    edges.sort(key=lambda e: e[0])
    return edges


def solve(points: List[int], pairs: int, part_2: bool = False) -> int:
    n = len(points)
    edges = build_edges(points)

    parent = list(range(n))
    size = [1] * n
    components = n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        nonlocal components
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
        size[ra] += size[rb]
        components -= 1
        return True

    if part_2:
        for _, i, j in edges:
            if union(i, j) and components == 1:
                return points[i][0] * points[j][0]

    for _, i, j in edges[:pairs]:
        union(i, j)
    comp_sizes = {}
    for i in range(n):
        r = find(i)
        comp_sizes[r] = comp_sizes.get(r, 0) + 1
    sizes = sorted(comp_sizes.values(), reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


print('Solution 1:', solve(points, pairs))
print('Solution 2:', solve(points, pairs, part_2=True))
