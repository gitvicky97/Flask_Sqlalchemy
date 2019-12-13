# Flask_Sqlalchemy


**SQLAlchemy** is an object-relational mapper (ORM), it allow us to interact with a database using Python functions and objects. For example, if we have a table called Cats we could retrieve every row with a command like Cats.query.all(). The main advantage of this is that it allows us to abstract away the SQL.

**Docker 🐳** allows us to quickly bring up a database within a Docker container, this means we don’t have to set up and configure a database on our local machine. We can simply kill the Docker container when we are done with the database. In this article, I will show you how you can create a very simple RESTful API using Flask and SQLAlchemy, which will connect to a database running in a Docker container.

**NOTE: Flask server will be running locally, not in a Docker container.

In this example, I will be using Postgres but it should be easy enough to use any other relational database, such as MySQL. I will also be using flask-sqlalchemy, which is a wrapper around SQLAlchemy, it simplifies our code and means we can use less boilerplate code.
