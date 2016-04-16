# Week 13 Lesson 2 #
## Introduction to Column-Oriented Databases ##

In this lesson, you will learn about column-oriented databases like
Cassandra. A column-oriented database is optimized to provide record data
in column-first format. This is important for large datasets, especially
when only a few columns may be required for a particular query.
Columns-ordered data enables specific columns ti be found quickly. To
connect to a Cassandra instance, we will use the Cassandra Python
database driver. This will allow us to execute CQL (Cassandra Query
Language) queries against the Cassandra instance in order to insert,
update, select, or delete records.

###Objectives ###

By the end of this lesson, you will be able to:

- Understand the basic concepts of a column-oriented database
- Be familiar with CQL
- Be able to use the Cassandra python database driver to insert, modify,
select, or delete data from a Cassandra database.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to Cassandra][l2nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Wikipedia article on [Column-Oriented Database][wcdb]
- Introduction to [Cassandra][ic]
- Getting Started with [Python and Cassandra][gsc]

## Optional Readings ##

- Overview of [Cassandra][oc]
- Wikipedia article on [Cassandra][wc]
- Try [Cassandra online][tco]
- (Older) Tutorial on using [Cassandra from IPython][c4ip]

_Safari Online Books_

- _Cassandra: The Definitive Guide_ by Eben Hewitt.
- _Cassandra High Performance Cookbook_ by Edward Capriolo
- _Cassandra Data Modeling and Analysis_ by C.Y. Kan

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 13 Lesson 2 Assessment][la]

[l2nb]: notebooks/intro2cassandra.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325374

[tco]: http://www.planetcassandra.org/try-cassandra/
[ic]: https://academy.datastax.com/resources/brief-introduction-apache-cassandra
[oc]: https://www.pythian.com/wp-content/uploads/2015/07/Pythian-Introduction-to-Cassandra-eBook-2015.pdf
[wc]: https://en.wikipedia.org/wiki/Apache_Cassandra
[wcdb]: https://en.wikipedia.org/wiki/Column-oriented_DBMS
[gsc]: https://datastax.github.io/python-driver/getting_started.html
[c4ip]: https://github.com/rustyrazorblade/python-presentation
