class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(course):
            if course in visited :
                return True
            if course in visiting :
                return False
            visiting.add(course)
            for prequisite in prereq_map[course] :
                if not dfs(prequisite) :
                    return False
            result.append(course)
            visiting.remove(course)
            visited.add(course)
            return True

        result = []
        visiting = set()
        visited = set()
        prereq_map = {i: [] for i in range(numCourses)}
        for a,b in prerequisites :
            prereq_map[a].append(b)
        
        for i in range(numCourses):
            if not dfs(i) :
                return []
        return result

        