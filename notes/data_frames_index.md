# Data frames and indexing

This is from an extension to the introduction to data frames notebook.  On reflection this made the page too long, and the material needs to go somewhere else.

**Text follows**

Notice that, above 15 billion GDP per million population, all the rich countries have a very similar maternal mortality.  The only slight outlier seems to be the country with the second highest GDP per million; it also has the highest maternal mortality of these richer countries.  Which country is that?

## The index


This brings us to the *index* of Series and DataFrames.  The index are *labels* for each row.  Series have these, as do DataFrames.   Here is the display of the table of rich countries sorted by maternal mortality ratio.

```{python}
rich_by_descending_mmr
```

Notice the numbers on the extreme left.  These numbers are labels - they identify the row.  Look down to the row for the United States.  It has label (index value) 202.


Now we get a Series from this DataFrame, by indexing to select a column:

```{python}
country_name = rich_by_descending_mmr["country_name"]
```

As we already know, the result is a Series:

```{python}
type(country_name)
```

We ask the notebook to show us the `country_name` Series:

```{python}
country_name
```

Notice that the `country_name` Series has the same labels (index values) as the data frame.  We can see that the United States still has label 202.


Now let's repeat our calculation of GDP per million:

```{python}
rich_gdp = rich_by_descending_mmr['gdp_us_billion']
rich_gdp
```

Notice the labels are the same, so 202 labels the United States.

```{python}
rich_population = rich_by_descending_mmr['population']
rich_population
```

Again 202 is the row corresponding to the United States, with a population around 319 million.


Here (again) is the calculation of GDP per million in the population:

```{python}
gdp_per_million = rich_gdp / rich_population
gdp_per_million
```

The value for the United States is around 55 billion dollars per million of the population.

Finally, we sort this series to find that this is indeed the second highest value, and the United States is our outlier in the plot of rich countries against GDP per million:

```{python}
gdp_per_million.sort_values(ascending=False)
```
