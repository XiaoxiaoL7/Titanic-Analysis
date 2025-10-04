import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns
train = pd.read_csv('train.csv')
def age_generator(df):
# save the mean value of the age column here 
    mean_age= df['Age'].mean()
    std_age= df['Age'].std()
    null_count_age = df['Age'].isnull().sum()
    age_random_list = np.random.randint(mean_age - std_age, mean_age + std_age, size = null_count_age)
    df.loc[df['Age'].isnull(), 'Age'] = age_random_list
    return df

train = age_generator(train)

fig, ax = plt.subplots(1,2,figsize=(15, 5))
sns.boxplot(x='Survived', y='Age', data=train[train['Sex']=='female'], ax=ax[0] )
sns.boxplot(x='Survived', y='Age', data=train[train['Sex']=='male'], ax=ax[1])
ax[0].set_title('Female Age Distribution by Survival')
ax[1].set_title('Male Age Distribution by Survival')
plt.show()