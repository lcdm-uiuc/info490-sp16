# Week 12 Lesson 1 #

## Introduction to Hadoop ##

In this lesson, you will about Hadoop, which is a dominant platform for
big data processing. Hadoop is an open source Java project that enables
scalable, distributed computing. At its core, Hadoop moves the
computations to the data. To do this,  Hadoop utilizes a custom,
distributed file system known as HDFS. With HDFS, data is chunked into
blocks, and these blocks are distributed (with replication) across the
nodes in the Hadoop system. In this manner, processing can be scaled up to
large numbers of nodes, and not fail if a small number of nodes fail,
since the data are processed multiple times by different nodes. Since we
do not have sufficient compute resources, we will run a single-node
instance of Hadoop in this course, which will allow you to learn how to
use Hadoop, HDFS, MapReduce, and Pig, but not experience the speed and
power of a full Hadoop cluster.


###Objectives ###

By the end of this lesson, you will be able to:

- Understand the basic concepts of cloud computing
- Be familiar with Hadoop and HDFS
- Be able to use Hadoop to interact with HDFS

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to Hadoop][l1nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Learn about [cloud computing][acc] from AWS
- Learn about [types of cloud computing][acct] from AWS
- Learn about [Apache Hadoop][wah] via Wikipedia

## Optional Readings ##

- Wikipedia article on [Cloud Computing][wcc]
- [Tutorial on using Hadoop][th]
- Hadoop [Command Guide][hcg]
- Hadoop [File System Shell][hfss] command list
- HortonWorks [Tutorial on HDFS][hthdfs]

- **** from  

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 12 Lesson 1 Assessment][la]

[l1nb]: notebooks/intro2hadoop.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325359

[th]: http://www.tutorialspoint.com/hadoop/index.htm

[acc]: https://aws.amazon.com/what-is-cloud-computing/
[acct]: https://aws.amazon.com/types-of-cloud-computing/

[wcc]: https://en.wikipedia.org/wiki/Cloud_computing
[wah]: https://en.wikipedia.org/wiki/Apache_Hadoop

[hcg]: http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/CommandsManual.html
[hfss]: http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html

[hthdfs]: http://hortonworks.com/hadoop-tutorial/using-commandline-manage-files-hdfs/
