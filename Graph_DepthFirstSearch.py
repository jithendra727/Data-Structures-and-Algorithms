from collections import defaultdict

class GraphDepthFirstSearch:
    def __init__(self):
        # Initialize the adjacency list as a dictionary of lists
        self.adj_list = defaultdict(list)

    # Add edge to the graph
    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)  # If undirected graph

    # Perform DFS using recursion
    def dfs_recursive(self, start):
        visited = set()
        self._dfs_recursive_helper(start, visited)

    # Helper method for recursive DFS
    def _dfs_recursive_helper(self, node, visited):
        visited.add(node)
        print(node, end=" ")

        # Visit all adjacent nodes
        for neighbor in self.adj_list[node]:
            if neighbor not in visited:
                self._dfs_recursive_helper(neighbor, visited)

    # Perform DFS using a stack (iterative approach)
    def dfs_iterative(self, start):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)
                print(node, end=" ")

                # Push all adjacent nodes onto the stack
                for neighbor in reversed(self.adj_list[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

if __name__ == "__main__":
    graph = GraphDepthFirstSearch()

    # Add edges to the graph
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)
    graph.add_edge(3, 7)

    print("DFS Recursive:")
    graph.dfs_recursive(1)

    print("\nDFS Iterative:")
    graph.dfs_iterative(1)
