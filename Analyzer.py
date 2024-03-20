class Analyzer():
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.activation = None
        self.innvestigate_analyzer = None
        self.analyzer_output = None
        self.ui_elements_config = {
                    "upper_plot_count": 0,
                    "bottom_plot_count": 0,
                    "upper_tabs": {}, # QWidget() elements
                    "bottom_tabs": {},
                    "upper_figures": [], #own Figures_() objects
                    "bottom_figures": []
                }
        
    def increase_upper_plot_count(self):
        self.ui_elements_config["upper_plot_count"] += 1
    
    def increase_bottom_plot_count(self):
        self.ui_elements_config["bottom_plot_count"] += 1