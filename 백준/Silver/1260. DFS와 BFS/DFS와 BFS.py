# 정점의 갯수 ,간선의 갯수, 시작 번호
N, M, V = map(int,input().split())

# 그래프 - 인접리스트 방식
graph = [[] for _ in range(N+1)]   # 정점의 갯수 +1 초기화
for _ in range(M): # 그래프에 간선 정보 채워넣기
    start , end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)  # 양방향 연결

for node in graph:
    node.sort() # 빠른 번호부터 탐색하기 위해 정렬 수행

visited = [False] * (N+1) # 방문 처리를 위한 리스트

# DFS
def DFS(graph,node,visited):
    # 방문처리
    visited[node] = True
    # 현재 노드 출력
    print(node, end= ' ')
    
    # 현재 노드에서 방문 할 수 있는 candidate탐색
    for candidate in graph[node]:
        if not visited[candidate]:
            DFS(graph,candidate,visited)
    
DFS(graph,V,visited)

# BFS
visited = [False] * (N+1) #방문처리 초기화

from collections import deque

def BFS(graph,node,visited):
    visited[node] = True
    
    queue = deque([node])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
            
    
print()
BFS(graph,V,visited) 