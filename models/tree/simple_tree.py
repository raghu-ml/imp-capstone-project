import numpy as np
from sklearn import tree

def train_simple_tree(X_train, y_train, X_test, y_test):
    # work through number of depths to find best tree
    training_scores = []
    test_scores = []
    max_depth = 20
    for i in range(1, max_depth+1):
        clf = tree.DecisionTreeClassifier(max_depth=i, criterion='entropy', random_state=42)
        #fit the training sets
        clf.fit(X_train, y_train)
        #update trainscore
        trainscore=clf.score(X_train, y_train)
        #update valscore
        valscore=clf.score(X_test, y_test)
        print( 'Depth:', i, 'Train Score:', trainscore, 'Validation Score:', valscore)
        training_scores.append(trainscore)
        test_scores.append(valscore)

    best_depth = np.argmax(test_scores)+1

    print ("Best Tree Depth {:}".format(best_depth))
    best_model = tree.DecisionTreeClassifier(max_depth=best_depth, criterion='entropy')
    return best_model.fit(X_train, y_train)