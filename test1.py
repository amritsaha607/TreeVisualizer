import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import networkx.generators.small as gs
import numpy as np

def makeGraph():

	fig = plt.figure()

	G = nx.DiGraph()
	G.add_node("Root")

	# write dot file to use with graphviz
	# run "dot -Tpng test.dot >test.png"
	# nx.nx_agraph.write_dot(G,'test.dot')

	# same layout using matplotlib with no labels
	plt.title('draw_networkx')
	pos=graphviz_layout(G, prog='dot')
	nx.draw(G, pos, with_labels=False, arrows=False)
	plt.savefig('nx_test.png')

	nx.draw(G, with_labels=True)

	plt.show()
	plt.savefig('tmp.png')

makeGraph()
