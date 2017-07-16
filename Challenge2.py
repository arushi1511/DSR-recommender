from __future__ import division
import networkx as nx
import re
import json

with open('data.json') as json_data:
    d = json.load(json_data)
with open('syllabus.json') as json_data:
    e = json.load(json_data)

k=[]
v=[]
for key,value in d.iteritems():
    k.append(key.encode('utf-8'))
    v.append(value)


#input the universal graph eg. A1-1, A2-2, A3-3
G=nx.Graph()
nodes = int(raw_input("Enter the no. of nodes in universal graph "))

node_name = []
node = []
for n in range(0,int(nodes)):
	nn = raw_input("Enter the node name ")  
	node_name.append(nn)
	st = nn.split('-',1)
	node.append(st[0])
print node
G.add_nodes_from(node)

edge_list = []
while True:
	t1 = raw_input("Edge from node ")
	edge_list.append(t1)
	t2 = raw_input("Edge to node ")
	edge_list.append(t2)
	e = (t1, t2)
	G.add_edge(*e)
	ip = raw_input("Enter another 'y' or 'n' ")	
	if ip == 'n':
		break
			
print "Number of nodes in graph is {0}".format(G.number_of_nodes())
print "Number of edges in graph is {0}".format(G.number_of_edges())
print "The edges in the graph are {0}".format(G.edges())

#user input subgraph as syllabus eg. A1, A2, A3
user_choice = k
'''
while True:
	temp = raw_input("User Choice Subgraph of syllabus ")
	user_choice.append(temp)
	flag = raw_input("press 'y' to continue and 'n' to exit ")
	if flag == 'n':
		break
'''		

print "Active nodes/ Syllabus {0}".format(user_choice)

status = [0] * len(node)

for c,i in enumerate(user_choice):
	idx = node.index(i)
	status[idx] = v[c]
print status

pre_config = raw_input("Enter predicate configuration setting (1 or 0)")

if pre_config == 0:
	while True:
		pass_fail = [0 for _  in range(len(node))]
		#print pass_fail
		idx = status.index(1)
		print "Course is {0}".format(node[idx])
		t = raw_input("..pass(1) or fail(0) for this course..")
		pass_fail[idx] = t
		counter = 1
		for i in range(idx+1, len(status), 1):
			if status[i] == 1:
				counter += 1
				print "Recommended course is {0}".format(node[i])
				t = raw_input("..pass(1) or fail(0) for this course..")
				pass_fail[i] = t
				per = pass_fail.count('1') / counter
				print per
				if per >= 0.7:
					print "Successful"
		per = pass_fail.count('1') /counter 
		if per == 1.0:
			print "Your Aced it"
		break
else:
	while True:
		pass_fail = [0 for _  in range(len(node))]
		#print pass_fail
		idx = status.index(1)
		print "Course is {0}".format(node[idx])
		t = raw_input("..pass(1) or fail(0) for this course..")
		if t == '0':
			i = edge_list.index(node[idx])
			if i % 2 != 0:
				print "Recommended course is {0}".format(edge_list[i-1])
				ii = node.index(edge_list[i-1])
				status[ii] = 1
			else:
				print "No recommended course available"
		pass_fail[idx] = t
		if t == '0':
			counter = 1
		else:
			counter = 0
		for i in range(idx+1, len(status), 1):
			if status[i] == 1:
				counter += 1
				print "Recommended course is {0}".format(node[i])
				t = raw_input("..pass(1) or fail(0) for this course..")
				pass_fail[i] = t
				per = pass_fail.count('1') / counter
				if per >= 0.7:
					print "Successful"
		per = pass_fail.count('1') /counter 
		if per == 1.0:
			print "Your Aced it"
		break	
