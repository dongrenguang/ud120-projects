#!/usr/bin/python

def cmp(x, y):
    if abs(x[2]) > abs(y[2]):
        return 1
    elif abs(x[2]) < abs(y[2]):
        return -1
    else:
        return 0


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    
    ### your code goes here
    for index in range(len(ages)):
        cleaned_data.append((ages[index][0], net_worths[index][0], net_worths[index][0] - predictions[index][0]))

    cleaned_data.sort(cmp)
    count = int(round(len(ages) * 0.9))
    cleaned_data = cleaned_data[0:count]
    
    return cleaned_data

