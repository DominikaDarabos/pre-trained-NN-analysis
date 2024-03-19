class Project():
    def __init__(self):
        #TODO: until testing
        self.model_file_path = "C:/Users/dominika/vpnet/trained_models/ecg_train_test_full_model.h5"
        self.custom_object_file_path = "C:/Users/dominika/vpnet/tensorflow/VPLayer.py"
        self.input_file_path = "C:/Users/dominika/vpnet/tensorflow/ecg_test_data.h5"
        self.model = None
        self.model_wo_softmax = None
        self.test_x = None
        self.test_y = None
        self.number_of_classes = None
        self.config = {
            "analyzers": {
                "IG": {
                    "checked": False,
                    "activation": None,
                    "analyzer": None,
                    "upper_plot_count": 0,
                    "bottom_plot_count": 0,
                    "upper_tabs": {},
                    "bottom_tabs": {},
                    "upper_figures": [],
                    "bottom_figures": []
                },
                "LRP_Z": {
                    "checked": False,
                    "activation": None,
                    "analyzer": None,
                    "upper_plot_count": 0,
                    "bottom_plot_count": 0,
                    "upper_tabs": {},
                    "bottom_tabs": {},
                    "upper_figures": [],
                    "bottom_figures": []
                },
                "LRP_AB": {
                    "checked": False,
                    "activation": None,
                    "alpa": False,
                    "beta": None,
                    "analyzer": None,
                    "upper_plot_count": 0,
                    "bottom_plot_count": 0,
                    "upper_tabs": {},
                    "bottom_tabs": {},
                    "upper_figures": [],
                    "bottom_figures": []
                },
                "LRP_Epsilon": {
                    "checked": False,
                    "activation": None,
                    "epsilon": None,
                    "analyzer": None,
                    "upper_plot_count": 0,
                    "bottom_plot_count": 0,
                    "upper_tabs": {},
                    "bottom_tabs": {},
                    "upper_figures": [],
                    "bottom_figures": []
                }
            }
        }

    def set_model_file(self, path):
        self.model_file_path = path

    def set_input_file(self, path):
        self.input_file_path = path

    def set_custom_file(self, path):
        self.custom_object_file_path = path
    
    def increase_upper_plot_count(self, analyzer):
        self.config["analyzers"][analyzer]["upper_plot_count"] += 1
    
    def increase_bottom_plot_count(self, analyzer):
        self.config["analyzers"][analyzer]["bottom_plot_count"] += 1