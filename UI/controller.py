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
        for i in range(2015,2019):
            self._view.ddyear.options.append(ft.dropdown.Option(key=i, text=str(i)))
        self._view.update_page()
        country = sorted(self._model.get_country())
        for c in country:
            self._view.ddcountry.options.append(ft.dropdown.Option(c))



    def handle_graph(self, e):
        if self._view.ddyear.value is None or self._view.ddcountry.value is None or self._view.ddyear.value=="" or self._view.ddcountry.value=="":
            self._view.create_alert("Selezionare tutti i campi!")
        else:
            self._view.txt_result.clean()
            self._model.buildGraph(int(self._view.ddyear.value), self._view.ddcountry.value)
            self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.graph.number_of_nodes()} nodi e {self._model.graph.number_of_edges()} archi."))
            self._view.update_page()



    def handle_volume(self, e):
        if self._model.graph.number_of_nodes() == 0 and self._model.graph.number_of_edges() == 0:
            self._view.create_alert("Creare prima il grafo!")
        else:
            self._view.txtOut2.clean()
            volumi = self._model.volumi()
            for v in volumi:
                self._view.txtOut2.controls.append(ft.Text(f"{v[0]} --> {v[1]}"))
            self._view.update_page()
    def handle_path(self, e):
        pass
