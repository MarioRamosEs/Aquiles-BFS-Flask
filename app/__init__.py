from flask import Flask
from flask import render_template
from copy import deepcopy
app = Flask(__name__)

class Node:
    def __init__(self, y, x, level):
        self.y = y
        self.x = x
        self.level = level

maze = [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1],
    [-1, 0, -1, 0, -1, 0, -1, -1, 0, -1],
    [-1, -1, -1, 0, -1, -1, -1, 0, 0, -1],
    [-1, 0, 0, 0, 0, 0, 0, 0, -1, -1],
    [-1, 0, -1, -1, 0, -1, -1, 0, 0, -1],
    [-1, 0, 0, 0, 0, -1, -1, -1, 0, -1],
    [-1, -1, 0, -1, 0, -1, 0, 0, 0, -1],
    [-1, -2, 0, -1, 0, 0, 0, -1, 0, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
]

def solveMaze(maze):
    tempMaze = deepcopy(maze)
    initialVector = Node(8, 1, 1)
    whiteList = [initialVector]

    while len(whiteList) > 0:
        vector = whiteList.pop()
        
        if(tempMaze[vector.y-1][vector.x] == 0):
            whiteList.insert(0, Node(vector.y-1, vector.x, vector.level+1))
            tempMaze[vector.y-1][vector.x] = vector.level

        if(tempMaze[vector.y+1][vector.x] == 0):
            whiteList.insert(0, Node(vector.y+1, vector.x, vector.level+1))
            tempMaze[vector.y+1][vector.x] = vector.level

        if(tempMaze[vector.y][vector.x-1] == 0):
            whiteList.insert(0, Node(vector.y, vector.x-1, vector.level+1))
            tempMaze[vector.y][vector.x-1] = vector.level

        if(tempMaze[vector.y][vector.x+1] == 0):
            whiteList.insert(0, Node(vector.y, vector.x+1, vector.level+1))
            tempMaze[vector.y][vector.x+1] = vector.level  

        vector.level = vector.level + 1

    return tempMaze

@app.route('/')
@app.route('/index')
@app.route('/maze')
def index():
    return render_template('index.html', title='Maze', maze=maze)

@app.route('/maze/solved')
def mazeSolved():
    solvedMaze = solveMaze(maze)
    return render_template('index.html', title='Maze Solved', maze=solvedMaze)