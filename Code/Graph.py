#!/usr/bin/env python
# coding: utf-8

# In[2]:


from collections import defaultdict
dict_encoding = {"AffiliationID_Place_Affiliation":0,
                  "AuthID_AffiliationID":1, 
                  "AuthID_FieldID":2, 
                  "AuthID_Name":3,
                  "ConfID_FieldID":4,
                  "ConfID_PaperID":5,
                  "ConfID_Venue_Year":6,
                  "FieldID_Topic":7,
                  "KeywordID_PaperID":8,
                  "PaperID_AuthID":9,
                  "PaperID_FieldID":10,
                  "PaperID_Summary":11,
                  "PaperID_Title":12} 


# In[3]:


main_dict = defaultdict(list)
for i in dict_encoding:
    main_dict[dict_encoding[i]].append(i)#First Element is Table Name
    main_dict[dict_encoding[i]]+= i.split("_")#rest of the elements are columns
print(main_dict)


# In[4]:


from collections import defaultdict
import queue

class Graph:
	def __init__(self,vertices):
		self.graph = defaultdict(list)
		self.v = vertices
	def addedge(self,a,b):
		self.graph[a].append(b)
		self.graph[b].append(a)

	def printgraph(self):
		for k in self.graph:
			print(k, self.graph[k])
	def cleangraph(self):
		for k in self.graph:
			self.graph[k] = list(set(self.graph[k]))        
	def distance(self,u,v):
		visited = [0] * self.v

		# Initialize distances as 0  
		distance = [0] * self.v 

		# queue to do BFS.  
		Q = queue.Queue() 
		distance[u] = 0
		parent = [-1]*self.v
		parent[u] = u
		arra = [] 
		Q.put(u)  
		visited[u] = True
		while (not Q.empty()): 
			x = Q.get()

		      
			for i in range(len(self.graph[x])): 
				if (visited[self.graph[x][i]]): 
					continue

				parent[self.graph[x][i]] = x
				distance[self.graph[x][i]] = distance[x] + 1
				Q.put(self.graph[x][i])  
				visited[self.graph[x][i]] = 1
		p = v
		arra.append(v)
		while p!=u:
			arra.append(parent[p])
			p = parent[p]
			#print(p)
		#arra.append(u)
		return distance[v],arra[::-1] 


# In[5]:


def creategraph(maindict,graph):
    for i in maindict:
        for j in maindict:
            if (i!=j):
                if set(maindict[i]) & set(maindict[j]) :
                    graph.addedge(i,j)

                    
            


# In[6]:


def min_path_column(graph,start,end):
    start_array = []
    end_array = []
    minimum = 500
    path = []
    
    for key in main_dict.keys():
        if start in main_dict[key]:
            start_array.append(key)
        if end in main_dict[key]:
            end_array.append(key)
    for i in start_array:
        for j in end_array:
            if graph.distance(i,j)[0]<minimum:
                minimum = graph.distance(i,j)[0]
                path = graph.distance(i,j)[1]
    return path


# In[16]:


def make_join_query(path):
    print(path)
    string = "FROM "
    first_table = main_dict[path[0]][0]
    last_table = main_dict[path[-1]][0]
    
    if len(path)==1:
        string+= main_dict[path[0]][0]
    for i in range(len(path)-1):
        first = path[i]
        second = path[i+1]
        #extract common column
        common = None
        for c1 in main_dict[first]:
            for c2 in main_dict[second]:
                if c1==c2:
                    common = c1
        string += main_dict[first][0]
        string += " JOIN "
        string += main_dict[second][0]
        string += " ON "
        string += main_dict[first][0] + '.'+ common + "=" + main_dict[second][0]+ '.'+ common + ' '
    return string,first_table,last_table

def printpath(path):
    for i in (path):
        print(main_dict[i][0],end=" ")
def from_query(start,end):
    graph = Graph(len(main_dict))
    creategraph(main_dict,graph)
    graph.cleangraph()
    #graph.printgraph()
    path = min_path_column(graph,start,end)
    #print("Path is: ",end = "")
    #printpath(path)
    #print("")
    query,first_table,last_table = make_join_query(path)
    #print(query)
    return query,first_table,last_table
    


# In[8]:



#graph.distance(1,11)
#path = min_path_column(graph,"Title","Year")

#print("path",path)
#printpath(path)

#make_join_query(path)


# In[17]:


query,first_table,last_table = from_query("Title","Year")
print("Query = ", query," \n first_table = ",first_table, " \n last_table = ",last_table)

