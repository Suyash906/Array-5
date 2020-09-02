class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0 , 0, 0, 1
        
        for instruction in instructions:
            if 'G' == instruction:
                x , y = x+dx, y+dy
            elif 'L' == instruction:
                dx, dy = -dy, dx
            elif 'R' == instruction:
                dx, dy = dy, -dx
        return (x ==0 and y == 0) or (dx !=0 or dy != 1)
