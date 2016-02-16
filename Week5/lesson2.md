# Week 5 Lesson 2 #
## Unsupervised Learning: Introduction to Clustering ##

In this lesson, you will learn about the Unsupervised Learning technique
of clustering. Cluster finding can be used to find groups or clusters
(the difference between these is generally the size of the identified
set of points, groups are smaller than clusters). Cluster finding is a
very popular machine learning technique since it can be used to find
related items in a much larger data set or to summarize data by focusing
on the identified clusters as opposed to the much larger data. In this
lesson, we focus on two simple, yet popular cluster detection
techniques: k-means and DBSCAN.   

###Objectives ###

By the end of this lesson, you will be able to:

- Understand the basic concepts behind clustering
- Understand the basic concepts behind the k-means and DBSCAN algorithms
- Be able to apply k-means and DBSCAN by using the scikit learn library

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to Clustering][l2nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Wikpedia article on [Clustering][wcl]
- A visual introduction to [k-means][vkm]
- A visual introduction to [DBSCAN][vdbs]
- A blog discussing [PCA and Clustering][bpc]

## Optional Readings ##

- Wikpedia article on [k-means][wkm]
- Wikpedia article on [DBSCAN][wdbs]
- An introduction to [k-means in Python][ikmp]
- Finding the [k in k-means in Python][fkkmp]
- A *very* gentle guide to [cluster detection with Python][vsgc].
- A sample chapter on [Clustering][bc-clust] from _Introduction to Data Mining_ by Tan, Steinbach, and Kumar

- Sections 10.3 from [Introduction to Statistical Learning][isl]  by
Gareth James, Daniela Witten, Trevor Hastie and Robert Tibshirani
- Section 14.3 from [Elements of Statistical Learning][esl] by Trevor
Hastie, Robert Tibshirani, and Jerome Friedman. Note this text is rather
mathematical in nature.

_Safari Online Books_

- **Chapter 19: Clustering** from _Data Science from Scratch_, by Joel Grus.
- **Chapter 15: Clustering** from _Python for Data Science For Dummies_, by John Paul Mueller and Luca Massaron.
- **Chapter 10: Cluster Analysis: Basic Concepts and Methods** from _Data Mining: Concepts
and Techniques_, 3rd Edition by Jiawei Han, Micheline Kamber, and Jian
Pei.
- The _Clustering_ section in **Chapter 6. Similarity, Neighbors, and Clusters** from _Data Science for Business_ by Foster Provost and Tom
Fawcett.

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 5 Lesson 2 Assessment][la]

[l2nb]: notebooks/intro2cluster.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325278

[vkm]: http://www.naftaliharris.com/blog/visualizing-k-means-clustering/
[vdbs]: http://www.naftaliharris.com/blog/visualizing-dbscan-clustering/

[bpc]: http://blog.yhat.com/posts/customer-segmentation-using-python.html

[vsgc]: http://guidetodatamining.com/assets/guideChapters/DataMining-ch8.pdf

[wcl]: https://en.wikipedia.org/wiki/Cluster_analysis
[wkm]: https://en.wikipedia.org/wiki/K-means_clustering
[wdbs]: https://en.wikipedia.org/wiki/DBSCAN

[ikmp]: https://datasciencelab.wordpress.com/2013/12/12/clustering-with-k-means-in-python/
[fkkmp]: https://datasciencelab.wordpress.com/2013/12/27/finding-the-k-in-k-means-clustering/

[bc-clust]: http://www-users.cs.umn.edu/~kumar/dmbook/ch8.pdf

[isl]: http://www-bcf.usc.edu/~gareth/ISL/
[esl]: http://statweb.stanford.edu/~tibs/ElemStatLearn/
