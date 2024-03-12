class Figure_():
    def __init__(self):
        self.config = {
            "class": "normal",
            "prediction_quality": "correct",
            "plot_type":{}
        }
    
    def add_default_comparison(self):
        self.config["plot_type"]["comparison"] = {
                    "channels":{
                        "single_sample":{
                            "activated": False,
                            "scatter": False,
                            "line": False
                        },
                        "average_sample_over_class":{
                            "activated": False,
                            "scatter": False,
                            "line": False
                        },
                        "single_analyzer_score":{
                            "activated": False,
                            "scatter": False,
                            "line": False
                        },
                        "average_analyzer_score":{
                            "activated": False,
                            "scatter": False,
                            "line": False
                        }
                    }
                }
    
    def add_default_distribution(self):
        self.config["plot_type"]["distribution"] = {
                    "box_plot":{
                        "activated": False,
                        "num_of_bins": 0
                    },
                    "histogram":{
                        "activated": False,
                        "analyzer_relevance_scores":{
                            "activated": False,
                            "show_all_class": False
                        },
                        "input":{
                            "activated": False,
                            "show_all_class": False
                        }
                    }
                }