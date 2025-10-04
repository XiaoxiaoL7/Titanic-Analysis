import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns
train = pd.read_csv('train.csv')
copy = train.copy()

# fill NaN values in age column with mean value. use the .fillna method. 
# Don't forget to set the inplace parameter to True
copy['Age'].fillna(copy['Age'].mean(), inplace=True)

#create a subplot with 2 plots to copare the age distribution before and after filling NaN value
fig, ax= plt.subplots(1,2,figsize=(15,5))
sns.histplot(train['Age'].dropna(), ax=ax[0], bins= 15)
sns.histplot(copy['Age'], ax=ax[1], bins= 15)
ax[0].set_title('Before filling NaN values')
ax[1].set_title('After filling NaN values')
plt.show()