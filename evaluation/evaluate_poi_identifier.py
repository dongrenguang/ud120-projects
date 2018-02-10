#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

reg = tree.DecisionTreeClassifier()
reg.fit(features_train, labels_train)

pred = reg.predict(features_test)

accu = accuracy_score(pred, labels_test)

# print pred
# print labels_test
# count = 0
# for i in range(len(pred)):
#     if pred[i] == labels_test[i] and pred[i] == 0.0:
#     # if labels_test[i] == 1.0:
#         count = count + 1
# # print len(labels_test)
# print count

from sklearn.metrics import precision_score, recall_score
print recall_score(labels_test, pred)