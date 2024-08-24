from collections import defaultdict, deque

class GraphBreadthFirstSearch:
    def __init__(self):
        # Initialize the adjacency list as a dictionary of lists
        self.adj_list = defaultdict(list)

    # Add edge to the graph
    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)  # If undirected graph

    # Perform BFS
    def bfs(self, start):
        visited = set()  # To track visited nodes
        queue = deque([start])  # Initialize the queue with the start node
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            # Visit all adjacent nodes
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

if __name__ == "__main__":
    graph = GraphBreadthFirstSearch()

    # Add edges to the graph
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)
    graph.add_edge(3, 7)

    print("BFS Traversal:")
    graph.bfs(1)
