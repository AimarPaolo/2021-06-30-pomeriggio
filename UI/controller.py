import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        for f in self._model._grafo.nodes:
            self._view.ddlocalizzazione.options.append(ft.dropdown.Option(text=f))

    def crea_grafo(self):
        self._view.txt_result.controls.clear()
        self._model.buildGraph()
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato!"))
        nNodes, nEdges = self._model.getCaratteristiche()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo creato ha {nNodes} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo creato ha {nEdges} archi"))
        self.fillDD()
        self._view.update_page()

    def handle_statistiche(self, e):
        self._view.txt_result.controls.clear()
        loc = self._view.ddlocalizzazione.value
        if loc is None:
            self._view.create_alert("Selezionare una localizzazione!")
            self._view.update_page()
            return
        self._view.txt_result.controls.append(ft.Text(f"Adiacenti a: {loc}"))
        for nodi_raggiungibili, peso in self._model.getConnectedComponents(loc):
            self._view.txt_result.controls.append(ft.Text(f"{nodi_raggiungibili}        {peso}"))
        self._view.update_page()

    def handle_path(self, e):
        self._view.txt_result.controls.clear()
        loc = self._view.ddlocalizzazione.value
        if loc is None:
            self._view.create_alert("Selezionare una localizzazione!")
            self._view.update_page()
            return
        peso, path = self._model.getBestPath(loc)
        self._view.txt_result.controls.append(ft.Text(f"Esiste un cammino di peso totale: {peso}"))
        for p in range(len(path)-1):
            self._view.txt_result.controls.append(ft.Text(f"{path[p]} --> {path[p+1]} {self._model._grafo[path[p]][path[p+1]]['weight']}"))
        self._view.update_page()