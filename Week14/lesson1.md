# Week 14 Lesson 1 #

## Introduction to Spark ##

In this lesson, you will about Spark, a popular new approach to
processing big data. Spark provides an alternative to the Map-Reduce
approach for processing tasks on Hadoop. Spark was built around a
concept called Resilient Distributed Datasets (or RDDs). In this lesson,
we introduce Spark, demonstrate how to perform basic operations within
Spark, before introducing RDDs and how to perform basic data processing.
All Spark processing is done locally this week, but the basic concepts
all extend to larger Hadoop clusters, and the processing is done by
using Python via pySpark.

###Objectives ###

By the end of this lesson, you will be able to:

- Understand the basic concepts of Spark
- Be familiar with an RDD
- Be able to use pySpark to create Spark applications from within an IPython Notebook.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to Spark][l1nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Wikipedia on [Spark][ws]
- Tutorial Introduction to [Spark][tis], and [RDDs][tirdd]
- Spark [Homepage][sh]
- Spark [Quick Start Guide][qsg], be sure to select Python for the examples.

## Optional Readings ##

- An overview of [Apache Spark][oas]
- Spark [Programming Guide][spg], be sure to select Python for the examples.
- Workshop [Introducing Spark with IPython][iws]
- Blog article on [Python and Spark][bps]

_Safari Online Books_

- **Chapters 1: Apache Spark** from _Mastering Apache Spark_, by Mike Frampton
- **Chapters 1-6:** from _Learning Spark_, by Holden Karau, Andy Konwinski, 
Patrick Wendell, Matei Zaharia.

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 14 Lesson 1 Assessment][la]

[l1nb]: notebooks/intro2spark.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325383

[ws]: https://en.wikipedia.org/wiki/Apache_Spark

[tis]: http://www.tutorialspoint.com/spark_sql/spark_introduction.htm
[tirdd]: http://www.tutorialspoint.com/spark_sql/spark_rdd.htm


[sh]: http://spark.apache.org
[qsg]: https://spark.apache.org/docs/latest/quick-start.html
[spg]: https://spark.apache.org/docs/latest/programming-guide.html

[oas]: http://www.infoq.com/articles/apache-spark-introduction
[iws]: https://districtdatalabs.silvrback.com/getting-started-with-spark-in-python
[bps]: http://www.mccarroll.net/blog/pyspark2/index.html
