import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
import random
from matplotlib.collections import LineCollection
from matplotlib.colors import BoundaryNorm, ListedColormap
from matplotlib.cm import ScalarMappable
from matplotlib.colors import LinearSegmentedColormap

class Figure_():
    def __init__(self):
        self.config = {
            "class": None,
            "channels" : None,
            "prediction_quality": "correct",
            "plot_type":{},
            "fig" : None
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
                        "analyzer_relevance_scores": False,
                        "input": False
                    }
                }

    def is_comparison(self):
        return ("comparison" in self.config["plot_type"])

    def is_hist_distribution(self):
        return ("distribution" in self.config["plot_type"] and self.config["plot_type"]["distribution"]["histogram"]["activated"])
    
    def is_box_distribution(self):
        return ("distribution" in self.config["plot_type"] and self.config["plot_type"]["distribution"]["box_plot"]["activated"])


    def normalize(self, data, min_val, max_val):
        return (data - np.min(data)) / (np.max(data) - np.min(data)) * (max_val - min_val) + min_val


    def plot_relevance_score_distribution(self, project, analyzer, figureSize):
        """
        Avarage relevance scores over class

        Creates a histogram for the analyzer given as parameter.
        The plot visualize all the classes' analyzer outcomes' distribution
        Classes seperated by the gorund truth labels
        """

        fig = plt.figure(figsize=((figureSize.width() - 10)/100, (figureSize.height() - 10)/100))
        ax = fig.add_subplot(111)
        colors=['darkred', 'dimgray', 'lightgray']
        alpha_val = 0.5

        color1 = (0 / 255, 139 / 255, 139 / 255)
        color1 = (139 / 255, 0 / 255, 0 / 255)
        color2 = (105 / 255,105 / 255,105 / 255)
        # Define the number of steps for the transition
        num_steps = len(self.config["channels"])

        # Create a list of colors transitioning between color1 and color2
        colors = [color1, (1,1,1),color2]

        # Create the custom colormap
        custom_cmap = LinearSegmentedColormap.from_list("custom_colormap", colors, N=num_steps)
        
    # Create the histogram plot
        for class_num in self.config["channels"]:
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
            if self.config["plot_type"]["distribution"]["histogram"]["analyzer_relevance_scores"]:
                ax.hist(analyzer_class.flatten(), bins=bin_num, color=custom_cmap(class_num), alpha = alpha_val, label=f"Class_{class_num}")
                label = "Relevance scores"
            elif self.config["plot_type"]["distribution"]["histogram"]["input"]:
                ax.hist(class_values.flatten(), bins=bin_num, color=custom_cmap(class_num), alpha = alpha_val, label=f"Class_{class_num}")
                label = "Input"
        #◙ax.set_title(analyzer, fontsize = 16)
        #◙ax.title.set_size(10)
        ax.set_yscale("log")
        ax.legend()
        #ax.set_ylabel('count')
        ax.set_xlabel(label,fontsize = 'medium')
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

        #ax.set_title(f"{analyzer} vs. probability of {classes[class_num]} signal according to the model")
        ax.set_xlabel(f"Probability of signal belongs to class_{class_num}")
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

    def upsample(self, data, factor):
    # Determine the number of new points to be inserted between each original point
        new_points = factor - 1

        # Initialize an empty list to store the new interpolated data
        interpolated_data = []

        for i in range(len(data) - 1):
            interpolated_data.append(data[i])  # Include the original point

            # Calculate the values to be interpolated between the current and next point
            for n in range(1, new_points + 1):
                interpolated_value = data[i] + (data[i + 1] - data[i]) * n / factor
                interpolated_data.append(interpolated_value)

        interpolated_data.append(data[-1])  # Include the last original point

        return interpolated_data

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

        color1 = (0 / 255, 139 / 255, 139 / 255)
        color2 = (139 / 255, 0 / 255, 0 / 255)
        # Define the number of steps for the transition
        num_steps = 256

        # Create a list of colors transitioning between color1 and color2
        colors = [color1, (1,1,1),color2]

        # Create the custom colormap
        custom_cmap = LinearSegmentedColormap.from_list("custom_colormap", colors, N=num_steps)

        fig = plt.figure(figsize=((figureSize.width() - 10)/100, (figureSize.height() - 10)/100))
        ax = fig.add_subplot(111)
        if self.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["activated"]:
            y = self.upsample(self.normalize(input_class_mean[0,:], -1, 1),5)
            x = range(len(y))
            if self.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["scatter"]:
                ax.scatter(x, y, color="indianred", label="Input mean", s=1)
            elif self.config["plot_type"]["comparison"]["channels"]["average_sample_over_class"]["line"]:
                ax.plot(y, color="indianred", linewidth = 1, label="Input mean")
        if self.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["activated"]:
            y = self.upsample(self.normalize(analyzer_class_mean[0,:], -1, 1),5)
            x = range(len(y))
            if self.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["scatter"]:
                ax.scatter(x, y, color="dimgray", label="Analyzer mean", s=1)
            elif self.config["plot_type"]["comparison"]["channels"]["average_analyzer_score"]["line"]:
                ax.plot(y, color="dimgray", linewidth = 1, label="Analyzer mean")
        if self.config["plot_type"]["comparison"]["channels"]["single_sample"]["activated"]:
            # single input data
            color_base = self.upsample(self.normalize(analyzer_for_class[random_index,:], -1, 1),5)
            y = self.upsample(self.normalize(input_for_class[random_index,:], -1, 1), 5)
            x = range(len(y))
            if self.config["plot_type"]["comparison"]["channels"]["single_sample"]["scatter"]:
                #ax.scatter(range(len(input_for_class[random_index,:])), self.normalize(input_for_class[random_index,:], -1, 1), color="r", label="Input input", s=2)
                cmap = plt.get_cmap(custom_cmap)
                norm = plt.Normalize(-1, 1)
                line_colors = cmap(norm(color_base))
                ax.scatter(x, y, color=line_colors, label="Single input", s=3)
                sm = ScalarMappable(cmap=cmap, norm=norm)
                sm.set_array([])  # Set an empty array or list
                cbar = fig.colorbar(sm, ax=ax)
                cbar.set_label('Analyzer value')
            elif self.config["plot_type"]["comparison"]["channels"]["single_sample"]["line"]:
                points = np.array([x, y]).T.reshape(-1, 1, 2)
                segments = np.concatenate([points[:-1], points[1:]], axis=1)
                norm = plt.Normalize(-1, 1)
                lc = LineCollection(segments, cmap=custom_cmap, norm=norm)
                lc.set_array(color_base)
                lc.set_linewidth(3)
                line = ax.add_collection(lc)
                #ax.plot(x, color_base)
                sm = ScalarMappable(cmap=custom_cmap, norm=norm)
                sm.set_array([])
                cbar = fig.colorbar(sm, ax=ax)
                cbar.ax.tick_params(labelsize=8)
                cbar.set_label('Analyzer value')
                ax.set_xlim(0, len(y))
                ax.set_ylim(-1.1, 1.1)
        plt.figure(figsize=(10,6))

        for h_line in np.arange(-1,1.25,0.5):
            ax.axhline(y = h_line, color = "gray", linestyle = "dashed", linewidth = 0.25)
        
        ax.set_yticks(np.arange(-1, 1.25, 0.25))
        ax.legend(fontsize='large', loc='upper right')
        #ax.set_title(title)
        return fig