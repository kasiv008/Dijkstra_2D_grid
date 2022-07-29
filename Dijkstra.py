import numpy as np
import sys
#np.set_printoptions(threshold=sys.maxsize)
import os
import matplotlib.pyplot as plt
from math import inf, sqrt, atan2
import math


class node():
    def __init__(self, value, is_start):
        self.value = value
        if is_start:
            self.dist = value
            self.backtrack = -1
        else:
            self.dist = np.inf
            self.backtrack = np.NaN

class Grid():
    def __init__(self, grid, start):
        self.grid = np.empty(grid.shape, dtype=node)
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if [i,j] == start:
                    self.grid[i,j] = node(grid[i,j], True)
                else:
                    self.grid[i,j] = node(grid[i,j], False)

class dijkstra():
    def __init__(self, grid, start, goal):
        self.grid = grid.grid
        self.start = start
        self.goal = goal
        self.unvisited = []
        self.visited = []
        self.found_path = 0
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                self.unvisited.append([i,j])

    def find_path(self):
        self.current_node = self.start
        while self.found_path == 0:
            neighbours = self.get_neighbours(self.current_node)
            for n in neighbours:
                tentative_dist = self.grid[self.current_node[0],self.current_node[1]].dist + self.grid[n[0],n[1]].value
                if tentative_dist < self.grid[n[0],n[1]].dist:
                    self.grid[n[0],n[1]].dist = tentative_dist
                    self.grid[n[0],n[1]].backtrack = self.current_node

            # print(self.current_node)
            self.visited.append(self.current_node)
            self.unvisited.remove(self.current_node)

            if self.current_node == self.goal:
                self.found_path = 1
                print("path found")
           
            self.current_node = self.get_next_node()

            if self.current_node == -1:
                self.found_path = -1
                print("path not found")


    def get_neighbours(self, node):
        neighbours = []
        max_x = self.grid.shape[0]-1
        max_y = self.grid.shape[1]-1
       
        if ([node[0]+1, node[1]+1] not in self.visited and 0 <= node[0]+1 <= max_x and 0 <= node[1]+1 <= max_y):
            neighbours.append([node[0]+1, node[1]+1])
            # self.grid[node[0]+1, node[1]+1].backtrack = [node[0], node[1]]
       
        if ([node[0]-1, node[1]-1] not in self.visited and 0 <= node[0]-1 <= max_x and 0 <= node[1]-1 <= max_y):
            neighbours.append([node[0]-1, node[1]-1])
            # self.grid[node[0]-1, node[1]-1].backtrack = [node[0], node[1]]
       
        if ([node[0]+1, node[1]-1] not in self.visited and 0 <= node[0]+1 <= max_x and 0 <= node[1]-1 <= max_y):
            neighbours.append([node[0]+1, node[1]-1])
            # self.grid[node[0]+1, node[1]-1].backtrack = [node[0], node[1]]
       
        if ([node[0]-1, node[1]+1] not in self.visited and 0 <= node[0]-1 <= max_x and 0 <= node[1]+1 <= max_y):
            neighbours.append([node[0]-1, node[1]+1])
            # self.grid[node[0]-1, node[1]+1].backtrack = [node[0], node[1]]

        if ([node[0]+1, node[1]] not in self.visited and 0 <= node[0]+1 <= max_x and 0 <= node[1] <= max_y):
            neighbours.append([node[0]+1, node[1]])
            # self.grid[node[0]+1, node[1]].backtrack = [node[0], node[1]]
       
        if ([node[0]-1, node[1]] not in self.visited and 0 <= node[0]-1 <= max_x and 0 <= node[1] <= max_y):
            neighbours.append([node[0]-1, node[1]])
            # self.grid[node[0]-1, node[1]].backtrack = [node[0], node[1]]
       
        if ([node[0], node[1]-1] not in self.visited and 0 <= node[0] <= max_x and 0 <= node[1]-1 <= max_y):
            neighbours.append([node[0], node[1]-1])
            # self.grid[node[0], node[1]-1].backtrack = [node[0], node[1]]
       
        if ([node[0], node[1]+1] not in self.visited and 0 <= node[0] <= max_x and 0 <= node[1]+1 <= max_y):
            neighbours.append([node[0], node[1]+1])
            # self.grid[node[0], node[1]+1].backtrack = [node[0], node[1]]

        return neighbours
