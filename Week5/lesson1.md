# Week 5 Lesson 1 #
## Unsupervised Learning: Introduction to Dimension Reduction ##

In this lesson, you will gain an introduction to Unsupervised Learning,
specifically via dimension reduction. Dimension reduction is used to
identify the statistically most important dimensions in a data set,
either for visualization (as we have been doing with the Iris data set)
or further processing. In some cases, dimension reduction can be used
for optimal feature selection. The most basic form of dimension
reduction is principal component analysis, or PCA. We can apply PCA to
a data set by using the scikit learn library.

###Objectives ###

By the end of this lesson, you will be able to:

- Understand the reasons for performing dimension reduction
- Understand the basic concepts of Principal Component Analysis (PCA)
- Be able to apply  PCA to a data set by using the scikit learn library
- Be aware of alternative dimension reduction techniques including
incremental PCA, sparse PCA, and non-negative matrix factorization.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [PCA][l1nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- A [simple introduction][spca] PCA
- A [three step guide][bpca] to PCA.

## Optional Readings ##

- A [gentle introduction][gipca], including the linear algebra required to understand PCA.

- A [detailed coverage][crpca] of dimensional reduction techniques.

- Sections 10.2 from [Introduction to Statistical Learning][isl]  by
Gareth James, Daniela Witten, Trevor Hastie and Robert Tibshirani
- Section 14.5 from [Elements of Statistical Learning][esl] by Trevor
Hastie, Robert Tibshirani, and Jerome Friedman. Note this text is rather
mathematical in nature.

_Safari Online Books_

- The _Dimensionality Reduction_ section in**Chapter 10: Working with Data** from _Data Science from Scratch_, by Joel Grus.
- The _Dimensionality reduction_ section in **Chapter 3: The Data Science Pipeline** from _Python Data Science Essentials_, by Luca Massaron and Alberto Boschetti
- **Chapter 14: Reducing Dimensionality** from _Python for Data Science For Dummies_, by John Paul Mueller and Luca Massaron.

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 5 Lesson 1 Assessment][la]

[l1nb]: notebooks/intro2dr.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325275

[bpca]: http://sebastianraschka.com/Articles/2014_pca_step_by_step.html
[spca]: http://www.lauradhamilton.com/introduction-to-principal-component-analysis-pca

[gipca]: http://www.cs.otago.ac.nz/cosc453/student_tutorials/principal_components.pdf
[crpca]: http://disp.ee.ntu.edu.tw/~pujols/Dimensionality%20Reduction.pdf

[isl]: http://www-bcf.usc.edu/~gareth/ISL/
[esl]: http://statweb.stanford.edu/~tibs/ElemStatLearn/
