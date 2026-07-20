class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Build adjacency list
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):

            # Mark current node as visited
            visited.add(node)

            # Explore all neighbors
            for neighbor in graph[node]:

                # Ignore the node we just came from
                if neighbor == parent:
                    continue

                # Visited neighbor that isn't the parent -> cycle
                if neighbor in visited:
                    return False

                # Continue DFS
                if not dfs(neighbor, node):
                    return False

            return True

        # Start DFS from node 0
        if not dfs(0, -1):
            return False

        # If not all nodes were visited, graph is disconnected
        return len(visited) == n