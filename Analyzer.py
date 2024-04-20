class Analyzer():
    """
    Wrapper class for the iNNvestigate.analyzer, completed with a dictionary storing information for UI elements.
    """
    def __init__(self, neuron = None):
        self.activation = None
        self.innvestigate_analyzer = None
        self.analyzer_output = None
        self.neuron = neuron
        self.ui_elements_config = {
                    "upper_plot_count": 0,
                    "bottom_plot_count": 0,
                    "upper_tabs": {}, # QWidget() elements
                    "bottom_tabs": {},
                    "upper_figures": [], #own Figures_() objects
                    "bottom_figures": [],
                    "upper_checkboxes": [],
                    "bottom_checkboxes": []
                }
        
    def increase_upper_plot_count(self):
        self.ui_elements_config["upper_plot_count"] += 1
    
    def increase_bottom_plot_count(self):
        self.ui_elements_config["bottom_plot_count"] += 1

class IG_Analyzer(Analyzer):
    def __init__(self, reference_input, steps):
        super().__init__()
        self.reference_input = reference_input
        self.steps = steps

class LRP_AB_Analyzer(Analyzer):
    def __init__(self, alpha, beta):
        super().__init__()
        self.alpha = alpha
        self.beta = beta

class LRP_E_Analyzer(Analyzer):
    def __init__(self, epsilon):
        super().__init__()
        self.epsilon = epsilon

class LRP_Z_Analyzer(Analyzer):
    def __init__(self):
        super().__init__()