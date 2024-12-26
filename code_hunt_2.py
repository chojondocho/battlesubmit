import io
import sys
from collections import deque
from contextlib import redirect_stdout

MOD = 10**9 + 7


def solve():
    data = sys.stdin.read().strip().split()
    p = 0
    N = int(data[p])
    p += 1
    M = int(data[p])
    p += 1
    Q = int(data[p])
    p += 1
    D = int(data[p])
    p += 1

    edges = [[] for _ in range(N)]
    indeg = [0] * N

    for _ in range(M):
        a = int(data[p])
        p += 1
        b = int(data[p])
        p += 1
        w = int(data[p])
        p += 1
        a -= 1
        b -= 1
        edges[a].append((b, w))
        indeg[b] += 1

    # 위상 정렬
    q = deque()
    for i in range(N):
        if indeg[i] == 0:
            q.append(i)

    topo = []
    topo_pos = [0] * N
    idx = 0
    while q:
        x = q.popleft()
        topo.append(x)
        topo_pos[x] = idx
        idx += 1
        for nx, _ in edges[x]:
            indeg[nx] -= 1
            if indeg[nx] == 0:
                q.append(nx)

    # 쿼리 처리
    ans_list = []
    for _ in range(Q):
        u = int(data[p])
        p += 1
        v = int(data[p])
        p += 1
        u -= 1
        v -= 1
        # 위상 순서 판별
        if topo_pos[u] > topo_pos[v]:
            ans_list.append("0")
            continue

        # DP
        ans_list.append(str(process_single_query(u, v, edges, topo, topo_pos, N, D)))

    print("\n".join(ans_list))


def process_single_query(start, end, edges, topo, topo_pos, N, D):
    dp = [[0] * D for _ in range(N)]
    dp[start][0] = 1

    sPos = topo_pos[start]
    ePos = topo_pos[end]
    for i in range(sPos, ePos + 1):
        node = topo[i]
        for r in range(D):
            cnt = dp[node][r]
            if cnt == 0:
                continue
            for nx, w in edges[node]:
                if topo_pos[nx] <= ePos:
                    nr = (r + w) % D
                    dp[nx][nr] = (dp[nx][nr] + cnt) % MOD
    return dp[end][0]


def test():
    # 예제 입력
    example_input = """4 4 2 3
1 2 1
2 3 2
1 3 2
3 4 0
1 4
2 4
"""
    # 예제 출력:
    # 1
    # 0

    # 테스트
    expected_output = """1
0
"""
    backup_stdin = sys.stdin
    backup_stdout = sys.stdout
    try:
        sys.stdin = io.StringIO(example_input)
        out_buffer = io.StringIO()
        with redirect_stdout(out_buffer):
            solve()
        result = out_buffer.getvalue()
    finally:
        sys.stdin = backup_stdin
        sys.stdout = backup_stdout

    print("[테스트 입력]\n", example_input, sep="")
    print("[예상 출력]\n", expected_output, sep="")
    print("[실제 출력]\n", result, sep="")
    if result == expected_output:
        print("[결과] 성공")
    else:
        print("[결과] 실패")


if __name__ == "__main__":
    # 이 스크립트를 그대로 실행하면, test()를 수행하여 예제 검증을 진행합니다.
    test()
