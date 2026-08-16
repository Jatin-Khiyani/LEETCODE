class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s = sorted(s)
        t = sorted(t)
        
        if len(s) != len(t):
            return False
        else:
            for s_value,t_value in zip(s,t):
                if s_value == t_value:
                    continue
                else:
                    return False
            return True