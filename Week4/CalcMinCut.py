# Implementaiton of the MinCut problem from the Course: Design and Analysis of Algorithms on Coursera

# Choose an edge at random: First choose the node1 at random and then any other node in the adjacency list of node1

import random
from random import randrange

minCut = []

# Running it for around 100 iterations to get the best result
for num in range(100):
	#Read the file for the adjacency list
	dataFile = open('kargerMinCut.txt','r')
	
	data = []
	
	for line in dataFile:
		number_Strings = line.split()
		numbers = [int(n) for n in number_Strings]
		data.append(numbers)

	# Perform edge contraction till there are just two nodes left
	while (len(data) > 2):
		
		#print(data)
		lenData = len(data)
		#print(lenData)
	
		#Choose the nodes index at random, to eventually choose an edge at random	
		indexNode1 = random.randint(0,lenData-1)
		node1 = data[indexNode1]
		#print('Random node1 index is:',indexNode1)
		#print('Random node1 is:',data[indexNode1])
		
		lenAdjList = len(data[indexNode1])
		#print(lenAdjList)
		
		indexNode2 = random.randint(1,lenAdjList-1)
		node2 = data[indexNode1][indexNode2]
		#print('Random node2 index is:',indexNode2)
		#print('Random node2 is:',data[indexNode1][indexNode2])
	
		# Once the random edge is chosen, we need to connect the fused node with the edges connected to one of the nodes in the group	
		indexEdge = 0
		for i in range(lenData):
			if (data[i][0] == node2):
				indexEdge = i
				lenList = len(data[i])
				for j in range(1,lenList):
					if(data[indexNode1][0] != data[i][j]):
						data[indexNode1].append(data[i][j])
		
		#print(data)
	
		# After edges have been contracted, we need to replace all the instances of , node2 (in our case), from the adjacency list and replace it with the fused node. The two lists below will hold the value of indexes where node2 is present	
		indexDelNodeX = []
		indexDelNodeY = []
		for k in range(len(data)):
			#print('Entering list:',data[k])
			for l in range(len(data[k])):
				#print('Checking the element', data[k][l])
				if (data[k][l] == node2):
					if(data[k][0] == data[indexNode1][0]):
						indexDelNodeX.append(k)
						indexDelNodeY.append(l)
					else:
						#print('Replacing with',data[indexNode1][0])
						data[k][l] = data[indexNode1][0]
						#print('After replacing:',data[k])
		
		#print('indexDelNodeX is:', indexDelNodeX)
		#print('indexDelNodeY is:', indexDelNodeY)
		# from the adjacency list of node1, delete all node2 instances
		for i in range (len(indexDelNodeY)):
			del data[indexDelNodeX[i]][indexDelNodeY[i]-i]
		# delete the node2 adjacency list
		del data[indexEdge]					
		#print(data)
	
	#print('final list is:', data)
	
		minCut.append(len(data[0])-1)
print(min(minCut))
