import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,MinMaxScaler,StandardScaler

#Task-1

df = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 2, 5],
    'age':         [25, np.nan, 35, np.nan, np.nan, 40],
    'city':        ['Mumbai', 'Delhi', np.nan, 'Mumbai', 'Delhi', np.nan],
    'gender':      ['Male', 'Female', 'Female', 'Male', 'Female', 'Male'],
    'annual_income': [40000, 80000, 60000, 120000, 80000, 95000]
})

df["age"]=df["age"].fillna(df["age"].median())
df["city"]=df["city"].fillna(df["city"].mode()[0])

df=df.drop_duplicates()

#Task-2
df=pd.get_dummies(df,columns=["city"])
Le=LabelEncoder()
df["gender"]=Le.fit_transform(df["gender"])

print("Encoded Data:\n",df)

#Task-3
df_minmax=df.copy()
df_standard=df.copy()
cols=['age', 'annual_income']

minmax=MinMaxScaler()
df_minmax[cols]=minmax.fit_transform(df_minmax[cols])


print("\nMin-Max Scaled Data:\n", df_minmax)

standard=StandardScaler()
df_standard[cols]=standard.fit_transform(df_standard[cols])

print("\nStandard Scaled Data:\n", df_standard)