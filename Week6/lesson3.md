# Week 6 Lesson 3 #
## Machine Learning: Practical Concepts ##

In this lesson, you will learn about several related practical concepts
that can improve the performance of a machine learning application.
First is feature scaling, which is used to change the distribution of
values for each feature in order to more effectively compare different
dimensions. Second is feature selection, which identifies the most
important features in a data set for a particular machine learning
approach. Third, is the concept of a pipeline where different components
in the machine learning process can be combined to run more efficiently.
Fourth is cross-validation, where multiple different train/test splits
are used to explore the efficacy of an algorithm to all of the data.
Fifth is the use of a grid search to identify optimal hyperparameters
for a machine learning algorithm,. Finally, we look at validation and
learning curves, which provide visual guidance on the effectiveness of a
particular algorithm and parameter values.

###Objectives ###

By the end of this lesson, you will be able to:

- Understand the basic concept of feature scaling and know when to use it.
- Understand how to build a machine learning pipeline in scikit learn. 
- Understand the basic techniques of feature selection
- Understand the cross-validation and how it can improve your machine learning results.
- Understand the validation and learning curves and how they can help improve machine learning results
- Understand how to use grid search to perform machine learning parameter estimation.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Practical Concepts][l2nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Wikipedia article on [Feature Scaling][wfs]
- Wikipedia article on [Feature Selection][wfse]
- Dato Blog post on [Validation and Testing][bvt]
- Dato Blog post on [Hyperparameter Testing][bht]

## Optional Readings ##

- Wikipedia article on [Cross-Validation][wcv]
- Documentation describing scikit learn [feature scaling][sksc]  
- Documentation describing scikit learn [feature selection][skfs]
- Documentation describing scikit learn [pipelines][skp]
- Documentation describing scikit learn [cross validation][skcv]
- Documentation describing scikit learn [grid search][skgs]  
- Documentation describing scikit learn [validation/learning curves][sklc]  

- Sections 5.1 from [Introduction to Statistical Learning][isl]  by
Gareth James, Daniela Witten, Trevor Hastie and Robert Tibshirani
- Section 7.10 from [Elements of Statistical Learning][esl] by Trevor
Hastie, Robert Tibshirani, and Jerome Friedman. Note this text is rather
mathematical in nature.

_Safari Online Books_

- **Chapter 5.  Overfitting and Its Avoidance** from _Data Science for
Business_ by Foster Provost and Tom Fawcett.
- **Chapter 8.  Visualizing Model Performance** from _Data Science for
Business_ by Foster Provost and Tom Fawcett.

 
### Assessment ###

When you have completed and worked through the above readings, please take the [Week 6 Lesson 3 Assessment][la]

[l2nb]: notebooks/intro2pc.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325293

[wfs]: https://en.wikipedia.org/wiki/Feature_scaling
[wfse]: https://en.wikipedia.org/wiki/Feature_selection
[wcv]: https://en.wikipedia.org/wiki/Cross-validation_(statistics)


[bvt]: http://blog.dato.com/how-to-evaluate-ml-models-part-3-validation-and-offline-testing
[bht]: http://blog.dato.com/how-to-evaluate-machine-learning-models-part-4-hyperparameter-tuning

[skfs]: http://scikit-learn.org/stable/modules/feature_selection.html
[skcv]: http://scikit-learn.org/stable/modules/cross_validation.html
[skgs]: http://scikit-learn.org/stable/modules/grid_search.html
[sksc]: http://scikit-learn.org/stable/modules/preprocessing.html#standardization-or-mean-removal-and-variance-scaling
[sklc]: http://scikit-learn.org/stable/modules/learning_curve.html
[skp]: http://scikit-learn.org/stable/modules/pipeline.html

[isl]: http://www-bcf.usc.edu/~gareth/ISL/
[esl]: http://statweb.stanford.edu/~tibs/ElemStatLearn/
