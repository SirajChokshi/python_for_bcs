import matplotlib.pyplot as plt
from src import dataset
from src import k_nearest_neighbor as knn
from src import logistic_regression as lr
from src import visualization as vis
from src import analyses
import numpy as np

np.set_printoptions(precision=3)

# data file
FILE_NAME = 'data/data2.csv'

# Dataset Parameters
TRAINING_PROPORTION = .75
NORMALIZE = False
SVD_DIM = 0

# print amount parameters
VERBOSE = True

# plot options
WORD_LABELS = True
PLOT_SVDS = False  # whether to plot svd, raw features if False

F1 = 0  # feature (or SV) 1 for feature-by-feature scatter plot
F2 = 1  # feature (or SV) 2 for feature-by-feature scatter plot

F_INDEX = 1  # feature to plot in feature-category scatter plot

C_INDEX = 1  # category to plot to visualize logistic regression results

SIM = None  # if cosine, heatmap will be of word similarities, if None, will be of word-feature values heatmap

# KNN Parameters
DISTANCE_METRIC = 'cosine'
MIN_MAX_KNN = (1, 5)

# Logistic Regression Parameters
LEARNING_RATE = 0.1
NUM_EPOCHS = 1000
OUTPUT_FILE_NAME = 'log_reg_results.txt'


def main():

    my_data = dataset.Dataset(FILE_NAME, TRAINING_PROPORTION, NORMALIZE, SVD_DIM, VERBOSE)

    # analyses.compute_feature_correlations(my_data, VERBOSE)
    #
    # vis.plot_feature_scatter(my_data, WORD_LABELS, F1, F2, PLOT_SVDS)
    # vis.plot_feature_by_category_scatter(my_data, F_INDEX, WORD_LABELS, PLOT_SVDS)
    # vis.plot_hierarchical_cluster(my_data, PLOT_SVDS, SIM)
    #
    # my_knn = knn.Knn(my_data, MIN_MAX_KNN, DISTANCE_METRIC, VERBOSE)
    # my_knn.train()
    # my_knn.test(my_data.test_list, my_data.training_list, my_knn.best_k)
    #
    # my_logreg = lr.LogisticRegression(my_data, LEARNING_RATE, NUM_EPOCHS, VERBOSE, OUTPUT_FILE_NAME)
    # my_logreg.train()
    # my_logreg.test()
    #
    # vis.plot_weight_heat_map(my_logreg)
    # vis.plot_ypredict_yactual_scatter(my_logreg, WORD_LABELS, C_INDEX)


main()



