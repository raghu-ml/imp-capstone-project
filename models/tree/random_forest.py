import numpy as np
from sklearn.ensemble import RandomForestClassifier
# from multiprocessing import Pool
import multiprocess as mp 


def _train(X_train, y_train, X_test, y_test, _n_estimators, _depth):
    clf = RandomForestClassifier(n_estimators=_n_estimators, max_depth=_depth, criterion='entropy', max_features=None, random_state=42) # consider all features for random split
    #fit the training sets
    clf.fit(X_train, y_train)
    #update trainscore
    trainscore=clf.score(X_train, y_train)
    #update valscore
    valscore=clf.score(X_test, y_test)
    print( 'N estimators', _n_estimators, 'Max Depth:', _depth, 'Train Score:', trainscore, 'Validation Score:', valscore)
    return valscore, clf




def train_random_forest(X_train, y_train, X_test, y_test):
    """Train a random forest model, will try seraching parameter space to to tune hyper paramerers"""

    # not many features, 
    n_estimators = np.array([ 50, 75, 100, 150] )
    n_dephts = np.array([7, 8, 9, 10, 11, 12])

    A, B = np.meshgrid(n_estimators, n_dephts)
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
