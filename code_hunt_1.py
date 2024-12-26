import io
import sys
from contextlib import redirect_stdout


def test_solve(example_input, expected_output):
    """
    example_input : 문자열로 된 예제 입력
    expected_output : 우리가 기대하는 출력 (문자열)

    1) stdin을 example_input으로 대체
    2) stdout을 StringIO로 받아옴
    3) solve() 실행
    4) 실제 출력 결과와 expected_output 비교
    """
    backup_stdin = sys.stdin
    backup_stdout = sys.stdout
    try:
        sys.stdin = io.StringIO(example_input)
        output_buffer = io.StringIO()
        with redirect_stdout(output_buffer):
            solve()
        result = output_buffer.getvalue().strip()
    finally:
        sys.stdin = backup_stdin
        sys.stdout = backup_stdout

    print("[입력]")
    print(example_input)
    print("[예상 출력]")
    print(expected_output)
    print("[실제 출력]")
    print(result)
    print("[테스트 결과]", "성공" if result == expected_output else "실패", "\n")


# 아래는 실제 예제를 테스트하는 부분입니다.
# -----------------------------------------
# 1) solve() 함수가 정의되어 있어야 합니다.
# 2) test_solve() 함수를 호출하여 결과를 확인합니다.


def solve():
    import heapq
    import sys

    input = sys.stdin.readline

    N, M, K = map(int, input().split())
    colors = [int(input()) for _ in range(N)]
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))

    INF = float("inf")
    dist = [[INF] * (1 << K) for _ in range(N)]

    # "정점 1"에서 출발하도록 고정
    start_mask = 1 << (colors[0] - 1)
    dist[0][start_mask] = 0
    pq = []
    heapq.heappush(pq, (0, 0, start_mask))

    ALL = (1 << K) - 1
    while pq:
        cost, v, mask = heapq.heappop(pq)
        if cost > dist[v][mask]:
            continue
        if mask == ALL:
            print(cost)
            return
        for nxt, wcost in graph[v]:
            nmask = mask | (1 << (colors[nxt] - 1))
            ncost = cost + wcost
            if dist[nxt][nmask] > ncost:
                dist[nxt][nmask] = ncost
                heapq.heappush(pq, (ncost, nxt, nmask))

    ans = min(dist[v][ALL] for v in range(N))
    print(ans if ans < INF else -1)


# 예제 1
input_data_1 = """5 6 2
1
1
2
1
2
1 2 3
2 3 4
2 4 7
1 5 10
5 3 2
4 3 1
"""
expected_output_1 = "7"

# 예제 2
input_data_2 = """4 4 3
1
2
3
3
1 2 2
2 3 2
2 4 5
3 4 1
"""
expected_output_2 = "-1"

# 두 예제를 테스트한다.
test_solve(input_data_1, expected_output_1)
test_solve(input_data_2, expected_output_2)
