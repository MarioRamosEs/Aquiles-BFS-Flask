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
    initialNode = Node(8, 1, 1) # Hardcoded bc of demo
    queue = [initialNode]

    while len(queue) > 0:
        node = queue.pop()
        
        if(tempMaze[node.y-1][node.x] == 0):
            queue.insert(0, Node(node.y-1, node.x, node.level+1))
            tempMaze[node.y-1][node.x] = node.level

        if(tempMaze[node.y+1][node.x] == 0):
            queue.insert(0, Node(node.y+1, node.x, node.level+1))
            tempMaze[node.y+1][node.x] = node.level

        if(tempMaze[node.y][node.x-1] == 0):
            queue.insert(0, Node(node.y, node.x-1, node.level+1))
            tempMaze[node.y][node.x-1] = node.level

        if(tempMaze[node.y][node.x+1] == 0):
            queue.insert(0, Node(node.y, node.x+1, node.level+1))
            tempMaze[node.y][node.x+1] = node.level  

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