# Week 3 Lesson 3 #
## Supervised Learning: Naive Bayes ##

In this lesson, you will learn about a third simple supervised learning
technique known as Naive Bayes, or NB. Naive Bayes uses the probability
for each Attribute belonging to a particular class to make predictions.
The naive descriptor relates to the underlying assumption that these
probabilities are independent, which is generally not the case. However,
this assumption can often be used to easily obtain good results.

###Objectives ###

By the end of this lesson, you will be able to:

- Understand the basic concepts behind the Naive Bayes algorithm
- Be able to apply Naive Bayes by using the scikit learn library
- Understand the class of problems that are appropriate for the Naive Bayes algorithm.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Naive Bayes][l3nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- An introduction to [Naive Bayes][inb]
- An blog introduction to [Naive Bayes][bnb]

## Optional Readings ##

- Scikit Learn [NB][snb] documentation
- Discussion on [improving Naive Bayes][dinb]
- Discussion of [using NV][unb] for text processing.

- Section 6.3.3 from [Elements of Statistical Learning][esl] by Trevor
Hastie, Robert Tibshirani, and Jerome Friedman. Note this text is rather
mathematical in nature.

_Safari Online Books_

- **Chapter 13: Naive Bayes** from _Data Science from Scratch_, by Joel Grus.
- **Section 8.3 Bayes Classification Methods** from _Data Mining: Concepts
and Techniques_, 3rd Edition by Jiawei Han, Micheline Kamber, and Jian
Pei.

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 3 Lesson 3 Assessment][la]

[l3nb]: notebooks/intro2nb.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325248

[snb]: http://scikit-learn.org/stable/modules/naive_bayes.html
[unb]: http://blog.yhat.com/posts/naive-bayes-in-python.html
[bnb]: http://machinelearningmastery.com/naive-bayes-classifier-scratch-python/
[inb]: http://www.analyticsvidhya.com/blog/2015/09/naive-bayes-explained/
[dinb]: http://machinelearningmastery.com/better-naive-bayes/

[esl]: http://statweb.stanford.edu/~tibs/ElemStatLearn/
