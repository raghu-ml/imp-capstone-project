import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import multiprocess as mp 


def _train(X_train, y_train, X_test, y_test, K):
    clf = KNeighborsClassifier(n_neighbors=K) #runs the one-versus-rest approach in multi-class classification
    clf.fit(X_train, y_train)

    #update trainscore
    trainscore=clf.score(X_train, y_train)
    #update valscore
    valscore=clf.score(X_test, y_test)
    print('Neighbours: ', K, 'Train Score:', trainscore, 'Validation Score:', valscore)
    return valscore, clf


def train_knn(X_train, y_train, X_test, y_test):

    neighbours = [5, 10, 15, 20, 25, 30, 40, 50 , 100]

    _mtrain = lambda _k : _train(X_train.values, y_train['class'].values, X_test.values, y_test['class'].values, _k)

    with mp.Pool(len(neighbours)) as p:
        fitting_results = p.map(_mtrain, neighbours)
        test_scores = [_res[0] for _res in fitting_results]
        models = [_res[1] for _res in fitting_results]


    idx = np.argmax(test_scores)
    best = neighbours[idx]
    print("Best parameters for KNN : {:}".format(best))
    best_model = models[idx]
    return best_model