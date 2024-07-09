# g = graph
# v = visit
# visited = visited
def dfs(g,v,visited):
	visited[v] = True
	print(v,end =' ')
	for i in g[v]:
		if not visited[i]:
			dfs(g,i,visited)
g =[
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7],
]

visited = [False] * 9

dfs(g,1,visited)

# ===>
# 1 2 7 6 8 3 4 5