#!/usr/bin/env python3

# ==============================
# Name: Random Boolean Network
# Author: Brendon Hutchins
# Date: 15/11/20
# Version: 1.0
# ==============================

# ==============================
# Comments: Will create two entities [Node](state, relation) and [TruthTable] (key value dict).
# n Nodes (20 in this case) will be created and assigned to collection [NodeObjectsContainer] as objects.
# each node will first be assigned a random boolean state. Each node will also be assigned 3 relations (nodes) (3 bits 000 <-> 111) randomly. (char set ^ length => 2^3 => total of 8 realities)
# we will print the resultant value at each time series. t, t+1, t+2 in column major. The first being the initial random states before any node \ relation calculations.
# 
# ==============================

#Imports
from random import randint
import random
from prettytable import PrettyTable
from argparse import ArgumentParser

#Globals
StateOptions = (True, False)
tableCurrentState = PrettyTable() # first table for init state
tableCurrentState.field_names = ["Node index", "State", "Relation"]

compositRelationValue = 0

tableT1State = PrettyTable() # second table for t+1
tableT1State.field_names = ["Node index", "State", "Relation"]

tableT2State = PrettyTable() # second table for t+2
tableT2State.field_names = ["Node index", "State", "Relation"]

# Program input parsing
parser = ArgumentParser(description='**** Generate network and dispaly ****')
parser.add_argument('-n', '--nodes', help='Number of nodes', default = 20, required=False)
parser.add_argument('-d', '--display', help='Set display method [terminal, LED matrix]', default= 'terminal',required=False)

args = parser.parse_args()
#TODO
if int(args.nodes)  > 1:
    # set node var HERE
    print("node larger then 1")
if args.display == 'terminal':
    # set display to TERMINAL HERE
    print("set to terminal")

if args.display == 'LED':
    print("LED has been selected")

class NodeInstance:
    def __init__(self, state):
        self.state = state
        self.relation = [randint(0,20), randint(0,20), randint(0,20)]

class TruthTable:
    def __init__ (self):
        TruthTable.booleanExpression = {'000': randint(0,1), '001': randint(0,1), '010': randint(0,1), '011': randint(0,1), '100': randint(0,1), '101': randint(0,1), '110': randint(0,1), '111': randint(0,1)}

    def printTruthTableInitState(self):
        return self.booleanExpression.items()

    def returnEntry(self, lookupValue):
        return self.booleanExpression.get(lookupValue, "Fault: Unable to locate value in list")
            
NodeObjectsContainer = []
tt = TruthTable()

for i in range (21):
    NodeObjectsContainer.append(NodeInstance(random.choice (StateOptions)))

# Getter
def getNewNodeIndex(value):
    return int(NodeObjectsContainer[value].state)

# Setter
def setNewNodeIndex():
    NodeObjectsContainer[indexLookup].state = False

# Extract t+1 state information
#for currentNode in NodeObjectsContainer:
# interate over each object: extract the relation tuple and assign to intermediate: lookup resultant value of the concatenated (3) key: append result of calculation to returnedValue list: return list.
def processing():
    returnedRelationalVlaue = [] # Resultant Values after relation calculation
    intermediateValueForProcessing = ''
    for obj in NodeObjectsContainer:
        # set obj relation 1, 2, 3
        compositRelationValue = obj.relation[0]
        intermediateValueForProcessing += (str(getNewNodeIndex(compositRelationValue)))

        compositRelationValue = obj.relation[1]
        intermediateValueForProcessing += (str(getNewNodeIndex(compositRelationValue)))

        compositRelationValue = obj.relation[2]
        intermediateValueForProcessing += (str(getNewNodeIndex(compositRelationValue)))

        # perform the intermediate calculation and assign to returnedRelationalValue array (in index order 0-19)
        #print(tt.returnEntry(intermediateValueForProcessing))
        obj.state = tt.returnEntry(intermediateValueForProcessing)
        returnedRelationalVlaue.append(intermediateValueForProcessing)
        intermediateValueForProcessing = ''
    return returnedRelationalVlaue

#Debug Info functions
#Print Current state 
def printCurrentState():
    print("Current State \n")
    csi = 0
    for obj in NodeObjectsContainer:
        tableCurrentState.add_row([csi, obj.state, obj.relation])
        csi += 1
    print(tableCurrentState)

def printT1TableState():
    print("T1 State \n")
    csi = 0
    for obj in NodeObjectsContainer:
        tableT1State.add_row([csi, obj.state, obj.relation])
        csi += 1
    print(tableT1State)

def printT2TableState():
    print("T2 State \n")
    csi = 0
    for obj in NodeObjectsContainer:
        tableT2State.add_row([csi, obj.state, obj.relation])
        csi += 1
    print(tableT2State)


printCurrentState()
processing()
printT1TableState()
processing()
printT2TableState()
print(tt.printTruthTableInitState())