'''
            > LP -----15--->Guitar ----20---> Piano
          /     \             ^               ^   
        5          \        30              /
      /               \    /              /
Book                    \ /             10
      \                 / \            /
        0             /     20       / 
          \         /          v   / 
            > Poster --- 35-->Drums


'''
#create the weighted directgraph
trade = {}
trade["Book"]= {}
trade["Book"]["LP"] = 5 
trade["Book"]["Poster"] = 0
trade["LP"]= {}
trade["LP"]["Guitar"] = 15
trade["LP"]["Drums"] = 20
trade["Poster"]= {}
trade["Poster"]["Guitar"] = 30
trade["Poster"]["Drums"] = 35
trade["Guitar"]= {}
trade["Guitar"]["Piano"] = 20
trade["Drums"]= {}
trade["Drums"]["Piano"] = 10
trade["Piano"] = {}

#create the costs hashtable
costs = {}
infinity = float("inf")
costs["LP"] = 5
costs["Poster"] = 0
costs["Guitar"] = infinity
costs["Drums"] = infinity
costs["Piano"] = infinity

#print(costs)

#create the parent hashtable
parents = {}
parents["LP"] = "Book"
parents["Poster"] = "Book"
parents["Guitar"] = None
parents["Drums"] = None
parents["Piano"] = None

#only check the node that has not been visited
visited = []

#find the node with lowest values
def findLowestValueNode(costs):
    #set the initial lowest cost
    lowestCost = float("inf")
    #set the initial node with lowest value
    lowestCostNode = None
    for n in costs:
        cost = costs[n]
        #only check the node that has not been visited
        if cost < lowestCost and n not in visited:
            lowestCostNode = n
            lowestCost = cost
    return lowestCostNode

#main function
Node = findLowestValueNode(costs)
while Node is not None:
    cost = costs[Node]
    neighbors = trade[Node]
    for n in neighbors.keys():
        newCost = cost+neighbors[n]
        if newCost<costs[n]:
            costs[n] = newCost
            parents[n] = Node
    visited.append(Node)
    Node = findLowestValueNode(costs)

print(parents, costs["Piano"])
