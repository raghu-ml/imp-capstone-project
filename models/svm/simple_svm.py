import numpy as np
from sklearn.svm import SVC
import multiprocess as mp 


def _train(X_train, y_train, X_test, y_test, kernel):
    clf = SVC(kernel=kernel) #runs the one-versus-rest approach in multi-class classification
    clf.fit(X_train, y_train)

    #update trainscore
    trainscore=clf.score(X_train, y_train)
    #update valscore
    valscore=clf.score(X_test, y_test)
    print( 'Kernel: ', kernel, 'Train Score:', trainscore, 'Validation Score:', valscore)
    return valscore, clf




def train_svm(X_train, y_train, X_test, y_test):

    kernels = ['linear', 'rbf', 'poly']

    _mtrain = lambda _k : _train(X_train.values, y_train['class'].values, X_test.values, y_test['class'].values, _k)

    with mp.Pool(len(kernels)) as p:
        fitting_results = p.map(_mtrain, kernels)
        test_scores = [_res[0] for _res in fitting_results]
        models = [_res[1] for _res in fitting_results]


    idx = np.argmax(test_scores)
    best = kernels[idx]
    print("Best parameters for SVM : {:}".format(best))
    best_model = models[idx]
    return best_model
