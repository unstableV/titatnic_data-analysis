import pandas as pd
from pandas import Series,DataFrame
titanic_df=pd.read_csv('C:/Users/unstableV/Desktop/titanic project/train.csv')
titanic_df.head()
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
titanic_df.head()
titanic_df['Alone']=titanic_df.SibSp+titanic_df.Parch
titanic_df['Alone']
titanic_df['Alone'].loc[titanic_df['Alone']>0]='With Family'
titanic_df['Alone'].loc[titanic_df['Alone']==0]='Alone'
titanic_df.head()
sns.factorplot('Alone',data=titanic_df,palette='Blues',kind='count')
titanic_df['Survivor']=titanic_df.Survived.map({0:'no',1:'yes'})
sns.factorplot('Survivor',data=titanic_df,kind='count')
sns.factorplot('Pclass','Survived',hue='person',data=titanic_df)
sns.lmplot('Age','Survived',hue='Pclass',data=titanic_df)
generations =[10,20,40,60,80]
sns.lmplot('Age','Survived',hue='Pclass',data=titanic_df)
sns.lmplot('Age','Survived',hue='Sex',data=titanic_df,x_bins=generations)
