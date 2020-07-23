import random
length = 10
step = 3
maze = [[random.randint(0,length) for i in range(length)] for j in range(length) ]


start = (0,0)
end = (random.randint(length*3//4, length-1),random.randint(length*3//4, length-1))
def dfs(maze,start,end,step):
    stack = []
    stack.append(start)
    used = set()
    def getneighbor(maze,start,steps):
        i,j = start
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        res = []
        old_val = maze[i][j]
        path = False
        for d in direction:
            new_i = i + d[0]
            new_j = j + d[1]
            if new_i >= 0 and new_i < len(maze) and new_j >= 0 and new_j < len(maze[0]) and (new_i,new_j) not in used:
                if maze[new_i][new_j] >= old_val-step and maze[new_i][new_j] <= old_val+step:
                    res.append((new_i,new_j))
                    path = True
                elif not path:
                    maze[new_i][new_j] = random.randint(old_val-step,old_val+step)
                    res.append((new_i,new_j))
                    path = True
                    
        return res
    while stack:
        cur = stack.pop()
        if cur == end:
            return
        neighbor = getneighbor(maze,cur,step) 
        if neighbor:
            for nei in neighbor:
                stack.append(nei)
                used.add(nei)
            
dfs(maze,start,end,step)
for i in range(len(maze)):
    print(maze[i], end = '\n')
    
    
    