# from pyMaze import maze,agent,COLOR
# def Bfs(m):
#     start=(m.rows,m.cols)
#     front=[start]
#     visited=[start]
#     path={}
#     while(len(front)>0):
#         currcell=front.pop(0)
#         if(currcell==(1,1)): 
#             break
#         for d in "ESNW":
#             if m.maze_map[currcell][d]==True:
#                 if d== "E":
#                     childcell=(currcell[0],currcell[1]+1)
#                 elif d== "W":
#                     childcell=(currcell[0],currcell[1]-1)
#                 elif d== "N":
#                     childcell=(currcell[0]-1,currcell[1]-1)
#                 elif d== "S":
#                     childcell=(currcell[0]+1,currcell[1]-1)
#                 if childcell in visited:
#                     continue
#                 front.append(childcell)
#                 visited.append(childcell)
#                 path[childcell]=currcell
#     straightPath={}
#     cell=(1,1)
#     while cell !=start:
#         straightPath[path[cell]]=cell
#         cell=path[cell]
#     return straightPath
# m=maze()
# m.CreateMaze()
# pa=Bfs(m)
# A=agent(m)
# m.tracePath({a:pa})
# m.run()
from pyMaze import maze,agent,COLOR,textLabel
from collections import deque
def BFS(m):
    start=(m.rows,m.cols)
    frontier=deque()
    explored=[start]
    bfsPath={}
    while len(frontier)>0:
        currCell=frontier.popleft()
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath

if __name__=='__main__':
    m=maze(5,7)
    m.CreateMaze(pattern='h')
    path=BFS(m)
    path={(1,2),(1,3)}
    a=agent(m,color="black")
    m.tracePath({a:path})
    l=textLabel(m,'Length of Shortest Path',len(path)+1)

    m.run()