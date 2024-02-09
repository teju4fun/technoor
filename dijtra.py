import heapq

def dijkstra(graph, start_node):
    """
    Implements Dijkstra's algorithm to find the shortest paths from a start node
    to all other nodes in a weighted graph.

    Args:
        graph (dict): A dictionary representing the graph, where keys are nodes and
                      values are dictionaries mapping neighboring nodes to edge weights.
        start_node (int): The node where the search starts.

    Returns:
        dict: A dictionary containing the shortest distances from the start node to
              each other node, or None if there's no path.
    """

    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    visited = set()
    pq = [(0, start_node)]  # Use a priority queue with (distance, node) tuples

    while pq:
        dist, node = heapq.heappop(pq)  # Get the node with the smallest distance so far

        if node in visited:
            continue  # Skip already visited nodes

        visited.add(node)

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))  # Update or add to priority queue

    return distances  # Return the final distances dictionary

# Example usage
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 3, 'D': 2},
    'C': {'A': 2, 'B': 3, 'D': 1, 'E': 3},
    'D': {'B': 2, 'C': 1, 'E': 1},
    'E': {'C': 3, 'D': 1}
}

shortest_paths = dijkstra(graph, 'A')

print("Shortest paths from node A:")
for node, distance in shortest_paths.items():
    print(f"  - {node}: {distance} (if no path, distance is infinity)")
