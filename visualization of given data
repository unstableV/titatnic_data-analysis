import pandas as pd
from pandas import Series,DataFrame
titanic_df=pd.read_csv('C:/Users/unstableV/Desktop/titanic project/train.csv')
titanic_df.head()
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
sns.factorplot('Sex',data=titanic_df,kind="count")
sns.factorplot('Pclass',data=titanic_df,hue='Sex',kind="count")
def male_female_child(passenger):
    age,sex=passenger
    
    if age<16:
        return 'child'
    else:
        return sex
titanic_df['person']=titanic_df[['Age','Sex']].apply(male_female_child,axis=1)
titanic_df[0:10]
sns.factorplot('Pclass',data=titanic_df,hue='person',kind="count")
titanic_df['Age'].hist(bins=70)
titanic_df['Age'].mean()
titanic_df['person'].value_counts()
