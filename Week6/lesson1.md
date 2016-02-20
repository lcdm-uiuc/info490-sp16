# Week 6 Lesson 1 #
## Machine Learning: Introduction to Recommender Systems ##

In this lesson, you will be introduced to recommendation systems. Anyone
who has used Internet sites for shopping has been exposed to a
recommendation system. For example, when you shop at Amazon, you will be
given recommendations for items that are often bought together and also
items that are similar to the current item of interest. The former is an
example of user-based collaborative filtering, where the results from
other _similar users_ are summarized to make recommendations/ The latter
is an example of item-based collaborative filtering, where other
_similar items_ are summarized to make recommendations. Recommendation
systems are often easy to understand conceptually, since they can be
develop from simple association rules (i.e., A goes with B) and have been
frequently used with success by both traditional brick-n-mortar shops
and online sites.

###Objectives ###

By the end of this lesson, you will be able to:

- Understand the difference between user and item based recommendation
- Understand the basic concepts of the _a priori_ algorithm
- Understand the basic concepts of frequent itemsets, their construction, and their use in making recommendations.
- Be able to develop a simple recommendation algorithm. 

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Recommender System][l1nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- An IBM developerWorks article [introducing recommender systems][ibm-rs]
- Wikipedia article on [Recommender Systems][wrs]
- Wikipedia article on [A Priori Algorithm][wap]

## Optional Readings ##

- Wikipedia article on [Cosine Similarity][wcs]
- Machine Learning Review of [Recommender Systems][rrs]
- Python Blog on [Association Rules][bar] 
  
- **Chapter6: [Association Rules][bc-ar]** from _Introduction to Data Mining_ by Tan, Steinbach, and Kumar
- **Chapter 8: [Recommendation Systems][mmds-rs]** from _Mining Massive Datasets_ by Jure Leskovec, Anand Rajaraman, and Jeff Ullman

_Safari Online Books_

- **Chapter 22: Recommender Systems** from _Data Science from Scratch_, by Joel Grus.
- **Chapter 4: Recommending Movies Using Affinity Analysis** from _Learning Data Mining with Python_, by Robert Layton
- **Chapter 6: Mining Frequent Patterns, Associations, and Correlations** from _Data Mining: Concepts
and Techniques_, 3rd Edition by Jiawei Han, Micheline Kamber, and Jian
Pei.

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 6 Lesson 1 Assessment][la]

[l1nb]: notebooks/intro2rs.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325287

[wrs]: https://en.wikipedia.org/wiki/Recommender_system
[wap]: https://en.wikipedia.org/wiki/Apriori_algorithm
[wcs]: https://en.wikipedia.org/wiki/Cosine_similarity

[rrs]: http://www.prem-melville.com/publications/recommender-systems-eml2010.pdf

[bc-ar]: http://www-users.cs.umn.edu/~kumar/dmbook/ch6.pdf
[bar]: http://aimotion.blogspot.com/2013/01/machine-learning-and-data-mining.html

[ibm-rs]: http://www.ibm.com/developerworks/library/os-recommender1/index.html

[mmds-rs]: http://infolab.stanford.edu/~ullman/mmds/ch9.pdf
