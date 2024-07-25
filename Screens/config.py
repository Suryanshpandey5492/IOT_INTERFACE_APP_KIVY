def update_dashboard_screen(self):
    dashboard = self.manager.get_screen('dashboard') 
    if dashboard:
        dashboard.create_widgets()
        dashboard.update_data()

def update_graph_screen_interval(self):
    graph_screen = self.manager.get_screen('graph')  
    if graph_screen:
        graph_screen.refresh_update_interval()
        graph_screen.on_enter()

def update_graph_screen(self):
    graph = self.manager.get_screen('graph')  
    if graph:
        graph.update_selected_data_series()
        graph.on_enter()
