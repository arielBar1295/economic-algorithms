from typing import List
import networkx as nx

#quuestion number 3
#made by Ariel Bar and Dana Morhaim

"""
The example module checks the change shifting function
The example is from: https://www.hamichlol.org.il/%D7%9E%D7%A2%D7%92%D7%9C%D7%99_%D7%A1%D7%97%D7%A8_%D7%A2%D7%9C%D7%99%D7%95%D7%A0%D7%99%D7%9D

>>> a=Worker('a',[3,2,4,1],1)
>>> b= Worker('b', [3,5,6], 2)
>>> c= Worker('c', [3,1], 3)
>>> d= Worker('d', [2,5,6,4], 4)
>>> e= Worker('e', [1,3,2], 5)
>>> f= Worker('f', [2,4,5,6], 6)

>>> workers = [a,b,c,d,e,f]
>>> exchange_shifts(workers)

c moves from shift 3 to Shift 3
a moves from shift 1 to Shift 2
b moves from shift 2 to Shift 5
e moves from shift 5 to Shift 1
d moves from shift 4 to Shift 6
f moves from shift 6 to Shift 4
"""

class Worker:
    name: str
    preferences: list
    current_shift: int

    def __init__(self, name, preferences,current_shift):
        self.name = name
        self.preferences = preferences
        self.current_shift = current_shift

#this method builds the graph for the first time
def build_graph(workers):
    G = nx.DiGraph()
    for worker in workers:
        G.add_edge(worker.name, worker.preferences[0])
        G.add_edge(worker.current_shift, worker.name)
    return G



def exchange_shifts (workers: List[Worker]):

    while workers:
        G = nx.DiGraph()
        G = build_graph(workers)
        # find the cycle in the graph
        changes = list(nx.find_cycle(G, orientation='ignore'))
        # [(3, 'c', 'forward')]
        for change in changes:

            if(type(change[0]) == str):
                currentShift = find_shift(workers, change[0])
                print(str(change[0]) + " moves from shift " +str(currentShift) +" to Shift " + str(change[1]))
                #remove worker
                workers=update_workers(workers, change[0])
                #remove this shift from al preferances
                update_preferances(workers, change[1])
                # remove the nodes that were found in the cycle




#this function returns the current shift of the worker
def find_shift(workers: List[Worker], workerName):
    for worker in workers:
        if worker.name==workerName:
            return worker.current_shift

#remove the taken shifts
def update_preferances(workers: List[Worker], shiftNum):
    for worker in workers:
        for pref in worker.preferences:
            if pref==shiftNum:
                worker.preferences.remove(pref)
#remove worker from workers list
def update_workers(workers: List[Worker], workerName):
    for worker in workers:
        if worker.name==workerName:
            workers.remove(worker)
    return  workers

if __name__ == "__main__":
    import doctest
    doctest.testmod()
