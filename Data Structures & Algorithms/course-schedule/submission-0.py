class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course):
            if course in visited :
                return True
            if course in visiting :
                return False
            visiting.add(course)
            for prequisite in prereq_map[course] :
                if not dfs(prequisite) :
                    return False
            visiting.remove(course)
            visited.add(course)
            return True

        visiting = set()
        visited = set()
        prereq_map = {i: [] for i in range(numCourses)}
        for a,b in prerequisites :
            prereq_map[a].append(b)
        
        for i in range(numCourses):
            if not dfs(i) :
                return False
        return True


        

        