#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6x6 그리드에서 (1,1) ~ (6,6)의 최단 거리 계산
필즈상 수상자 & 세계 최고의 해커 정신으로 작성
"""

from collections import deque
from typing import List


def find_shortest_path(grid: List[List[int]]) -> int:
    """
    6x6 격자에서 (0,0)부터 (5,5)까지의 최단 이동 횟수를 BFS로 계산한다.
    0: 이동 가능
    1: 이동 불가능
    도달 불가 시 -1 반환
    """
    # 시작점 혹은 도착점이 벽인 경우, 바로 -1
    if grid[0][0] == 1 or grid[5][5] == 1:
        return -1

    visited = [[False] * 6 for _ in range(6)]
    dist = [[0] * 6 for _ in range(6)]

    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    dist[0][0] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()

        # 목표 지점 확인
        if (r, c) == (5, 5):
            return dist[r][c]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 6 and 0 <= nc < 6:
                if grid[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

    return -1  # 도착점에 끝내 도달하지 못하면 -1


def main():
    """
    예제 격자를 직접 정의하고, BFS로 최단 거리를 출력한다.
    - 추가로, 경로가 없는 경우도 테스트하여 -1이 출력되는지 확인.
    """
    # 예제 1: 문제에서 주어진 이동 가능 격자 (결과: 10)
    sample_grid_1 = [
        [0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
    ]
    result1 = find_shortest_path(sample_grid_1)
    print(f"[예제 1] 최단 이동 횟수: {result1}")  # 기대값: 10

    # 예제 2: 시작점 또는 도착점이 벽인 경우 (결과: -1)
    # 여기서는 도착점(5,5)을 벽으로 설정
    sample_grid_2 = [
        [0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1],  # 맨 끝(5,5)을 1로 만들어서 벽 처리
    ]
    result2 = find_shortest_path(sample_grid_2)
    print(f"[예제 2] 최단 이동 횟수: {result2}")  # 기대값: -1


if __name__ == "__main__":
    main()
