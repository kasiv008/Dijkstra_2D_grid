from dijkstra import * 

start = [18, 0]
grid = Grid(cmap, start)
dij = dijkstra(grid, start, goal)
dij.find_path()
path = dij.back_track()[::-1]
