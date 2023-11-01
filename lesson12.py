# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:06:12 2023

@author: fanny
"""

import pandas as pd

print(pd.__version__)
df=pd.read_csv("Educational_Attainment_20231027.csv")
print(df.head())
print(df)