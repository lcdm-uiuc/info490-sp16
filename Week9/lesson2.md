# Week 9 Lesson 2 #
## Introduction to NLP: Topic Modeling ##

In this lesson, you will be introduced to the concept of topic modeling.
Topic modeling is a form of unsupervised learning where specific topics,
or concepts are derived from documents. The dominant technique for
performing topic modeling is Latent Dirichlet Allocation or LDA. We
also will explore the application of Non-negative Matrix Factorization
(NMF) to the construction of topic models. To apply these techniques to
text data, we will use both the scikit learn and _gensim_ libraries.

###Objectives ###

By the end of this lesson, you will be able to:

- Understand the basic concept of topic modeling.
- Be familiar with the basic concepts of Latent Dirichlet Allocation.
- Be familiar with the basic concepts of Non-negative Matrix Factorization.
- Be able to apply LDA to derive topic models from text documents by using Python.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to NLP: Topic Modeling][l2nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Wikipedia article on [Topic Models][wtm] 
- Introduction to topic modeling, [part 1][[itm] and [part 2][itm-2]

## Optional Readings ##

- Blog article on [topic modeling][botm]
- Wikipedia article on [Latent Dirichlet Allocation (LDA)[wlda] 
- Wikipedia article on [Non-negative Matrix Factorization][wnmf] (focus on text-mining)
- Tutorial on using gensim for [topic modeling][gtm] 
- [Text Analysis with topic Models][tatm] for the Humanities and Social Sciences
- Blog article on [matrix factorization][bnmf], with application to NMF

_Safari Online Books_

- **Chapter 4: Topic Modeling** from _Building Machine Learning Systems
with Python (2nd Ed.)_ by Willi Richert and Luis Pedro Coelho

- The section on _Decomposing the feature matrices using non-negative
matrix factorization_ in **Chapter 4: Data Analysis-Deep Dive** from
_Python Data Science Cookbook_ by Gopi Subramanian

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 9 Lesson 2 Assessment][la]

[l2nb]: notebooks/intro2nlp-tm.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325326

[wlda]: https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation
[wtm]: https://en.wikipedia.org/wiki/Topic_model
[wnmf]: https://en.wikipedia.org/wiki/Non-negative_matrix_factorization

[itm]: http://journalofdigitalhumanities.org/2-1/topic-modeling-a-basic-introduction-by-megan-r-brett/
[itm-2]: http://journalofdigitalhumanities.org/2-1/topic-modeling-and-digital-humanities-by-david-m-blei/
[gtm]: http://radimrehurek.com/gensim/tut2.html
[tatm]: https://www.de.dariah.eu/tatom/index.html

[bnmf]: http://www.quuxlabs.com/blog/2010/09/matrix-factorization-a-simple-tutorial-and-implementation-in-python/

[botm]: https://www.oreilly.com/ideas/topic-models-past-present-and-future
