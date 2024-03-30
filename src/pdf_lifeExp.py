from readit import read_data
import seaborn as sns
from scipy.stats import norm
import matplotlib.pyplot as plt

df = read_data()
#lifeExp = (df.lifeExp-df['lifeExp'].mean())/df['lifeExp'].std()  --normalization using mean

#using scipy.stats.norm
k = norm.pdf(df.lifeExp,loc=df['lifeExp'].mean(), scale=df['lifeExp'].std())
sns.displot(data = k, x = df.lifeExp ,kde=True,bins='auto',stat='density')
plt.title("PDF of Life Expectancy")
plt.xlabel("Life Expectency")
plt.savefig('figs/pdf_lifeExp.png')
plt.show()
