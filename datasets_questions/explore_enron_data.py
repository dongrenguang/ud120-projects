#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""
from __future__ import division
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print len(enron_data)
#
# print len(enron_data['METTS MARK'])
#
# count = 0
# for key in enron_data:
#     if enron_data[key]['poi'] == 1:
#         count = count + 1
# print count
#
# print enron_data['PRENTICE JAMES']['total_stock_value']
#
# print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
#
# print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

# for key in enron_data:
#     if key[0] == 'A' or key[0] == 'F':
#         print key
#
# print enron_data['SKILLING JEFFREY K']['total_payments']
# print enron_data['LAY KENNETH L']['total_payments']
# print enron_data['FASTOW ANDREW S']['total_payments']
#

# print enron_data['SKILLING JEFFREY K']
# count = 0
# for key in enron_data:
#     if enron_data[key]['email_address'] != 'NaN':
#         count = count + 1
# print count


# import sys
# from time import time
# sys.path.append("../tools/")
# from feature_format import featureFormat
# from feature_format import targetFeatureSplit
#
# feature_list = ["salary"]
# data_array = featureFormat(enron_data, feature_list)
# # label, features = targetFeatureSplit(data_array)
# print data_array
#
#
# count = 0
# for key in enron_data:
#     if enron_data[key]['total_payments'] == 'NaN':
#         count = count + 1
#
# print count + 10

count = 0
poiCount = 0
for key in enron_data:
    if enron_data[key]['poi'] == True:
        poiCount = poiCount + 1
        if enron_data[key]['total_payments'] == 'NaN':
            count = count + 1

print count,  poiCount
#
# print len(enron_data) + 10
