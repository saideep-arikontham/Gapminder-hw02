from readit import read_data
import seaborn as sns
import matplotlib.pyplot as plt

df = read_data()
print("Box plot for Time evolution of life expectancy by continent")
g2 = sns.FacetGrid(df, col = "continent", height = 5, col_wrap = 3)
g2.map(sns.boxplot, 'year', 'lifeExp')

plt.savefig('figs/lifeExp_vs_year.png')
plt.show()
