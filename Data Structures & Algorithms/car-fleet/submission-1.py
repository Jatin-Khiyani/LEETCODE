class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        pair = []

        for p,s in zip(position,speed):
            pair.append([p,s])
        
        pair = sorted(pair)[::-1]

        for p,s in pair:
            time = (target-p)/s
            stack.append(time)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)


                
        