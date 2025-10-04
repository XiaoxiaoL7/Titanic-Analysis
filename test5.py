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

sns.barplot(x='Sex', y='Survived', data=train, hue='Sex')
plt.show()