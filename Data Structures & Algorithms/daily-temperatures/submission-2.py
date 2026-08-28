class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        p_day=[]
        
        for day in range(len(temperatures)) :
            while p_day  and temperatures[day] > temperatures[p_day[-1]] :
                popped_index = p_day.pop()
                dference = day - popped_index
                result[popped_index]=dference
            p_day.append(day)
        
        return result




