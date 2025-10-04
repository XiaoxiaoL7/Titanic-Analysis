import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

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


train['Embarked'].fillna('S', inplace=True)
train.drop(columns=['Cabin'], inplace=True)
train['FamilySize'] = train['SibSp'] + train['Parch'] + 1



train['IsAlone'] = 0
train.loc[train['FamilySize'] == 1, 'IsAlone']= 1

sns.barplot(x='Sex', y='Survived', data=train, hue='IsAlone')
plt.show()



