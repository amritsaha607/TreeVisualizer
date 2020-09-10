import numpy as np
import matplotlib.pyplot as plt

class Circle:
    '''
        Circle that conatins centre co-ordinates(x, y) & radius(s)
    '''

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s


def showNodes(circles, texts, mode='multi', debug=True):
    '''
        Shows multiple nodes
    '''
    if not mode=='multi':
        circles = [circles]
        texts = [texts]
    plt.scatter(
        [circle.x for circle in circles], 
        [circle.y for circle in circles], 
        s=[circle.s for circle in circles], 
        alpha=1,
        zorder=2,
    )
    for i, text in enumerate(texts):
        plt.text(
            circles[i].x, circles[i].y, 
            str(text), 
            horizontalalignment='center',
            verticalalignment='center',
        )
    if debug:
        plt.axis('off')
        plt.margins(0.1)
        plt.show()


def showCircle(circles, mode='multi', debug=True):
    '''
        Shows multiple circles
    '''
    if not mode=='multi':
        circles = [circles]
    plt.scatter(
        [circle.x for circle in circles], 
        [circle.y for circle in circles], 
        s=[circle.s for circle in circles], 
        alpha=0.5,
        zorder=2,
    )
    if debug:
        plt.show()


def showEdges(edges, mode='multi', debug=True):
    if not mode=='multi':
        edges = [edges]
    for edge in edges:
        plt.plot(
            [edge[0][0], edge[1][0]], [edge[0][1], edge[1][1]], 
            c='#6699ff', 
            zorder=1
        )


def makeCircles(data):
    '''
        Makes list circles from data points
    '''
    circles = []
    for [x, y, s] in data:
        circles.append(Circle(x, y, s))
    return circles


def getDepth(node):
    if not node:
        return 0
    return 1+max(getDepth(node.left), getDepth(node.right))

def showTree(node, edge=True, size=500, debug=True):
    d = getDepth(node)

    q = [[node, 0, 0, d-1]]
    circles, texts, edges = [], [], []

    while len(q):
        [cur, x, y, level] = q[0]
        del q[0]

        cur.circle = Circle(x, y, s=size)
        circles.append(cur.circle)
        texts.append(cur.val)
        
        if cur.left:
            q.append([cur.left, x-2**level, y-1, level-1])
            edges.append([(x, y), (x-2**level, y-1)])
        if cur.right:
            q.append([cur.right, x+2**level, y-1, level-1])
            edges.append([(x, y), (x+2**level, y-1)])

    showEdges(edges)
    showNodes(circles, texts, mode='multi')
