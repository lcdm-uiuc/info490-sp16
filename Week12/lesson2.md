# Week 12 Lesson 2 #
## Introduction to MapReduce ##

In this lesson, you will learn about MapReduce. MapReduce is a
processing paradigm where a computing task is broken into a Map phase,
where a function is mapped onto data and a reduce phase, where the
results of the Map phase are aggregated. The Hadoop platform was
initially designed to facilitate bulk processing of text data, such as
computing unigrams. In this case, the Map phase would be to find
unigrams, while the reduce phase would be to count the number of
occurrences for each unigram. This is done by creating key-value pairs in
the map phase, such as a token and the number one; and in the reduce
phase summing up the one values for every adjacent, identical token. The
Hadoop platform, by default, sorts the output of the map phase and
aggregates them for the reducer task. 

###Objectives ###

By the end of this lesson, you will be able to:

- Understand the Map/Reduce paradigm
- Be familiar with the YARN resource scheduler
- Be able to use Hadoop Streaming to process a Python based map/reduce application

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to Map/Reduce][l2nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- HortonWorks tutorial on Yarn, [Introduction][tyi], [Part 1][typ1], and [Part 2][typ2]
- Basic Tutorial on the Map/Reduce, [Part 1][btmr1] and [Part II][btmr2]

## Optional Readings ##

- A lengthy (and slightly outdated) [tutorial on using Python][tphs] with Hadoop Streaming
- Official Apache Hadoop [MapReduce Tutorial][amrt]
- Official Apache Hadoop [Yarn Overview][ayo]

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 12 Lesson 2 Assessment][la]

[l2nb]: notebooks/intro2mr.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325362

[tphs]: http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

[btmr1]: http://www.tutorialspoint.com/map_reduce/map_reduce_introduction.htm
[btmr2]: http://www.tutorialspoint.com/map_reduce/map_reduce_algorithm.htm

[amrt]: http://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html
[ayo]: http://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html

[ty1]: http://hortonworks.com/blog/introducing-apache-hadoop-yarn/
[typ1]: http://hortonworks.com/blog/apache-hadoop-yarn-background-and-an-overview/
[typ2]: http://hortonworks.com/blog/apache-hadoop-yarn-concepts-and-applications/
