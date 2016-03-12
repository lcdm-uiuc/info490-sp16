# Week 9 Lesson 3 #
## Introduction to NLP: Semantic Analysis ##

In this lesson, you will be introduced to the concept of semantic
analysis, where we try to infer the meaning of text data. In part this
will build on the concepts of part of speech tagging and named entity
recognition presented in Lesson 1. Other concepts, however, are also
important, including the relative locations of words, and colocations.
To perform semantic analysius, we will develop the word vector space
model that underlies to the _word2vec_ appraoch. We will learn to employ
word2vec (and other related models) by using the _gensim_ Python
library. 
 
###Objectives ###

By the end of this lesson, you will be able to:

- Understand the basic concepts of semantic analysis
- Be familiar with the word2vec model
- Be able to apply semantic analysis within a Python application

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to NLP: Semantic Analysis][l3nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Wikipedia article on [word2vec][ww2v]
- Introduction to Word Vectors, [Part 1][ip1] and [Part 2][ip2], via Kaggle

## Optional Readings ##

- Wikipedia article on [Vector Space Models][wvsm]
- Wikipedia article on [Latent Semantic Analysis (LSA)[wlsa] 
- Wikipedia article on [Semantic Similarity][wss]
- Blog discussing the use of [semantic analysis for fashion][bwe] 
- Implementation of [word2vec in python][wip], via gensim.
- Blog article discussing the use of [word2vec for text analysis][wta].
- Original Google [word2vec][gw2v] implementation. 

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 9 Lesson 3 Assessment][la]

[l3nb]: notebooks/intro2nlp-sa.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325329

[bwe]: http://developers.lyst.com/2014/11/11/word-embeddings-for-fashion/

[ip1]: https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-2-word-vectors
[ip2]: https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-3-more-fun-with-word-vectors

[wvsm]: https://en.wikipedia.org/wiki/Vector_space_model
[ww2v]: https://en.wikipedia.org/wiki/Word2vec
[wlsa]: https://en.wikipedia.org/wiki/Latent_semantic_analysis
[wss]: https://en.wikipedia.org/wiki/Semantic_similarity

[gw2v]: https://code.google.com/archive/p/word2vec/
[wip]: http://radimrehurek.com/gensim/models/word2vec.html
[wta]: http://blog.dato.com/practical-text-analysis-using-deep-learning
