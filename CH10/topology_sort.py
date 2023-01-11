from collections import deque


def topology_sort(graph, indegree):
    result = []
    queue = deque()
    v = len(graph) - 1
    for i in range(1, v+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    return result
