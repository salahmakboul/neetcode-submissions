class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i:[] for i in range(numCourses)}
        for a,b in prequisites :
            graph[a].append(b)
        
        result= {i:set() for i in range(numCourses)}

        def dfs(current_node,start_node) :
            neighbors = {u if current_node == v else v for u,v in graph if current_node in (u,v)}
            for neighbor in neighbors :
                if neighbor in result[start_node]:
                    continue
                result[start_node].append(neighbor)
                dfs(current_node, start_node)
        for i in range(numCourses):
            dfs(i,i)
        bolList=[]
        for u,v in queries :
            if v in result[u]:
                bolList.append(True)
            else :
                bolList.append(False)
        return bolList