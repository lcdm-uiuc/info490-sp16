# Week 7 Lesson 3 #
## Introduction to Text Mining ##

In this lesson, we will be build on previous concepts to produce more
powerful text mining applications. First, we will introduce the concept
of stemming, where different forms of the same word are reduced to a
common form. This can improve text mining accuracy by altering the
frequency counts of different words or terms. Next, we will extend the
bag of words concept to include n-grams, which are groups of n-words.
The basic bag of words can be thought of as unigrams, or 1-grams. Higher
order groupings include bigrams and trigrams, where words are taken
as pairs or triples. n-grams can also improve the accuracy of text
mining applications by introducing higher order associations. Finally,
we will explore other machine learning concepts including dimension
reduction and clustering as applied to text data.
 
###Objectives ###

By the end of this lesson, you will be able to:

- Understand stemming and how it can affect text mining applications.
- Understand n-grams, and how to construct them from a document by using Python. 
- Be able to apply stemming and n-grams in a Python program by using scikit-learn and NLTK.
- Be able to perform dimensional reduction and clustering on text data by using scikit learn.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to Text Mining][l3nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Wikipedia article on [n-grams][wng]
- Wikipedia article on [Stemming][wst]
- Wikipedia article on [Lemmatisation][wl]
- Google [n-gram viewer][gnv]
- Alternative [n-gram viewer][anv]
- Wikipedia article on [Text Clustering][wtc]
- Blog on Sentiment Analysis with NLTK, [Part III][bsa3] and [Part IV][bsa4]

## Optional Readings ##


- An online [Stemming Demo][std] using NLTK
- A [treatise on Snowball][tsb] discussing, in depth, the process of stemming.
- A discourse on [Dimension Reduction][msdr]
- [Local Linear Embedding][lle], for dimensional reduction
- [Independent Component Analysis][ica] for text data

_Safari Online Books_

- **Chapter 10: Clustering News Articles** from _Learning Data Mining with Python_, by Robert Layton

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 7 Lesson 3 Assessment][la]

[l3nb]: notebooks/intro2tm.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325305

[wst]: https://en.wikipedia.org/wiki/Stemming
[wl]: https://en.wikipedia.org/wiki/Lemmatisation
[wtc]: https://en.wikipedia.org/wiki/Document_clustering

[tsb]: http://snowball.tartarus.org/texts/introduction.html
[std]: http://text-processing.com/demo/stem/

[wng]: https://en.wikipedia.org/wiki/N-gram

[gnv]: https://books.google.com/ngrams
[anv]: http://xkcd.culturomics.org

[bsa3]: http://streamhacker.com/2010/05/24/text-classification-sentiment-analysis-stopwords-collocations/
[bsa4]: http://streamhacker.com/2010/05/24/text-classification-sentiment-analysis-stopwords-collocations/

[msdr]: http://research.microsoft.com/pubs/150728/FnT_dimensionReduction.pdf
[lle]: http://science.sciencemag.org/content/290/5500/2323.abstract
[ica]: http://www.cs.rutgers.edu/~mlittman/topics/dimred02/kolenda99independent.pdf
