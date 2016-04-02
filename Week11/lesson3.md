# Week 11 Lesson 3 #
## Introduction to General Linear Models ##

In this lesson, you will learn about general linear models. A general
linear model is a flexible approach to computing model fits to the
observed data where the model errors can be non-Gaussian. As was the
case with linear regression, the model terms can be non-linear, however,
they can't include combinations of different terms. For example, a
quadratic term is allowed, but we can't have x1 * x2. We will use the
pymc3 library to quickly and easily compute general linear models within
a Bayesian framework.

###Objectives ###

By the end of this lesson, you will be able to:

- Understand the basic concepts of general linear models.  
- Be familiar with the application of general linear models in a Bayesian framework.
- Be able to use the pymc3 library to compute general linear models.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to General Linear Models][l3nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Tutorial on Bayesian Modeling in Python, [Section 4][bmps4].
- PyMC3 [Robust Regression][pymc3rr] Example
- PyMC3 [Robust Regression with Outliers][pymc3rro] Example
- Wikipedia article on [General Linear Models][wglm]

## Optional Readings ##

- Applied AI blog on [Bayesian Inference with PyMC3][aibpymc3], Part 2.
- **[Chapter 3][bmh3]: Opening the Black Box of MCMC** from  _Bayesian Methods for Hackers_ by Cam Davidson-Pilon
- **[Chapter 4][bmh4]: The Greatest Theorem Never Told** from  _Bayesian Methods for Hackers_ by Cam Davidson-Pilon
- **[Chapter 5][bmh5]: Would you rather lose an arm or a leg?** from  _Bayesian Methods for Hackers_ by Cam Davidson-Pilon
- **[Chapter 6][bmh6]: Getting our priorities straight** from  _Bayesian Methods for Hackers_ by Cam Davidson-Pilon

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 11 Lesson 3 Assessment][la]

[l3nb]: notebooks/intro2pp-glm.ipynb

[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325353

[wglm]: https://en.wikipedia.org/wiki/Generalized_linear_model

[pymc3rr]: http://pymc-devs.github.io/pymc3/GLM-robust/
[pymc3rro]: http://pymc-devs.github.io/pymc3/GLM-robust-with-outlier-detection/

[bmh3]: http://nbviewer.ipython.org/urls/raw.github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/master/Chapter3_MCMC/Chapter3.ipynb
[bmh4]: http://nbviewer.ipython.org/urls/raw.github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/master/Chapter4_TheGreatestTheoremNeverTold/Chapter4.ipynb
[bmh5]: http://nbviewer.ipython.org/urls/raw.github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/master/Chapter5_LossFunctions/Chapter5.ipynb
[bmh6]: http://nbviewer.ipython.org/urls/raw.github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/master/Chapter6_Priorities/Chapter6.ipynb

[bmps4]: http://nbviewer.jupyter.org/github/markdregan/Bayesian-Modelling-in-Python/blob/master/Section%204.%20Bayesian%20regression.ipynb

[aibpymc3]: http://blog.applied.ai/bayesian-inference-with-pymc3-part-2/
