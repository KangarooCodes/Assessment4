Make sure you download the starter code and run the following:

```sh
  psql < movies.sql
  psql movies_db
```

In markdown, you can place a code block inside of three backticks (```) followed by the syntax highlighting you want, for example

\```sql

SELECT \* FROM users;

\```

Using the `movies_db` database, write the correct SQL queries for each of these tasks:

1.  The title of every movie.

        SELECT title FROM movies;

2.  All information on the G-rated movies.

       SELECT * FROM movies WHERE rating='PG-13';
       

3.  The title and release year of every movie, ordered with the
    oldest movie first.

        SELECT title, release_year FROM movies ORDER BY release_year;
    
4.  All information on the 5 longest movies.

        SELECT * FROM movies ORDER BY runtime LIMIT 5;

5.  A query that returns the columns of `rating` and `total`, tabulating the
    total number of G, PG, PG-13, and R-rated movies.

        SELECT rating,COUNT(*) AS total FROM movies WHERE rating IN('G','PG','PG-13','R') GROUP BY rating;      

6.  A table with columns of `release_year` and `average_runtime`,
    tabulating the average runtime by year for every movie in the database. The data should be in reverse chronological order (i.e. the most recent year should be first).

        SELECT release_year, AVG(runtime) FROM movies GROUP BY release_year ORDER By release_year desc;

7.  The movie title and studio name for every movie in the database.

        SELECT title, name FROM movies Join studios on movies.studio_id=studios.id;

8.  The star first name, star last name, and movie title for every matching movie and star pair in the database.

        SELECT s.first_name, s.last_name, m.title FROM movies m JOIN roles r ON m.id=r.movie_id JOIN stars s ON r.star_id=s.id;

9.  The first and last names of every star who has been in a G-rated movie. The first and last name should appear only once for each star, even if they are in several G-rated movies. *IMPORTANT NOTE*: it's possible that there can be two *different* actors with the same name, so make sure your solution accounts for that.

        SELECT s.first_name, s.last_name
        FROM movies m
        JOIN roles r
        ON m.id=r.movie_id
        JOIN stars s
        ON r.star_id=s.id
        WHERE rating='G'
        GROUP BY s.first_name, s.last_name;

10. The first and last names of every star along with the number of movies they have been in, in descending order by the number of movies. (Similar to #9, make sure that two different actors with the same name are considered separately).

        SELECT s.first_name, s.last_name, Count(*) as number_of_movies
        FROM movies m
        JOIN roles r
        ON m.id=r.movie_id
        JOIN stars s
        ON r.star_id=s.id
        GROUP BY s.first_name, s.last_name
        ORDER BY Count(*) desc;


### The rest of these are bonuses

11. The title of every movie along with the number of stars in
    that movie, in descending order by the number of stars.

        SELECT m.title, Count(*) as stars_in_movie
        FROM movies m
        JOIN roles r
        ON m.id=r.movie_id
        JOIN stars s
        ON r.star_id=s.id
        GROUP BY m.title
        ORDER BY Count(*) desc;

12. The first name, last name, and average runtime of the five
    stars whose movies have the longest average.

        ( I added Rounding because I dislike so many decimal places)

        SELECT s.first_name, s.last_name, ROUND(AVG(runtime),2) as avg_runtime
        FROM movies m
        JOIN roles r
        ON m.id=r.movie_id
        JOIN stars s
        ON r.star_id=s.id
        GROUP BY s.first_name, s.last_name
        ORDER BY ROUND(AVG(runtime),2) desc
        LIMIT 5;

13. The first name, last name, and average runtime of the five stars whose movies have the longest average, among stars who have more than one movie in the database.

        SELECT s.first_name, s.last_name, ROUND(AVG(runtime),2) as avg_runtime, Count(*) as movie_count
        FROM movies m
        JOIN roles r
        ON m.id=r.movie_id
        JOIN stars s
        ON r.star_id=s.id
        GROUP BY s.first_name, s.last_name
        HAVING Count(*) >= 2
        ORDER BY ROUND(AVG(runtime),2) desc
        LIMIT 5;

14. The titles of all movies that don't feature any stars in our database.

        SELECT m.title
        FROM movies m
        LEFT JOIN roles r
        ON m.id=r.movie_id
        LEFT JOIN stars s
        ON r.star_id=s.id
        WHERE s.id is NULL
        GROUP BY m.title;

15. The first and last names of all stars that don't appear in any movies in our database.

        SELECT s.first_name, s.last_name
        FROM movies m
        RIGHT JOIN roles r
        ON m.id=r.movie_id
        RIGHT JOIN stars s
        ON r.star_id=s.id
        WHERE m.id is NULL
        GROUP BY s.first_name, s.last_name;


16. The first names, last names, and titles corresponding to every
    role in the database, along with every movie title that doesn't have a star, and the first and last names of every star not in a movie.
        
        SELECT s.first_name, s.last_name, m.title
        FROM movies m
        FULL JOIN roles r
        ON m.id=r.movie_id
        FULL JOIN stars s
        ON r.star_id=s.id
        GROUP BY s.first_name, s.last_name, m.title
        ORDER BY m.title desc;