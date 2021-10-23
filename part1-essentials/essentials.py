
# set up Spark Session here

############################################################
# Dataframes basics
############################################################


############################################################
# Columns and expressions
############################################################

"""
    Exercises
    1. Read the movies DF and select 2 columns of your choice
    2. Create another column summing up the total profit of the movies = US_Gross + Worldwide_Gross + DVD sales
    3. Select all COMEDY movies with IMDB rating above 6

    Use as many versions as possible!
"""

############################################################
# Data sources and formats
############################################################

# JSON & flags
# CSV & flags
# JDBC (Postgres)

"""
    Exercise: read the movies DF, then write it as
      - tab-separated values file with header
      - Parquet
      - table "public.movies" in the Postgres DB
"""

############################################################
# Aggregations
############################################################

"""
    Exercises
    1. Sum up ALL the profits of ALL the movies in the DF
    2. Count how many distinct directors we have
    3. Show the mean and standard deviation of US gross revenue for the movies
    4. Compute the average IMDB rating and the average US gross revenue PER DIRECTOR
"""


############################################################
# Joins
############################################################

# join types (including some rare ones) & demos

"""
    Exercises
    1. show all employees and their max salary (all time)
    2. show all employees who were never managers
    3. for each employee, find the difference in their latest salary 
        between their own salary and the max salary of their job/department
"""

############################################################
# RDDs
############################################################

"""
    Exercises
    0. Read the movies file as an RDD.
    1. Select all the movies in the Drama genre with IMDB rating > 6.
    2. Show the average rating of movies by genre.
"""


if __name__ == '__main__':
    pass
