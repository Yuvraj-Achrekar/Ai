#Solve the block of World problem.

class  point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
def evalPointOnline(p, curLine):
    eval = curLine.a*p.x + curLine.b*p.y + curLine.c
    if (eval > 0):
        return 1
    return -1
def minJumpToReachDestination(start, dest, lines, N):
    jumps = 0
    for i in range(N):
        signStart = evalPointOnline(start, lines[i])
        signDest = evalPointOnline(dest, lines[i])
        if (signStart * signDest < 0):
            jumps = jumps+1
    return jumps
start = point(1, 1)
dest = point(-2, -1)
lines = []
lines.append(line(1,0,0))
lines.append(line(0,1,0))
lines.append(line(1,1,-2))
print(minJumpToReachDestination(start, dest, lines, 3))