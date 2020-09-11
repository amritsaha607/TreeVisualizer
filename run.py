from helper import bakeTree
from utils import showTree
import argparse

def run(filename='cpp/dump.txt'):
    arr = [int(elem) for elem in open(filename, 'r').read().strip().split()]
    # print(f)

    root = bakeTree(arr)
    showTree(root)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", 
        type=str, 
        default="cpp/dump.txt", 
        help="File to read"
    )

    args = parser.parse_args()

    run(filename=args.f)