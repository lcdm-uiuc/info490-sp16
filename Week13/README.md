#Week 13 Overview#

## NoSQL DataStores ##

This week we introduce NoSQL Databases, which are generally recent
additions to the database world that provide functionality beyond that
provided by traditional relational databases, often to enable fast
processing of very large data sets. Typically these systems differ from
a relational database by violating a specific item in the relational
database _ACID_ test. Often this is consistency, which means that a
select query might return different results depending on when it is run.
This might be important for a shopping cart application for an online
retailer, for example, who might be more interested in fast responses to
user requests than an exact count of the number of items remaining in
the inventory. These types of databases can also be based on specific
types of data, such as document data or graph data structures. 

### Objectives ###

#####By the end of this lesson, you should be able to:######

- Understand the basic concepts of a NoSQL database.
- Understand the basics of documented-oriented, column-oriented, and
graph databases
- Understand how to connect to these database from a Python program.
- Be able to insert, update, select, and delete data from these database
by using a Python program.

### Activities and Assignments ###

|Activities and Assignments | Time Estimate | Deadline* | Points|
|:------| -----|-------|----------:|
|**[Week 13 Introduction Video][wv]** |10 Minutes|Tuesday|20|
|**[Week 13 Lesson 1: Introduction to Document Databases](lesson1.md)**| 2 Hours |Thursday| 20|
|**[Week 13 Lesson 2: Introduction to Column Databases](lesson2.md)**| 2 Hours | Thursday | 20 |
|**[Week 13 Lesson 3: Introduction to Graph Databases](lesson3.md)**| 2 Hours | Thursday| 20 |
|**[Week 13 Quiz][wq]**| 45 Minutes | Friday | 70|
|**Week 13 Assignment Submission**| 4 Hours | *The following* Monday | 80 Instructor, 40 Peer | 
|**Week 13 Completion of Peer Review**| 2 Hours | *The following* Saturday | 30 | 

*Please note that unless otherwise noted, the due time is 6pm Central time!*

----------
[wv]: https://mediaspace.illinois.edu/media/Week+Thirteen/1_59rokqo0/38493712
[wq]: https://learn.illinois.edu/mod/quiz/view.php?id=1325185
