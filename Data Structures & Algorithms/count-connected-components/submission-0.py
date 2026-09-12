class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        components = n
        def find_leader(node) :
            while parent[node] != node: node = parent[node]
            return node
        for u,v in edges :
            leader_u = find_leader(u)
            leader_v = find_leader(v)
            if leader_u != leader_v :
                parent[leader_u] = leader_v
                components -= 1
            elif leader_u == leader_v :continue
        return components

        