# Week 11 Lesson 2 #
## Introduction to Hierarchical Modeling ##

In this lesson, you will learn about hierarchical modeling, in which a
Bayesian model is applied to an entire data set and individual data
subsets at the same time. This process, which is known as pooling,
enables the entire data to guide the model fitting for data subsets.
Ideally this improves the model fits to the individual data subsets.
Hierarchical modeling is important in many areas, including Bayesian A/B
testing.

###Objectives ###

By the end of this lesson, you will be able to:

- Understand the concept of hierarchical modeling. 
- Be familiar with the differences between pooled and unpooled model fits.
- Be able to use the pymc3 library to perform Bayesian Hierarchical Model fitting. 

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to Hierarchical Modeling][l2nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Tutorial on Bayesian Modeling in Python, [Section 3][bmps3]
- Blog article on [Bayesian A/B/ Testing][bbabt] (Note this was written for pymc2)
- Introduction to [Hierarchical Modeling with PyMC3][ihm]

## Optional Readings ##

- Wikipedia article on [Hierarchical Models][whm]
- [Blog post on [pitfalls in A/B Testing][bpabt]
- **[Chapter 2][bmh2]: A little more on PyMC** from  _Bayesian Methods for Hackers_ by Cam Davidson-Pilon

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 11 Lesson 2 Assessment][la]

[l2nb]: notebooks/intro2pp-hm.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325350

[whm]: https://en.wikipedia.org/wiki/Multilevel_model

[bmps3]: http://nbviewer.jupyter.org/github/markdregan/Bayesian-Modelling-in-Python/blob/master/Section%203.%20Hierarchical%20modelling.ipynb

[bbabt]: http://blog.dominodatalab.com/ab-testing-with-hierarchical-models-in-python/

[ihm]: http://pymc-devs.github.io/pymc3/GLM-hierarchical/

[bpabt]: http://chris-said.io/2016/02/28/four-pitfalls-of-hill-climbing/
[bmh2]: http://nbviewer.jupyter.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Chapter2_MorePyMC/Chapter2.ipynb
