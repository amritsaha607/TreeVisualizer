from treeNode import TreeNode

def bakeTree(arr):
    '''
        Creates a tree and return root node of the tree
        arr should be a list of numbers containing tree node values
        -1 => NULL node
    '''
    q = []
    root = None

    while len(arr):
        val = arr[0]
        arr.pop(0)

        cur = None if val==-1 else TreeNode(val)
        if cur:
            q.append(cur)
        
        if not root:
            root = cur
        else:
            node = q[0]
            if not node.left:
                node.left = cur if cur else True
            else:
                node.right = cur
                q.pop(0)
                if node.left==True:
                    node.left = None
    
    return root

