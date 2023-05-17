import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
df_mt_cars = pd.read_csv("mtcars.csv")
df_mt_cars.head()
df_best_mpg=df_mt_cars[df_mt_cars['mpg']==df_mt_cars['mpg'].max()]
print(df_best_mpg['model'])
df_worst_mpg=df_mt_cars[df_mt_cars['mpg']==df_mt_cars['mpg'].min()]
print(df_worst_mpg['model'])
df_best_hp=df_mt_cars[df_mt_cars['hp']==df_mt_cars['hp'].max()]
df_best_hp['model']
print("median hp is "+str(df_mt_cars['hp'].median()))
df_manual = df_mt_cars[df_mt_cars['am']==1]
df_automatic = df_mt_cars[df_mt_cars['am']==0]
print("Manual avg mpg of car is "+str(df_manual['mpg'].mean()))
print("Automatic avg mpg of car is "+str(df_automatic['mpg'].mean()))
df_manual.head()
df_automatic.head()
fig, ax = plt.subplots(figsize =(6, 4))
ax.hist(df_mt_cars['mpg'])
legend = ['mpg']
plt.xlabel("mpg")
plt.ylabel("frequency")
plt.legend(legend)
plt.title('mpg histogram')
plt.show()
#sns.boxplot(x=df_mt_cars["cyl"],y=df_mt_cars["mpg"]).set_title("cylinder of car vs mpg of car")
pd.crosstab(df_mt_cars.am,df_mt_cars.am,rownames=['automatic'], colnames=['manual'])
print("Correlation between the weight of the car and mpg is "+str(df_mt_cars['wt'].corr(df_mt_cars['mpg'])))