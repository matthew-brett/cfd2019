'for_loops' exercise assumes conditionals, that we haven't covered.  The later
exercises are pretty hard.

Allow errors in notebook cell:

```{python tags=c("raises-exception")}
```

Pandas intro too long - move plotting into its own page.

Where, argmin page - 2D is confusing, move into own page.

Add gradient lines to optimization notebook.

Historical review of correlation / regression:

https://amstat.tandfonline.com/doi/full/10.1080/10691898.2001.11910537

Useful dataset for merge with gender_data:

* <https://humansurveys.org>
* <https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/QXZV3E>

```python
surveys = pd.read_stata('human_country_year_2018.dta')
surveys_2014 = surveys[surveys['id_200'] == 2014]
```
