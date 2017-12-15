'''
Created on Dec 7, 2017

@author: jamesyu
'''
import pandas as pd
from sklearn.cross_validation import ShuffleSplit
from sklearn.svm import SVC

%matplotlib inline


if __name__ == '__main__':
    data = pd.read_csv('../data.csv')
    
    print data.describe()