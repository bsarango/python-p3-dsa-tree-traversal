class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_seen = [] #empty list to keep track of results
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      node  = nodes_to_visit.pop(0) #we get rid of the first node in the list of nodes_to_visit | assign the first value to the variable node

      if node['id'] == id:  #look to see if the value of the node's id is equal to the id argument - a string
        return node         # if so, we return the node itself

      else:                 #If not, we append the node to nodes_seen to know that we saw it already
        nodes_seen.append(node) 
        nodes_to_visit = node['children'] + nodes_to_visit  #we append the children of the current node to the nodes_to_visit list and repeats the while loop
      #Children are added to the front of the list to be seen next; we keep going lower in level by children of one branch until we move on to the next branch of nodes
    return None # if we don't return anything from the if in the while loop, we return None outside of the loop

    # while len(nodes_to_visit) > 0:
    #   node = nodes_to_visit.pop(0)

    #   if node['id'] == id:
    #     return node

    #   else:
    #     nodes_seen.append(node)
    #     nodes_to_visit = nodes_to_visit + node['children']  #for breadth-first method; will keep looking at the next nodes in the list. Children are added at the end

    # return None