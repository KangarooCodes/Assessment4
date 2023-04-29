### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
    PostgreSQL is a relational database management system. We use psql to issue database commands in the terminal.
    PostgreSQL is a ORM to utilize SQL along with JSON queries. SQL is one of the most common relational database languages.

- What is the difference between SQL and PostgreSQL?
    PostgreSQL is a free, open source product that supports the use of JSON

- In `psql`, how do you connect to a database?
    \c database_name

- What is the difference between `HAVING` and `WHERE`?
    `WHERE` must directly follow `FROM` and `HAVING` can follow `GROUP BY`

- What is the difference between an `INNER` and `OUTER` join?
    `INNER` join returns the data that matches both tables.
    `OUTER` join returns all of the data between both tables.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
    `LEFT OUTER` join returns all data in the left table, and matching data in the right table.
    `RIGHT OUTER` join returns all data in the right table, and matching data in the left table.

- What is an ORM? What do they do?
    Object-Relational Mapper. Converts data between a programming language, like Python, and a relational database.

- What are some differences between making HTTP requests using AJAX and from the server side using a library like `requests`?
    One is making requests from and executed by the browser with client IP address and the other is making requests from the server originated from the server IP address.

- What is CSRF? What is the purpose of the CSRF token?
   CSRF (Cross-Site Request Forgery) tokens are hidden, user-specific tokens to protect against fraud.

- What is the purpose of `form.hidden_tag()`?
    adds the CSRF token to the template.