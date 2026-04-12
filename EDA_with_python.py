import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
'''plt.hist(df["total_bill"],bins=5,edgecolor="black")
plt.title("Dstribution of total bill (5bins)")
plt.xlabel("TOtal bill")
plt.ylabel("Frequency")
plt.show()

plt.hist(df["total_bill"],bins=20,edgecolor="black",color="red")
plt.title("Dstribution of total bill (20-bins)")
plt.xlabel("Total bill")
plt.ylabel("Frequency")
plt.show()'''

'''sns.histplot(df["total_bill"],kde=True,bins=5)
plt.title("Dstribution of total bill (5bins)")
plt.xlabel("TOtal bill")
plt.ylabel("Frequency")
plt.show()

sns.histplot(df["total_bill"],kde=True,bins=20,color="red")
plt.title("Distribution of total bill (20bins)")
plt.xlabel("TOtal bill")
plt.ylabel("Frequency")
plt.show()'''

'''fig=px.histogram(df["total_bill"],nbins=20,title="Distribution of total bill (20bins)")
fig.show()'''



'''fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].hist(df['total_bill'], bins=5, color='steelblue', edgecolor='black')
axes[0].set_title('Total Bill Distribution (5 Bins)')
axes[0].set_xlabel('Total Bill (USD)')
axes[0].set_ylabel('Frequency')

axes[1].hist(df['total_bill'], bins=20, color='coral', edgecolor='black')
axes[1].set_title('Total Bill Distribution (20 Bins)')
axes[1].set_xlabel('Total Bill (USD)')
axes[1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()'''

sns.boxplot(df,x="day",y="total_bill",order=['Thur', 'Fri', 'Sat', 'Sun'])
plt.title("Toatl bill distribution by day")
plt.xlabel("Day")
plt.ylabel("Totalbill")
plt.show()

q1 = df[df['day'] == 'Sat']['total_bill'].quantile(0.25)
q3 = df[df['day'] == 'Sat']['total_bill'].quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print(f"Q1: {q1}, Q3: {q3}, IQR: {iqr}")
print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")

outliers = df[(df['day'] == 'Sat') & 
              ((df['total_bill'] < lower_bound) | (df['total_bill'] > upper_bound))]
print(outliers[['total_bill']])


fig=px.scatter(
    df,
    x="total_bill",
    y="tip",
    color="time",
    hover_data=["day","size"],
    title="Tip vs Total Bill by Meal Time (Lunch vs Dinner)"
)
fig.show()