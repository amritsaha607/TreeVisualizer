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


def showNodes(circles, texts, mode='multi'):
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
        alpha=0.5
    )
    for i, text in enumerate(texts):
        plt.text(
            circles[i].x, circles[i].y, 
            str(text), 
            horizontalalignment='center',
            verticalalignment='center',
        )
    plt.show()


def showCircle(circles, mode='multi'):
    '''
        Shows multiple circles
    '''
    if not mode=='multi':
        circles = [circles]
    plt.scatter(
        [circle.x for circle in circles], 
        [circle.y for circle in circles], 
        s=[circle.s for circle in circles], 
        alpha=0.5
    )
    plt.show()


def makeCircles(data):
    '''
        Makes list circles from data points
    '''
    circles = []
    for [x, y, s] in data:
        circles.append(Circle(x, y, s))
    return circles


def showTree(node, size=100):
    q = [[node, 0, 0]]
    circles, texts = [], []

    while len(q):
        [cur, x, y] = q[0]
        del q[0]

        cur.circle = Circle(x, y, s=size)
        circles.append(cur.circle)
        texts.append(cur.val)
        
        if cur.left:
            q.append([cur.left, x-1, y-1])
        if cur.right:
            q.append([cur.right, x+1, y-1])

    showNodes(circles, texts, mode='multi')
