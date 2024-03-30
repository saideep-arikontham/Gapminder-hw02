.PHONY: data, clean

data/gapminder.tsv:
	mkdir -p data
	cd data; curl -LO https://raw.githubusercontent.com/jennybc/gapminder/main/inst/extdata/gapminder.tsv

plot1: data/gapminder.tsv
	mkdir -p figs
	python -B src/lifeExp_distribution.py

plot2: data/gapminder.tsv
	mkdir -p figs
	python -B src/lifeExp_over_years.py

plot3: data/gapminder.tsv
	mkdir -p figs
	python -B src/lifeExp_vs_gdp.py

plot4: data/gapminder.tsv
	mkdir -p figs
	python -B src/pdf_lifeExp.py

clean:
	rm data/gapminder.tsv
