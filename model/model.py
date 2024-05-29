import networkx as nx
from database.DAO import DAO
class Model:
    def __init__(self):
        self.graph = nx.Graph()
        self.idMap = {}

    def buildGraph(self, year, country):
        self.graph.clear()
        nodi = DAO.get_retailers_dao(country)
        for n in nodi:
            self.idMap[n.code] = n
            self.graph.add_node(n)
        for n1 in self.graph.nodes:
            for n2 in self.graph.nodes:
                if n1.code != n2.code:
                    peso = DAO.get_peso_dao(n1.code, n2.code, year)
                    if peso[0]>0:
                        self.graph.add_edge(n1, n2, weight=peso[0])

    def volumi(self):
        result = []
        for n1 in self.graph.nodes:
            volume = 0
            for n2 in self.graph.neighbors(n1):
                volume += self.graph[n1][n2]["weight"]
            result.append((n1.name, volume))
        return sorted(result, key=lambda x: x[1], reverse=True)
    def get_country(self):
        return DAO.get_country_dao()