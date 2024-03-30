from readit import read_data
import seaborn as sns
import matplotlib.pyplot as plt

df = read_data()
print("Linear Scale for Life expectancy vs GDP:")
g3 = sns.FacetGrid(df, col = "continent", height = 5, col_wrap = 3)
g3.map(sns.scatterplot, 'lifeExp', 'gdpPercap')
plt.yscale('linear')
plt.savefig('figs/linear_lifeExp_vs_gdp.png')
plt.show()

print("Log Scale for Life expectancy vs GDP:")

g4 = sns.FacetGrid(df, col = "continent", height = 5, col_wrap = 3)
g4.map(sns.scatterplot, 'lifeExp', 'gdpPercap')
plt.yscale('log')
plt.savefig('figs/log_lifeExp_vs_gdp.png')
plt.show()
