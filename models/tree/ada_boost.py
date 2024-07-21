import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
# from multiprocessing import Pool
import multiprocess as mp 


def _train(X_train, y_train, X_test, y_test, _n_estimators, _lr):
    estimator = DecisionTreeClassifier(criterion='entropy', max_depth=9, random_state=42) # parameters from tree model
    clf = AdaBoostClassifier(estimator=estimator, n_estimators=int(_n_estimators), learning_rate=_lr, random_state=42, algorithm='SAMME') # consider all features for random split
    #fit the training sets
    clf.fit(X_train, y_train)
    #update trainscore
    trainscore=clf.score(X_train, y_train)
    #update valscore
    valscore=clf.score(X_test, y_test)
    print( 'N estimators', _n_estimators, 'Learning Rate:', _lr, 'Train Score:', trainscore, 'Validation Score:', valscore)
    return valscore, clf




def train_ada_forest(X_train, y_train, X_test, y_test):
    """Train a ada boost forest model, will try seraching parameter space to to tune hyper paramerers"""

    # not many features, 
    n_estimators = np.array([ 50, 75, 100, 150] )
    n_lr = np.array([0.5, 0.75, 1.0, 1.25, 1.5, 2, 5, 10])

    A, B = np.meshgrid(n_estimators, n_lr)
    parameter_space = np.stack( (A.flatten(), B.flatten() ), axis=1 )

    _mtrain = lambda _n, _d : _train(X_train.values, y_train['class'].values, X_test.values, y_test['class'].values, _n, _d)

    with mp.Pool(len(parameter_space)) as p:
        fitting_results = p.starmap(_mtrain, parameter_space)
        test_scores = [_res[0] for _res in fitting_results]
        models = [_res[1] for _res in fitting_results]


    idx = np.argmax(test_scores)
    best = parameter_space[idx]
    print("Best parameters for random forest: {:}".format(best))
    best_model = models[idx]
    return best_model
