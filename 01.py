import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

roll=[1,2,3,4,5,6,7,8,9,10]
marks=[41,43,45,48,34,24,76,56,87,32]
attendence=[75,83,95,93,72,56,78,79,89,77]
gender = ['f','m','f','f',np.nan,'m','m','m','f','m']
data ={ 'roll':roll,'marks':marks,'attendence':attendence,'gender':gender}

df=pd.DataFrame(data)
print(df)
print(df["gender"].isnull().sum())
print(df["gender"].isnull())
print("avg:",df["marks"].mean())
count=df["gender"].value_counts()
print(count)
