import heapq

graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('D', 1)],
    'C': [('B', 2), ('D', 5)],
    'D': []
}

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}   # everything starts "infinitely far"
    dist[start] = 0
    pq = [(0, start)]                               # (distance, node)

    while pq:
        d, node = heapq.heappop(pq)     # grab the closest place so far

        if d > dist[node]:                          # old, outdated entry, skip it
            continue

        for neighbor, weight in graph[node]:
            new_d = d + weight
            if new_d < dist[neighbor]:              # found a shorter way
                dist[neighbor] = new_d
                heapq.heappush(pq, (new_d, neighbor))

    return dist
