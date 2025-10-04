import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   
import numpy as np

train = pd.read_csv('train.csv')
print(train.shape)
print(train.head(5))
print(train.isnull().sum())

# make a copy of the dataframe
copy = train.copy()
# drop all nan values of the age column using dropna.
# don't forget to set the inplace parameter to True

copy['Age'].dropna(inplace=True)    
sns.displot(copy['Age'], bins = 15, kde=False)
plt.show()














