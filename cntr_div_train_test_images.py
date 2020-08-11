# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 10:57:41 2019

Creates train and test splits at the IMAGE LEVEL to prep for thumbnail extraction in countr_cnn_1

@author: smcguire
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## read dataframe of unique images with annotation info
df_unique = pd.read_pickle('./df_unique.pkl')

# create df_test from every 4th image
df_test = df_unique[df_unique.index % 4 == 0] 

# create df_train_val from every image not in df_test
df_train_val = df_unique[df_unique.index % 4 != 0]

# reset indexes
df_test = df_test.reset_index(drop=True)   
df_train_val = df_train_val.reset_index(drop=True)

# pickle dataframes
df_test.to_pickle('./df_test.pkl')      
df_train_val.to_pickle('./df_train_val.pkl')  
    
    