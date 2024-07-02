import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self.nodi = []
        self.idMap = {}
        self._costBest = 0
        self._solBest = []

    def buildGraph(self):
        self._grafo.clear()
        self.nodi = DAO.nome1()
        self._grafo.add_nodes_from(self.nodi)
        self.addEdges()

    def addEdges(self):
        self._grafo.clear_edges()
        for loc1, loc2, peso in DAO.nome2():
            if loc2 != loc1:
                if peso > 0:
                    if self._grafo.has_edge(loc1, loc2) is False:
                        self._grafo.add_edge(loc1, loc2, weight=peso)

    def getConnectedComponents(self, loc):
        raggiungibili = []
        for nodi in self._grafo.neighbors(loc):
            raggiungibili.append((nodi, self._grafo[nodi][loc]['weight']))
        return raggiungibili

    def getBestPath(self, loc):
        self._costBest = 0
        self._solBest = []
        parziale = [loc]
        self.ricorsione(parziale)
        return self._costBest, self._solBest


    def ricorsione(self, parziale):
        if self.peso(parziale) > self._costBest:
            self._costBest = self.peso(parziale)
            self._solBest = copy.deepcopy(parziale)

        for v in self._grafo.neighbors(parziale[-1]):
            if v not in parziale:
                parziale.append(v)
                self.ricorsione(parziale)
                parziale.pop()

    def peso(self, parziale):
        peso = 0
        for p in range(len(parziale)-1):
            peso += self._grafo[parziale[p]][parziale[p+1]]["weight"]
        return peso

    def getCaratteristiche(self):
        return len(self._grafo.nodes), len(self._grafo.edges)