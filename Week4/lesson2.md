# Week 4 Lesson 2 #
## Ensemble Techniques: Bagging ##

In this lesson, you will learn about ensemble learning techniques that
employ bootstrap aggregation, or bagging. This approach leverages the
power of the crowd to make a more robust prediction. For example, when
estimating the number of marbles in a jar, studies have shown that the
average of a many different estimates is often very accurate. In machine
learning, we can combine the predictions from many weak learners to make
a more powerful learning algorithm. The weak learners can be trained on
only part of the data (e.g., only some features). These predictions can
then be combined via bagging to generate an improved estimate with
reduced variance. The most popular ensemble technique is the random
forest (RF) algorithm, which is available in the scikit learn library.


###Objectives ###

By the end of this lesson, you will be able to:

- Understand the basic concepts behind ensemble techniques and, in particular, bagging
- Understand the basic concepts behind the random forest algorithm
- Be able to apply RF by using the scikit learn library
- Understand how to use RF effectively for different types of learning problems.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Random Forest][l2nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Wikpedia article on [Bagging][wb]

- A short introduction to [Random Forests][frf]
- A lengthy presentation on [Random Forests in Python][yrfp]

- An [introduction to random forests][arf1] Part I
- An [introduction to random forests][arf2] Part II

## Optional Readings ##

- A Kaggle [discussion on random forests][krf]
- Scikit Learn [Ensemble Techniques: Bagging][seba] documentation
- An overview of [ensemble methods][ema].

- Original [Random Forest][orf] article.

- Sections 8.2.1 and 8.2.2 from [Introduction to Statistical Learning][isl]  by
Gareth James, Daniela Witten, Trevor Hastie and Robert Tibshirani
- Section 8.7 from [Elements of Statistical Learning][esl] by Trevor
Hastie, Robert Tibshirani, and Jerome Friedman. Note this text is rather
mathematical in nature.

_Safari Online Books_

- The Random Forest section in **Chapter 17: Decision Trees** from _Data Science from Scratch_, by Joel Grus.

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 4 Lesson 2 Assessment][la]

[l2nb]: notebooks/intro2rf.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325257

[seba]: http://scikit-learn.org/stable/modules/ensemble.html#bagging

[frf]: http://fastml.com/intro-to-random-forests/
[yrfp]: http://blog.yhat.com/posts/random-forests-in-python.html
[arf1]: http://www.analyticsvidhya.com/blog/2014/06/introduction-random-forest-simplified/
[arf2]: http://www.analyticsvidhya.com/blog/2015/09/random-forest-algorithm-multiple-challenges/
[krf]: https://www.kaggle.com/c/titanic/details/getting-started-with-random-forests

[wb]: https://en.wikipedia.org/wiki/Bootstrap_aggregating

[orf]: http://www.stat.berkeley.edu/~breiman/randomforest2001.pdf
[ema]: http://www.cs.ucl.ac.uk/fileadmin/UCL-CS/research/Research_Notes/RN_11_02.pdf

[isl]: http://www-bcf.usc.edu/~gareth/ISL/
[esl]: http://statweb.stanford.edu/~tibs/ElemStatLearn/
