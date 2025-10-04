import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns
train = pd.read_csv('train.csv')
copy = train.copy()

def age_generator(df):
# save the mean value of the age column here 
    mean_age= df['Age'].mean()
    std_age= df['Age'].std()
    null_count_age = df['Age'].isnull().sum()
    age_random_list = np.random.randint(mean_age - std_age, mean_age + std_age, size = null_count_age)
    df.loc[df['Age'].isnull(), 'Age'] = age_random_list
    return df

copy = age_generator(train.copy())
#create a subplot with 2 plots to copare the age distribution before and after filling NaN value
fig, ax= plt.subplots(1,2,figsize=(15,5))
sns.histplot(train['Age'], ax=ax[0], bins= 15)
sns.histplot(copy['Age'], ax=ax[1], bins= 15)
ax[0].set_title('Before filling NaN values')
ax[1].set_title('After filling NaN values')
plt.show()
# fill NaN values in age column with random values between (mean - std) and (
