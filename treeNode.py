import numpy as np
import matplotlib.pyplot as plt

class TreeNode(object):

    def __init__(self, val):
        super(TreeNode, self).__init__()
        
        self.val = val
        self.left = None
        self.right = None

        self.circle = None

