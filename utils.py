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


def showNodes(nodes, focus=[], mode='multi', debug=True):
    '''
        Shows multiple nodes
    '''
    if not mode=='multi':
        nodes = [nodes]
    nodes_ = list(set(nodes)-set(focus))
    plt.scatter(
        [node.circle.x for node in nodes_], 
        [node.circle.y for node in nodes_], 
        s=[node.circle.s for node in nodes_], 
        alpha=1,
        zorder=2,
    )
    plt.scatter(
        [node.circle.x for node in focus], 
        [node.circle.y for node in focus], 
        s=[node.circle.s for node in focus], 
        c='r',
        alpha=1,
        zorder=2,
    )
    for i, node in enumerate(nodes):
        plt.text(
            node.circle.x, node.circle.y, 
            str(node.val), 
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

def showTree(node, edge=True, focusNodes=[], size=500, debug=True):
    d = getDepth(node)

    q = [[node, 0, 0, d-1]]
    nodes, edges = [], []

    while len(q):
        [cur, x, y, level] = q[0]
        del q[0]

        cur.circle = Circle(x, y, s=size)
        nodes.append(cur)
        
        if cur.left:
            q.append([cur.left, x-2**level, y-1, level-1])
            edges.append([(x, y), (x-2**level, y-1)])
        if cur.right:
            q.append([cur.right, x+2**level, y-1, level-1])
            edges.append([(x, y), (x+2**level, y-1)])

    showEdges(edges)
    showNodes(nodes, focus=focusNodes, mode='multi')
