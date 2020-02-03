# Remainder of lab03 exercise

I was working through the lab03 exercise, and didn't get to the latter part of
the exercise (further below).

I needed a tutorial on `logical_and` etc, now in `notebooks/08/combining_booleans`.

## Remainder of exercise

**Question 5.6.** Here's a challenge: Find the number of movies that came out in *even* years.

*Hint:* The operator `%` computes the remainder when dividing by a number.  So `5 % 2` is 1 and `6 % 2` is 0.  A number is even if the remainder is 0 when you divide by 2.

*Hint 2:* `%` can be used on arrays, operating elementwise like `+` or `*`.  So `make_array(5, 6, 7) % 2` is `array([1, 0, 1])`.

*Hint 3:* Create a column called "Year Remainder" that's the remainder when each movie's release year is divided by 2.  Make a copy of `imdb` that includes that column.  Then use `where` to find rows where that new column is equal to 0.  Then use `num_rows` to count the number of such rows.

```{python for_assignment_type=student}
num_even_year_movies = ...
num_even_year_movies
```

```{python}
_ = ok.grade('q5_6')
```

**Question 5.7.** Check out the `population` table from the introduction to this lab.  Compute the year when the world population first went above 6 billion.

```{python}
year_population_crossed_6_billion = ...
year_population_crossed_6_billion
```

```{python}
_ = ok.grade('q5_7')
```

## Miscellanea
There are a few more table methods you'll need to fill out your toolbox.  The first 3 have to do with manipulating the columns in a table.

The table `farmers_markets.csv` contains data on farmers' markets in the United States  (data collected [by the USDA]([dataset](https://apps.ams.usda.gov/FarmersMarketsExport/ExcelExport.aspx)).  Each row represents one such market.

**Question 6.1.** Load the dataset into a table.  Call it `farmers_markets`.

```{python}
farmers_markets = ...
farmers_markets
```

```{python}
_ = ok.grade('q6_1')
```

You'll notice that it has a large number of columns in it!

### `num_columns`

**Question 6.2.** The table property `num_columns` (example call: `tbl.num_columns`) produces the number of columns in a table.  Use it to find the number of columns in our farmers' markets dataset.

```{python}
num_farmers_markets_columns = ...
print("The table has", num_farmers_markets_columns, "columns in it!")
```

```{python}
_ = ok.grade('q6_2')
```

Most of the columns are about particular products -- whether the market sells tofu, pet food, etc.  If we're not interested in that stuff, it just makes the table difficult to read.  This comes up more than you might think.

### `select`

In such situations, we can use the table method `select` to pare down the columns of a table.  It takes any number of arguments.  Each should be the name or index of a column in the table.  It returns a new table with only those columns in it.

For example, the value of `imdb.select("Year", "Decade")` is a table with only the years and decades of each movie in `imdb`.

**Question 6.3.** Use `select` to create a table with only the name, city, state, latitude ('y'), and longitude ('x') of each market.  Call that new table `farmers_markets_locations`.

```{python}
farmers_markets_locations = ...
farmers_markets_locations
```

```{python}
_ = ok.grade('q6_3')
```

### `select` is not `column`!

The method `select` is **definitely not** the same as the method `column`.

`farmers_markets.column('y')` is an *array* of the latitudes of all the markets.  `farmers_markets.select('y')` is a table that happens to contain only 1 column, the latitudes of all the markets.

**Question 6.4.** Below, we tried using the function `np.average` to find the average latitude ('y') and average longitude ('x') of the farmers' markets in the table, but we screwed something up.  Run the cell to see the (somewhat inscrutable) error message that results from calling `np.average` on a table.  Then, fix our code.

```{python for_assignment_type=student}
average_latitude = np.average(farmers_markets.select('y'))
average_longitude = np.average(farmers_markets.select('x'))
print("The average of US farmers' markets' coordinates is located at (", average_latitude, ",", average_longitude, ")")
```

```{python}
_ = ok.grade('q6_4')
```

### `drop`

`drop` serves the same purpose as `select`, but it takes away the columns you list instead of the ones you don't list, leaving all the rest of the columns.

**Question 6.5.** Suppose you just didn't want the "FMID" or "updateTime" columns in `farmers_markets`.  Create a table that's a copy of `farmers_markets` but doesn't include those columns.  Call that table `farmers_markets_without_fmid`.

```{python}
farmers_markets_without_fmid = ...
farmers_markets_without_fmid
```

```{python}
_ = ok.grade('q6_5')
```

#### `take`
Let's find the 5 northernmost farmers' markets in the US.  You already know how to sort by latitude ('y'), but we haven't seen how to get the first 5 rows of a table.  That's what `take` is for.

The table method `take` takes as its argument an array of numbers.  Each number should be the index of a row in the table.  It returns a new table with only those rows.

Most often you'll want to use `take` in conjunction with `np.arange` to take the first few rows of a table.

**Question 6.6.** Make a table of the 5 northernmost farmers' markets in `farmers_markets_locations`.  Call it `northern_markets`.  (It should include the same columns as `farmers_markets_locations`.

```{python}
northern_markets = ...
northern_markets
```

```{python}
_ = ok.grade('q6_6')
```

**Question 6.7.** Make a table of the farmers' markets in Berkeley, California.  (It should include the same columns as `farmers_markets_locations`.)

```{python}
berkeley_markets = ...
berkeley_markets
```

```{python}
_ = ok.grade('q6_7')
```

Recognize any of them?


## Summary

For your reference, here's a table of all the functions and methods we saw in this lab.

|Name|Example|Purpose|
|-|-|-|
|`Table`|`Table()`|Create an empty table, usually to extend with data|
|`Table.read_table`|`Table.read_table("my_data.csv")`|Create a table from a data file|
|`with_columns`|`tbl = Table().with_columns("N", np.arange(5), "2*N", np.arange(0, 10, 2))`|Create a copy of a table with more columns|
|`column`|`tbl.column("N")`|Create an array containing the elements of a column|
|`sort`|`tbl.sort("N")`|Create a copy of a table sorted by the values in a column|
|`where`|`tbl.where("N", are.above(2))`|Create a copy of a table with only the rows that match some *predicate*|
|`num_rows`|`tbl.num_rows`|Compute the number of rows in a table|
|`num_columns`|`tbl.num_columns`|Compute the number of columns in a table|
|`select`|`tbl.select("N")`|Create a copy of a table with only some of the columns|
|`drop`|`tbl.drop("2*N")`|Create a copy of a table without some of the columns|
|`take`|`tbl.take(np.arange(0, 6, 2))`|Create a copy of the table with only the rows whose indices are in the given array|

<br/>
