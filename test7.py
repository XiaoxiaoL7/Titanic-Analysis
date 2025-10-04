import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
train = pd.read_csv('train.csv')

sns.barplot(x='Sex', y='Survived', data=train, hue='Pclass')
plt.show()
