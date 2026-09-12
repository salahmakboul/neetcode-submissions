class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent = [i for i in range(n + 1)]
        def find_leader(node) :
            while parent[node]!= node :
                node = parent[node]
            return node
        for u,v in edges :
            leader_u=find_leader(u)
            leader_v=find_leader(v)
            if leader_u == leader_v :
                return [u,v]
            elif leader_u != leader_v :
                parent[leader_u] = leader_v

        



        