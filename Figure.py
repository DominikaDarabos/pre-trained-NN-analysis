import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

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

    def is_comparison(self):
        return ("comparison" in self.config["plot_type"])

    def is_distribution(self):
        return ("distribution" in self.config["plot_type"])

    def plot_relevance_score_distribution(self, project, analyzer, class_nums):
        """
        Avarage relevance scores over class

        Creates a histogram for the analyzer given as parameter.
        The plot visualize all the classes' analyzer outcomes' distribution
        Classes seperated by the gorund truth labels
        """
        if class_nums == "all":
            classes = [f"Class_{num+1}" for num in range(project.number_of_classes)]
            possible_classes = range(project.number_of_classes)
        else:
            classes = [f"Class_{num}" for num in class_nums]
            possible_classes = class_nums
        fig = plt.figure()
        ax = fig.add_subplot(111)
        colors=['red', 'dimgray', 'lightgray']
        alpha_val = 0.5
        
    # Create the histogram plot
        for class_num in possible_classes:
            class_indices = project.get_truth_class_indices(class_num)
            class_values = project.test_x[class_indices]
            analyzer_class = project.analyzers[analyzer].analyzer_output[class_indices]
            if class_values.shape[0] == 0:
                continue
            ax.hist(analyzer_class.flatten(), bins=30, color=colors[class_num], alpha = alpha_val, label=classes[class_num])
        ax.set_title(analyzer, fontsize = 16)
        ax.title.set_size(10)
        ax.set_yscale("log")
        ax.legend()
        #ax.set_ylabel('count')
        ax.set_xlabel('Relevance scores',fontsize = 11)
        #plt.savefig(f"{Path.cwd()}\..\plots\latest\ecg\hist_plot_distribution\dist_ecg_{title}.png")
        #plt.show()
        return fig
    
    def plot_grouped_boxplot(self, project, class_num, analyzer):
        class_probabilities = project.predictions[:, class_num]
        sorted_indices = np.argsort(class_probabilities)
        
        #plt.figure(figsize=(10,6))
        fig = plt.figure()
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
        ax.boxplot(output[:,sorted_correct_pos_indices[::3]], positions=sorted_correct_pos_indices[::3], flierprops = dict(marker='.', markersize=3, linestyle='none', markeredgecolor='indianred'), patch_artist=True, boxprops = dict(facecolor = "indianred"))
        ax.boxplot(output[:,sorted_correct_neg_indices[::3]], positions=sorted_correct_neg_indices[::3], flierprops = dict(marker='.', markersize=3, linestyle='none', markeredgecolor='powderblue'), patch_artist=True, boxprops = dict(facecolor = "powderblue"))
        ax.boxplot(output[:,sorted_false_neg_indices[::3]], positions=sorted_false_neg_indices[::3], flierprops = dict(marker='.', markersize=3, linestyle='none', markeredgecolor='darkcyan'), patch_artist=True, boxprops = dict(facecolor = "darkcyan"))
        ax.boxplot(output[:,sorted_false_pos_indices[::3]], positions=sorted_false_pos_indices[::3], flierprops = dict(marker='.', markersize=3, linestyle='none', markeredgecolor='darkred'), patch_artist=True, boxprops = dict(facecolor = "darkred"))

        legend_patches = [Patch(facecolor='powderblue', edgecolor='powderblue', label='True negative'),
                            Patch(facecolor='darkcyan', edgecolor='darkcyan', label='False negative'),
                            Patch(facecolor='indianred', edgecolor='indianred', label='True positive'),
                            Patch(facecolor='darkred', edgecolor='darkred', label='False positive')]

        ax.legend(handles=legend_patches, loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=len(legend_patches))

        classes = ["normal", "abnormal"]
        ax.set_title(f"{analyzer} vs. probability of {classes[class_num]} signal according to the model")
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
        #plt.show()
        return fig