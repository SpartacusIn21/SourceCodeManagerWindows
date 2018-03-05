def ConstructPath(p, i, j):
    print("construct path %d to %d"%(i,j))
    i,j = int(i), int(j)
    if(i==j):
      print (i,)
    elif(p[i,j] == -30000):
      print (i,'-',j)
    else:
      ConstructPath(p, i, p[i,j]);
      print(j,)

import numpy as np

graph = np.array([[0,1],[2,1]])
print("graph:")
print(graph)

v = len(graph)

# path reconstruction matrix
p = np.zeros(graph.shape)
for i in range(0,v):
    for j in range(0,v):
        p[i,j] = i
        if (i != j and graph[i,j] == 0): 
            p[i,j] = -30000 
            graph[i,j] = 30000 # set zeros to any large number which is bigger then the longest way

for k in range(0,v):
    for i in range(0,v):
        for j in range(0,v):
            if graph[i,j] > graph[i,k] + graph[k,j]:
                graph[i,j] = graph[i,k] + graph[k,j]
                p[i,j] = p[k,j]

#show graph matrix
print("output:")
print(graph)
# show p matrix
print("p:")
print(p)

# reconstruct the path from 0 to 4
ConstructPath(p,0,1)
