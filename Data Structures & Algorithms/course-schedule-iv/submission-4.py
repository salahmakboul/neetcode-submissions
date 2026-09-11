class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i:[] for i in range(numCourses)}
        for a,b in prerequisites :
            graph[a].append(b)
        
        result= {i:set() for i in range(numCourses)}

        def dfs(current_node,start_node) :
            neighbors = graph.get(current_node, [])
            for neighbor in neighbors :
                if neighbor in result[start_node]:
                    continue
                result[start_node].add(neighbor)
                dfs(neighbor, start_node)
        for i in range(numCourses):
            dfs(i,i)
        bolList=[]
        for u,v in queries :
            if v in result[u]:
                bolList.append(True)
            else :
                bolList.append(False)
        return bolList