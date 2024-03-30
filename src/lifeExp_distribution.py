from readit import read_data
import seaborn as sns
import matplotlib.pyplot as plt

df = read_data()
print("Distribution of Life Expectancy for each continent")
g1 = sns.FacetGrid(df, col = "continent", col_wrap = 3)
g1.map(sns.histplot, "lifeExp")

#g1.savefig('figs/lifeExp_distribution.png')
plt.savefig('figs/lifeExp_distribution.png')
plt.show()


