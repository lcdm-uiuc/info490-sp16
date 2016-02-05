# Week 4 Lesson 3 #
## Ensemble Techniques: Boosting ##

In this lesson, you will learn about ensemble learning techniques that
employ boosting to combine many weak learners into a strong learner.
Boosting generally involves an iterative combination of new weak
leaners, possibly with weighting, into a stronger learner. This
iterative process can result in longer training times as optimizations
in combining new weak learners can become computationally more intensive
than some competing algorithms. However, the application of the
algorithm to make predictions is more responsive since the model has
already been constructed. Two of the most popular ensemble techniques
that employs boosting are the adaptive boosting (or Adaboost) algorithm
and the gradient boosted decision tree (GBT) algorithm, both of which are
available in the scikit learn library. 

###Objectives ###

By the end of this lesson, you will be able to:

- Understand the basic concepts behind ensemble techniques and, in particular, boosting
- Understand the basic concepts behind the adaptive boosting and gradient boosted tree algorithms
- Be able to apply Adaboost and GBT by using the scikit learn library
- Understand how to use these algorithms effectively for different types of learning problems.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Gradient Bosted Decision Tree][l2nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Wikpedia article on [Boosting][wb]
- A comparison between [Bagging and Boosting][cbb]
- A blog detailing how to use [Gradient Boosted Trees][bgbt] with a corresponding [Notebook][ngbt]

## Optional Readings ##

- Scikit Learn [Adaboost][sada] documentation
- Scikit Learn [Gradient Tree Boosting][sgbt] documentation

- Complete tutorial on [Gradient Boosting][tgbt].

- Sections 8.2.3 from [Introduction to Statistical Learning][isl]  by
Gareth James, Daniela Witten, Trevor Hastie and Robert Tibshirani
- Chapter 10 from [Elements of Statistical Learning][esl] by Trevor
Hastie, Robert Tibshirani, and Jerome Friedman. Note this text is rather
mathematical in nature.

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 4 Lesson 3 Assessment][la]

[l2nb]: notebooks/intro2gbt.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325260

[sada]: http://scikit-learn.org/stable/modules/ensemble.html#adaboost
[sgbt]: http://scikit-learn.org/stable/modules/ensemble.html#gradient-tree-boosting

[wb]: https://en.wikipedia.org/wiki/Boosting_(machine_learning)

[bgbt]: http://www.datarobot.com/blog/gradient-boosted-regression-trees/
[ngbt]: http://nbviewer.jupyter.org/urls/s3.amazonaws.com/datarobotblog/notebooks/gbm-tutorial.ipynb

[cbb]: http://fastml.com/what-is-better-gradient-boosted-trees-or-random-forest/

[tgbt]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3885826/

[isl]: http://www-bcf.usc.edu/~gareth/ISL/
[esl]: http://statweb.stanford.edu/~tibs/ElemStatLearn/
