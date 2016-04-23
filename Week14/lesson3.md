# Week 14 Lesson 3 #
## Introduction to Spark Machine Learning ##

In this lesson, you will learn about Spark Machine Learning. Spark
machine learning encompasses two packages: Spark MLlib and Spark ML. THe
former operates on RDDs, while the latter, which is less well developed,
operates on DataFrames. In this lesson, we focus on MLlib, which
includes functionality for basic statistics functionality, as well as
classification, regression, clustering, and dimensional reduction. In this
lesson you will not only learn about the MLlib package, but specifically
how to use pySpark to use this functionality to generate models from
large data sets.


###Objectives ###

By the end of this lesson, you will be able to:

- Understand the basic contents of the Spark ML package
- Be familiar with basic statistical analysis by using the Spark ML package
- Be able to use pySpark to perform machine learning by using Spark.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to Pig][l3nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Spark [MLlib Basic Statistics][mbs]
- Spark [MLlib Classification and Regression][mcr]
- Spark [MLlib Clustering][mc]
- Spark [MLlib Feature Extraction and Transformation][mfet]

## Optional Readings ##

- Spark [MLlib Data Types][mdt]
- Blog discussing [topic modeling with Spark][stm]
- Blog demonstrating [Logistic Regression with Python and Spark][blrps]
- Blog post on [Customer Classification using Spark MLlib][bscc]

_Safari Online Books_

- **Chapters 2: Apache Spark MLlib** from _Mastering Apache Spark_, by Mike Frampton
- **Chapter 11: Machine Learning with MLlib:** from _Learning Spark_, by Holden Karau, 
Andy Konwinski, Patrick Wendell, Matei Zaharia.
- _Machine Learning with Spark_, by Nick Pentreath

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 14 Lesson 3 Assessment][la]

[l3nb]: notebooks/sparkmllib.ipynb

[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325389

[mcr]: https://spark.apache.org/docs/latest/mllib-classification-regression.html
[mc]: https://spark.apache.org/docs/latest/mllib-clustering.html
[mfet]: https://spark.apache.org/docs/latest/mllib-feature-extraction.html

[blrps]: https://www.codementor.io/spark/tutorial/spark-mllib-logistic-regression
[stm]: https://databricks.com/blog/2015/09/22/large-scale-topic-modeling-improvements-to-lda-on-spark.html
[bscc]: https://www.mapr.com/blog/classifying-customers-mllib-and-spark

[mdt]: https://spark.apache.org/docs/latest/mllib-data-types.html
[mbs]: https://spark.apache.org/docs/latest/mllib-statistics.html
