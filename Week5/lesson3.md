# Week 5 Lesson 3 #
## Unsupervised Learning: Density Estimation ##

In this lesson, you will learn about density estimation. Often, as part
of exploratory data analysis, a histogram is used to understand how data
are distributed, and in fact this technique can be used to compute a
probability mass function (or PMF) from a data set. However, the binning
approach has issues, including a dependance on the number and width of
the bins used to compute the histogram. One approach to overcome these
issues is to fit a function to the binned data, which is known as
parametric estimation. Alternatively, we can construct an approximation
to the data by employing a non-parametric density estimation. The most
commonly used non-parametric technique is kernel density estimation (or
KDE). In this lesson, you will learn about density estimation and
specifically how to employ KDE.

###Objectives ###

By the end of this lesson, you will be able to:

- Understand the basic concepts behind both parametric and non-parametric density estimation
- Understand the basic concepts behind kernel density estimation
- Be able to apply KDE by using the scikit learn library
- Understand how to use density estimation to approximate or smooth discrete data.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to Density Estimation][l2nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Introduction to [density estimation][gde]
- Using density estimation to [improve data visualization with Seaborn][skde]
- Density Estimation from [Silverman][sde], read through Section 2.5.

## Optional Readings ##

- Wikpedia article on [density estimation][wde]
- Wikpedia article on [kernel density estimation][wde]
- A comparison of different methods for [density estimation in Python][jde]

- Chapter 6 from [Elements of Statistical Learning][esl] by Trevor
Hastie, Robert Tibshirani, and Jerome Friedman. Note this text is rather
mathematical in nature.

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 5 Lesson 3 Assessment][la]

[l2nb]: notebooks/intro2de.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325281

[gde]: http://www.lancs.ac.uk/~struijke/density/index.html
[sde]: http://ned.ipac.caltech.edu/level5/March02/Silverman/Silver_contents.html
[jde]: https://jakevdp.github.io/blog/2013/12/01/kernel-density-estimation/

[skde]: http://stanford.edu/~mwaskom/software/seaborn/tutorial/distributions.html

[wde]: https://en.wikipedia.org/wiki/Density_estimation
[wkde]: https://en.wikipedia.org/wiki/Kernel_density_estimation

[esl]: http://statweb.stanford.edu/~tibs/ElemStatLearn/
