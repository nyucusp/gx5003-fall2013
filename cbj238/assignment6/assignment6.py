"""
assignment6.py
author: Christopher Jacoby <cbj238@nyu.edu>
"""

import argparse, csv
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.stats import mode

LABELLED_DATA = "labeled_data.csv"
UNLABELLED_DATA = "unlabeled_data.csv"
DEBUG = False

def read_csv_to_dict(csvfilename):
    csv_data = []
    with open(csvfilename, 'rb') as csvfile:
        datareader = csv.DictReader(csvfile)
        for row in datareader:
            csv_data.append(row)

    return datareader.fieldnames, csv_data

def datadict_to_nparray(keys, data):
    dataarr = np.zeros([len(data), len(keys)])
    for point_index in xrange(len(data)):
        for key_index in xrange(len(keys)):
            dataarr[point_index, key_index] = np.float( data[point_index][keys[key_index]] )
    return dataarr

def get_data():
    keys1, labelled_data = read_csv_to_dict(LABELLED_DATA)
    labelled_data_arr = datadict_to_nparray(keys1, labelled_data)

    keys2, unlabelled_data = read_csv_to_dict(UNLABELLED_DATA)
    unlabelled_data_arr = datadict_to_nparray(keys2, unlabelled_data)

    return (keys1, labelled_data_arr), (keys2, unlabelled_data_arr)

def get_10_fold_cross_validated_sets_from_data(data, N=10):
    """ splits the input, data, into 10 chunks, randomly sampled from the data
    for 10-fold cross validation.
    N is the number of folds, default 10.
    """
    # Start off by randomly sampling the data.
    if DEBUG:
        print "Creating Cross Validation Folds..."

    indices = np.random.permutation(data.shape[0])
    fold_index_hop = len(data) / N

    # build the folds from the randomized samples.
    result_sets = []
    for index in xrange(N):
        fold_start = index * fold_index_hop
        fold_end = (index + 1) * fold_index_hop

        result_sets.append( data[indices[fold_start : fold_end]] )

    if DEBUG:
        print "Created {0} folds from {1} input points, with {2} points each" \
            .format(N, len(data), fold_index_hop)
    return result_sets

def get_train_test_sets(crossval_data, leave_out_index):
    """ Given the folds returned from
    get_10_fold_cross_validated_sets_from_data, and the index for which
    fold to leave out, return (training_set, test_set)
    """
    training_set = None
    test_set = None

    for index in xrange(len(crossval_data)):
        if index is leave_out_index:
            test_set = crossval_data[index]
        else:
            if training_set is None:
                training_set = crossval_data[index]
            else:
                training_set = np.concatenate( (training_set, crossval_data[index]) )

    return training_set, test_set

def enforce_shape(input):
    if len(input.shape) == 1:
        input.shape = (input.shape[0], 1)

def generate_model(training_set, order):
    """ returns the model using ordinary least squares """
    # The input data (population)
    x = training_set[:,1]
    # The result data (num_incidents)
    t = training_set[:,2]

    # \Phi(x)=x^degree/order ; the basis expansion, etc.
    x2 = x ** order

    #Add ones for the intercept and combine everything into X_nonlin=[ones X \Phi(X)]
    enforce_shape(x)
    enforce_shape(x2)
    X_nonlin = np.concatenate((np.ones((len(x),1)), x, x2),axis=1)

    # Solve to get OLS estimate
    # obtaining the parameters by fitting a hyper-plane in this expanded space
    w_ols = np.linalg.lstsq(X_nonlin,t)[0]

    # Our OLS estimator/predictions (on the training data).
    # You can try creating "unseen"/test data, coding cross-validation
    # to choose model complexity, and predict on it as well
    t_hat = X_nonlin.dot(w_ols)

    return t_hat

def get_rmse(t, t_hat):
    """ Returns the root mean squared error (RMSE), given the original
    observations, and the predicted results from the model.
    RMSE(t, t_hat) = sqrt( avg((t - t_hat)^2) )"""
    if (len(t) == len(t_hat)):
        return np.sqrt( np.sum( ( (t - t_hat) ** 2)) / len(t) )
    else:
        raise Exception("rmse - input vectors are not the same size")

def get_r_squared_error(t, t_hat):
    """ Returns the r-squared error, given the original observations (t) and the
    predicted results (t_hat):
    r_squared_error(t, t_hat) = 1 - (sum( (t_n - t_hat_n)^2 ) / ( (t_n - avg(t_hat)^2)"""
    if len(t) == len(t_hat):
        return 1 - ( np.sum( (t - t_hat)**2 ) / np.sum( (t - np.average(t))**2 ) )
    else:
        raise Exception("r_squared_error - input vectors are not the same size")

def evaluate_model(data, model):
    """ returns rmse, rsquared """
    return (get_rmse(data, model), get_r_squared_error(data, model) )

def part_a(data):
    """ Plot the data and reason about any phenomena of interest you see
    (you should report it in a short text).

    takes: n x m numpy array;
    n is the number of samples, m is the number of features (2 for this example)
    Plots the first feature against the second."""

    fig, ax = plt.subplots()

    ax.plot(data[1][:, 1], data[1][:,2], 'ko')

    ax.grid(True)
    ax.margins(.02, .02)
    ax.set_title("")
    ax.set_xlabel(data[0][1])
    ax.set_ylabel(data[0][2])

    fig.patch.set_facecolor('white')
    plt.show()


def part_b(crossval_folds):
    """ Using the labeled dataset produce python codes that report the
    10-fold-Cross Validated RMSE and R^2 scores for OLS
    (num_incidents ~ f(population)) with polynomial models from
     1 to 5th order (e.g. for second order t ~ w_0 + w_1*x1 + w2*x^2)
      and select a model complexity (polynomial order) based on these scores.
    """
    print "Part B."
    fig, ax = plt.subplots(1, 2)
    draw_colors = ['r','g','b','c','m']

    rmse_scores = []
    rsquared_scores = []
    all_models = []
    rmse_bests = []
    rsquared_bests = []
    # for each fold, get data, leaving the other folds out.
    for index in xrange(len(crossval_folds)):
        if DEBUG:
            print "Fold: ", index

        training_set, test_set = get_train_test_sets(crossval_folds, index)

        # calculate the scores for each order
        order_rmse = []
        order_rsquared = []
        order_models = []
        for order in xrange(1, 6):
            model = generate_model(training_set, order)
            rmse, rsquared = evaluate_model(training_set[:, 1], model)
            order_rmse.append(rmse)
            order_rsquared.append(rsquared)
            order_models.append(model)

            if DEBUG:
                print "\tOrder: %d | RMSE: %.2e | R^2: %.2f" % (order, rmse, rsquared)

        rmse_scores.append( order_rmse )
        rsquared_scores.append( order_rsquared )
        rmse_bests.append( argmin(order_rmse))
        rsquared_bests.append( argmax(order_rsquared))
        if DEBUG:
            print "\tMin RMSE: {0}\tMax R^2: {1}".format(rmse_bests[-1] + 1, rsquared_bests[-1] + 1)

        ax[0].plot(range(1,6), order_rmse, '-')
        ax[1].plot(range(1,6), order_rsquared, '-')

    rmse_order_mode = mode(rmse_bests)[0] + 1
    rsquared_order_mode = mode(rsquared_bests)[0] + 1
    if DEBUG:
        print "Selected Model: {0} from RMSE, {1} from R^2".format( rmse_order_mode, rsquared_order_mode)
    selected_order = rmse_order_mode[0]
    if not (len(rmse_order_mode) == 1 and len(rsquared_order_mode) == 1 and rmse_order_mode == rsquared_order_mode):
        """Okay, I could probably make this smarter. Placeholder for now. Also,
        I haven't yet observed a case where any of those conditions were true.

        And so, I chose the 'minimum' order if they were different, under the
        assumption that lower orders are better."""
        selected_order = min(rmse_order_mode, rsquared_order_mode)
    print "Model Order Decided:", selected_order

    ax[0].set_xticks(range(6))
    ax[1].set_xticks(range(6))
    ax[0].grid(True)
    ax[1].grid(True)
    ax[0].margins(.02, .02)
    ax[1].margins(.02, .02)
    ax[0].set_title("RMSE Score per Fold")
    ax[1].set_title("R^2 Score per Fold")
    ax[0].set_xlabel('Order')
    ax[1].set_xlabel('Order')

    # fig.tight_layout()
    fig.patch.set_facecolor('white')
    plt.show()

    return selected_order, rmse_scores


def part_c(data, order, rmse_scores):
    """ Compute the RMSE on the whole training set (all your data) and plot it
     against the 10-fold CV average (with std error-bars) as a function of model
     complexity (y-axis RMSE, x-axis order of polynomial). What do you observe?.
    """
    print "Part c"
    model = generate_model(data, order)
    rmse, rsquared = evaluate_model(data[:, 1], model)

    arr_rmse_scores = np.array(rmse_scores)
    mean_rmse = np.average(arr_rmse_scores, axis=0)
    std_rmse = np.std(arr_rmse_scores, axis=0)

    # print order, rmse
    # print mean_rmse, std_rmse
    ind = np.arange(arr_rmse_scores.shape[1]) + 1
    width = .35

    fig, ax = plt.subplots()

    ax.bar(ind, mean_rmse, width, color='r', yerr=std_rmse, ecolor='b')
    ax.axhline(rmse, color='g')
    ax.text(0.4, rmse+5000, "RMSE for whole set") #, rotation='vertical', verticalalignment='bottom'
    ax.arrow(0.4, rmse+5000, 0, -5000)

    ax.grid(True)
    ax.margins(0.2, 0)
    ax.set_title("RMSE for order, with RMSE across all data overlaid")
    ax.set_xlabel('Order')
    ax.set_ylabel('RMSE')
    ax.set_ylim(mean_rmse.min() * .8, mean_rmse.max() * 1.1)
    plt.xticks(ind+width/2, ind)

    fig.patch.set_facecolor('white')
    plt.show()


def part_d():
    """ Build your final OLS model (you can use as many predictor
        variables/features as you want or other external data matched by
        zip code, again be careful not to overfit) and submit your predictions
        for the number of incidents on the test data.
    """
    pass

def main():
    global DEBUG
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--run", help="part to run, if you just want to run one.")
    parser.add_argument("-d", "--debug", action="store_true", help="debug mode")
    args = parser.parse_args()
    DEBUG = args.debug

    ld, uld = get_data()
    ten_fold_data = get_10_fold_cross_validated_sets_from_data(ld[1])

    if DEBUG:
        print "Labelled Data - Fields: {0}\nLength: {1}".format(ld[0], len(ld[1]))
        print "\nUnlabelled Data - Fields: {0}\nLength: {1}".format(uld[0], len(uld[1]))

    if not args.run or args.run == "a":
        part_a(ld)

    if not args.run or args.run == "b" or args.run=="c":
        selected_order, rmse_scores = part_b(ten_fold_data)

        if not args.run or args.run == "c":
            part_c(ld[1], selected_order, rmse_scores)

    if not args.run or args.run == "d":
        part_d()

if __name__ == "__main__":
    main()
