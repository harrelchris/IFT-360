# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 22:50:58 2022

@author: aelbadra
"""
from tree import Tree, TreeNode
from graph import Graph

class GraphTraverser:
    
    def __init__(self, g):
        self.graph = g
        self.tree = Tree()
        
    #creates a tree to traverse the graph breadth-first starting at start_node_name
    def breadth_first_traversal(self, start_node_name, target_node_name):
        #check if start node is part of the graph
        if start_node_name not in self.graph.nodes:
            print(start_node_name, "not found in graph!")
            return
        #check if start node is the target node
        if start_node_name == target_node_name:
            print("Start node is the target node! No search needed.")
            return
        
        #setup data structures to keep track of reached nodes and 
        #nodes that ae yet to be expanded per breadth-first
        reached_nodes = {}
        reached_nodes[start_node_name] = 1
        nodes_to_expand = [start_node_name]
        
        
        #construct the traversal tree, starting at the root.
        self.tree = Tree()
        rootNode = TreeNode(start_node_name, None)
        self.tree.set_root(rootNode)

        while len(nodes_to_expand) > 0:
            #expand the node at the beginning of the espansion list
            node_name = nodes_to_expand.pop(0)
            children = self.graph.expand_node(node_name)
            
            for child in children: #for each new child
                child_name = child[0]
                child_edgewt = child[1]
                #if child is target, return solution!
                if child_name == target_node_name:
                    n = TreeNode(child_name,node_name)
                    self.tree.add_child_node( n , node_name, child_edgewt)
                    print('Target Reached!')
                    self.tree.print_path(n)
                    return
                #if child is a newly reached node, add to expansion list, tree
                if child_name not in reached_nodes:
                    reached_nodes[child_name] = 1
                    nodes_to_expand.append(child_name)
                    n = TreeNode(child_name,node_name)
                    self.tree.add_child_node( n, node_name, child_edgewt)
                    
        #if all nodes were expanded and solution not found:
        print('Target not found!')
        return

    def depth_first_traversal(self, start_node_name, target_node_name):
        # check if start node is part of the graph
        if start_node_name not in self.graph.nodes:
            print(start_node_name, "not found in graph!")
            return
        # check if start node is the target node
        if start_node_name == target_node_name:
            print("Start node is the target node! No search needed.")
            return

        # setup data structures to keep track of reached nodes and
        # nodes that ae yet to be expanded per breadth-first
        reached_nodes = {}
        reached_nodes[start_node_name] = 1
        nodes_to_expand = [start_node_name]

        # construct the traversal tree, starting at the root.
        self.tree = Tree()
        rootNode = TreeNode(start_node_name, None)
        self.tree.set_root(rootNode)

        while len(nodes_to_expand) > 0:
            # expand the node at the end of the expansion list
            node_name = nodes_to_expand.pop()
            children = self.graph.expand_node(node_name)

            for child in children:  # for each new child
                child_name = child[0]
                child_edgewt = child[1]
                # if child is target, return solution!
                if child_name == target_node_name:
                    n = TreeNode(child_name, node_name)
                    self.tree.add_child_node(n, node_name, child_edgewt)
                    print('Target Reached!')
                    self.tree.print_path(n)
                    return
                # if child is a newly reached node, add to expansion list, tree
                if child_name not in reached_nodes:
                    reached_nodes[child_name] = 1
                    nodes_to_expand.append(child_name)
                    n = TreeNode(child_name, node_name)
                    self.tree.add_child_node(n, node_name, child_edgewt)

        # if all nodes were expanded and solution not found:
        print('Target not found!')
        return
#==================================================================
#==================================================================
#==================================================================
