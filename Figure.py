import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
import random

class Figure_():
    def __init__(self):
        self.config = {
            "class": None,
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
                        "sample_frequency": 0
                    },
                    "histogram":{
                        "activated": False,
                        "num_of_bins": 0,
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

    def is_comparison(self):
        return ("comparison" in self.config["plot_type"])

    def is_hist_distribution(self):
        return ("distribution" in self.config["plot_type"] and self.config["plot_type"]["distribution"]["histogram"]["activated"])


    def normalize(self, data, min_val, max_val):
        return (data - np.min(data)) / (np.max(data) - np.min(data)) * (max_val - min_val) + min_val


    def plot_relevance_score_distribution(self, project, analyzer, figureSize, classes = None):
        """
        Avarage relevance scores over class

        Creates a histogram for the analyzer given as parameter.
        The plot visualize all the classes' analyzer outcomes' distribution
        Classes seperated by the gorund truth labels
        """
        analyzer_ = False
        input_ = False
        if self.config["plot_type"]["distribution"]["histogram"]["analyzer_relevance_scores"]["activated"]:
            analyzer_ = True
            if self.config["plot_type"]["distribution"]["histogram"]["analyzer_relevance_scores"]["show_all_class"] and classes == None:
                possible_classes = range(project.number_of_classes)
            elif classes != None:
                possible_classes = classes
            else:
                possible_classes = [int(self.config["class"])]
        elif self.config["plot_type"]["distribution"]["histogram"]["input"]["activated"]:
            input_ = True
            if self.config["plot_type"]["distribution"]["histogram"]["input"]["show_all_class"] and classes == None:
                possible_classes = range(project.number_of_classes)
            elif classes != None:
                possible_classes = classes
            else:
                possible_classes = [int(self.config["class"])]

        fig = plt.figure(figsize=((figureSize.width() - 10)/100, (figureSize.height() - 10)/100))
        ax = fig.add_subplot(111)
        colors=['red', 'dimgray', 'lightgray']
        alpha_val = 0.5
        
    # Create the histogram plot
        for class_num in possible_classes:
            if self.config["prediction_quality"] == "ground_truth":
                class_indices = project.get_truth_class_indices(class_num)
            elif self.config["prediction_quality"] == "correct":
                #TODO: will be the same for all class
                class_indices = project.get_correct_pred_indices_for_class(class_num)
            elif self.config["prediction_quality"] == "incorrect":
                class_indices = project.get_incorrect_prediction_indices_for_class(class_num)
            elif self.config["prediction_quality"] == "false_negative":
                class_indices = project.get_false_negative_indices(class_num)
            elif self.config["prediction_quality"] == "false_positive":
                class_indices = project.get_false_positive_indices(class_num)
            else:
                class_indices = []

            class_values = project.test_x[class_indices]
            analyzer_class = project.analyzers[analyzer].analyzer_output[class_indices]
            if class_values.shape[0] == 0:
                continue
            bin_num = self.config["plot_type"]["distribution"]["histogram"]["num_of_bins"]
            if analyzer_:
                ax.hist(analyzer_class.flatten(), bins=bin_num, color=colors[class_num], alpha = alpha_val, label=f"Class_{class_num+1}")
            elif input_:
                ax.hist(class_values.flatten(), bins=bin_num, color=colors[class_num], alpha = alpha_val, label=f"Class_{class_num+1}")
        #◙ax.set_title(analyzer, fontsize = 16)
        #◙ax.title.set_size(10)
        ax.set_yscale("log")
        ax.legend()
        #ax.set_ylabel('count')
        ax.set_xlabel('Relevance scores',fontsize = 'medium')
        fig.tight_layout()
        #plt.savefig(f"{Path.cwd()}\..\plots\latest\ecg\hist_plot_distribution\dist_ecg_{title}.png")
        #plt.show()
        return fig
    
    def plot_grouped_boxplot(self, project, analyzer, figureSize):
        class_num = int(self.config["class"])
        sample_freq = int(self.config["plot_type"]["distribution"]["box_plot"]["sample_frequency"])
        class_probabilities = project.predictions[:, class_num]
        sorted_indices = np.argsort(class_probabilities)
        
        fig = plt.figure(figsize=((figureSize.width() - 10)/100, (figureSize.height() - 10)/100))
        ax = fig.add_subplot(111)
        correct_pos_indices = project.get_correct_pos_prediction_indices_for_class(class_num)
        correct_neg_indices = project.get_correct_neg_prediction_indices_for_class(class_num)
        false_neg_indices_for_class = project.get_false_negative_indices(class_num)
        false_pos_indices_for_class = project.get_false_positive_indices(class_num)

        sorted_false_neg_indices = np.where(np.isin(sorted_indices, false_neg_indices_for_class))[0]
        sorted_false_pos_indices = np.where(np.isin(sorted_indices, false_pos_indices_for_class))[0]
        sorted_correct_neg_indices = np.where(np.isin(sorted_indices, correct_neg_indices))[0]
        sorted_correct_pos_indices = np.where(np.isin(sorted_indices, correct_pos_indices))[0]

        output = project.analyzers[analyzer].analyzer_output[sorted_indices].T
        #plt.boxplot(output[:,sorted_correct_indices], positions=sorted_correct_indices, flierprops = dict(marker='.', markersize=3, linestyle='none', markeredgecolor='dimgray'), patch_artist=True, boxprops = dict(facecolor = "dimgray"))
        ax.boxplot(output[:,sorted_correct_pos_indices[::sample_freq]], positions=sorted_correct_pos_indices[::sample_freq], flierprops = dict(marker='.', markersize=3, linestyle='none', markeredgecolor='indianred'), patch_artist=True, boxprops = dict(facecolor = "indianred"))
        ax.boxplot(output[:,sorted_correct_neg_indices[::sample_freq]], positions=sorted_correct_neg_indices[::sample_freq], flierprops = dict(marker='.', markersize=3, linestyle='none', markeredgecolor='powderblue'), patch_artist=True, boxprops = dict(facecolor = "powderblue"))
        ax.boxplot(output[:,sorted_false_neg_indices[::sample_freq]], positions=sorted_false_neg_indices[::sample_freq], flierprops = dict(marker='.', markersize=3, linestyle='none', markeredgecolor='darkcyan'), patch_artist=True, boxprops = dict(facecolor = "darkcyan"))
        ax.boxplot(output[:,sorted_false_pos_indices[::sample_freq]], positions=sorted_false_pos_indices[::sample_freq], flierprops = dict(marker='.', markersize=3, linestyle='none', markeredgecolor='darkred'), patch_artist=True, boxprops = dict(facecolor = "darkred"))

        legend_patches = [Patch(facecolor='powderblue', edgecolor='powderblue', label='True negative'),
                            Patch(facecolor='darkcyan', edgecolor='darkcyan', label='False negative'),
                            Patch(facecolor='indianred', edgecolor='indianred', label='True positive'),
                            Patch(facecolor='darkred', edgecolor='darkred', label='False positive')]

        ax.legend(handles=legend_patches, loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=len(legend_patches))

        classes = ["normal", "abnormal"]
        #ax.set_title(f"{analyzer} vs. probability of {classes[class_num]} signal according to the model")
        ax.set_xlabel(f"Probability of {classes[class_num]} signal")
        ax.set_ylabel("Relevance Scores")
        min_, max_ = np.percentile(project.analyzers[analyzer].analyzer_output.T, [0.1,99.9])
        ax.set_ylim(min_,max_)

        array = class_probabilities[sorted_indices]
        tick_positions = np.arange(0,1,0.1)
        ticks = np.arange(0,100,10)
        nearest_indices = (np.abs(array[:, None] - tick_positions)).argmin(axis=0)
        ax.set_xticks(nearest_indices, ticks)
        fig.tight_layout()
        ax.grid(True, which='major', axis='x')
        #plt.savefig(f"{Path.cwd()}\..\plots\latest\ecg\\box_plot_distribution\{title}_class_{classes[class_num]}.png")
        return fig


    def plot_comparison(self, project, analyzer, figureSize):
        class_num = int(self.config["class"])
        if self.config["prediction_quality"] == "correct":
            indices_for_class = project.get_correct_pos_prediction_indices_for_class(class_num)
            input_for_class = project.test_x[indices_for_class]
            analyzer_for_class = project.analyzers[analyzer].analyzer_output[indices_for_class]
            analyzer_class_mean = np.mean(analyzer_for_class, axis=0, keepdims=True)
            input_class_mean = np.mean(input_for_class, axis=0, keepdims=True)
            title = f"Correctly classified values - for class {class_num}"
        elif self.config["prediction_quality"] == "incorrect":
            indices_for_class = project.get_incorrect_prediction_indices_for_class(class_num)
            input_for_class = project.test_x[indices_for_class]
            analyzer_for_class = project.analyzers[analyzer].analyzer_output[indices_for_class]
            analyzer_class_mean = np.mean(analyzer_for_class, axis=0, keepdims=True)
            input_class_mean = np.mean(input_for_class, axis=0, keepdims=True)
            title = f"Incorrectly classified values - for class {class_num}"
        elif self.config["prediction_quality"] == "false_negative":
            indices_for_class = project.get_false_negative_indices(class_num)
            input_for_class = project.test_x[indices_for_class]
            analyzer_for_class = project.analyzers[analyzer].analyzer_output[indices_for_class]
            analyzer_class_mean = np.mean(analyzer_for_class, axis=0, keepdims=True)
            input_class_mean = np.mean(input_for_class, axis=0, keepdims=True)
            title = f"False negatively classified values - for class {class_num}"
        elif self.config["prediction_quality"] == "false_positive":
            indices_for_class = project.get_false_positive_indices(class_num)
            input_for_class = project.test_x[indices_for_class]
            analyzer_for_class = project.analyzers[analyzer].analyzer_output[indices_for_class]
            analyzer_class_mean = np.mean(analyzer_for_class, axis=0, keepdims=True)
            input_class_mean = np.mean(input_for_class, axis=0, keepdims=True)
            title = f"False positively classified values - for class {class_num}"
        

        random_indices_to_plot = random.sample(range(input_for_class.shape[0]), 1)
        random_index = random_indices_to_plot[0]
        fig = plt.figure(figsize=((figureSize.width() - 10)/100, (figureSize.height() - 10)/100))
        ax = fig.add_subplot(111)
        if self.config["plot_type"]["comparison"]["channels"]["single_sample"]["activated"]:
            # single input data
            if self.config["plot_type"]["comparison"]["channels"]["single_sample"]["scatter"]:
                ax.scatter(range(len(input_for_class[random_index,:])), self.normalize(input_for_class[random_index,:], -1, 1), color="r", label="Input input", s=2)
            elif self.config["plot_type"]["comparison"]["channels"]["single_sample"]["line"]:
                ax.plot(self.normalize(input_for_class[random_index,:], -1, 1), color="r", linestyle = "dashed", linewidth = 1, label="Single input")
        if self.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["activated"]:
            # mean input data
            if self.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["scatter"]:
                ax.scatter(range(len(input_class_mean[0,:])), self.normalize(input_class_mean[0,:], -1, 1), color="r", label="Input mean", s=2)
            elif self.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["line"]:
                ax.plot(self.normalize(input_class_mean[0,:], -1, 1), color="r", linewidth = 1, label="Input mean")
        if self.config["plot_type"]["comparison"]["channels"]["single_analyzer_score"]["activated"]:
            # single analyzer
            if self.config["plot_type"]["comparison"]["channels"]["single_analyzer_score"]["scatter"]:
                ax.scatter(range(len(analyzer_for_class[random_index,:])), self.normalize(analyzer_for_class[random_index,:], -1, 1), color="k", label="Single analyzer", s=2)
            elif self.config["plot_type"]["comparison"]["channels"]["single_analyzer_score"]["line"]:
                ax.plot(self.normalize(analyzer_for_class[random_index,:], -1, 1), color="k", linestyle = "dashed", linewidth = 1, label="Single analyzer")
        if self.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["activated"]:
            # mean analyzer
            if self.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["scatter"]:
                ax.scatter(range(len(analyzer_class_mean[0,:])), self.normalize(analyzer_class_mean[0,:], -1, 1), color="k", label="Analyzer mean", s=2)
            elif self.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["line"]:
                ax.plot(self.normalize(analyzer_class_mean[0,:], -1, 1), color="k", linewidth = 1, label="Analyzer mean")
        plt.figure(figsize=(10,6))
        plt.plot(self.normalize(input_class_mean[0,:], -1, 1), color="r", label="Input")
        plt.plot(self.normalize(analyzer_class_mean[0,:], -1, 1), color="k", linestyle = "dashed", linewidth = 0.5, label="Analyzer")

        for h_line in np.arange(-1,1.25,0.5):
            ax.axhline(y = h_line, color = "gray", linestyle = "dashed", linewidth = 0.25)
        
        ax.set_yticks(np.arange(-1, 1.25, 0.25))
        ax.legend(fontsize='large', loc='upper right')
        #ax.set_title(title)
        return fig