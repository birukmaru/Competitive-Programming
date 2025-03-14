class Solution:
    def shortestToChar(self, s: str, c: str):
        c_index = []
        res = []
        min_dis = float("inf")

        for i in range(len(s)):
            if s[i] == c:
                c_index.append(i)
        
        for i in range(len(s)):
            for num in c_index:
                curr_dis =  abs(num - i)
                min_dis = min(curr_dis, min_dis)
            res.append(min_dis)
            min_dis = float("inf") 
            
        return res