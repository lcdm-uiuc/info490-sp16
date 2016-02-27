# Week 7 Lesson 2 #
## Introduction to Text Classification ##

In this lesson, you will be introduced to  classifying text documents,
including to perform sentiment analysis. To improve machine
classification of text documents, we will identify stop words and
demonstrate how they can be removed from the analysis by using NLTK.
Next, we will introduce the concept of frequency normalization, where we
normalize the frequency of token or word occurrences across multiple
documents. Formally, this is known as Term-Frequency, inverse document
frequency, or TD-IDF. Finally, we will explore how text classification
can be extended to perform sentiment analysis.

###Objectives ###

By the end of this lesson, you will be able to:

- Understand the basic concepts involved in text classification
- Understand stop words and how to remove them from a text analysis
- Understand TD-IDF and be able to employ it in a text classification implementation 
- Be able to apply text classification to perform sentiment analysis by using Python

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to Text Classification][l2nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Overview of text mining in the [digital humanities][tudh]
- Wikipedia article on [Text Mining][wtm]
- Gentle Introduction (in Python 2) to text analysis with Python, [part 3][nctap3]
- Blog on computing TF-IDF, [Part 1][btf1] and [Part II][btf2]
- Blog on Sentiment Analysis with NLTK, [Part 1][bsa1] and [Part II][bsa2]

**Part of speech?**

## Optional Readings ##

- Wikipedia article on [Stop Words][wsw]
- [Text classification][sktc] using scikit learn
- scikit learn documentation on [Text Feature Extraction][sktfe], sections 4.2.3.1 through 4.2.3.5
- Computing [Term Frequencies][ctf] in Python
- Sections 3, 4, and 5 from Chapter 6 of the free [NLTK version 3.0][nltk3-6] book

_Safari Online Books_

- **Chapter 6:  Learning to Classify Text** from _Natural Language Processing with Python_, by Steven Bird, Ewan Klein, and Edward Loper
- **Chapter 7: Text Classification** from _Python 3 Text Processing with NLTK 3 Cookbook_, by Jacob Perkins

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 7 Lesson 2 Assessment][la]

[l2nb]: notebooks/intro2tc.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325302

[tudh]: http://tedunderwood.com/2015/06/04/seven-ways-humanists-are-using-computers-to-understand-text/
[wtm]: https://en.wikipedia.org/wiki/Text_mining

[sktc]: http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
[sktfe]: http://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction

[btf1]: http://blog.christianperone.com/2011/09/machine-learning-text-feature-extraction-tf-idf-part-i/
[btf2]: http://blog.christianperone.com/2011/10/machine-learning-text-feature-extraction-tf-idf-part-ii/

[bsa1]: http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/
[bsa2]: http://streamhacker.com/2010/05/17/text-classification-sentiment-analysis-precision-recall/

[ctf]: http://marcobonzanini.com/2015/03/17/mining-twitter-data-with-python-part-3-term-frequencies/

[wsw]: https://en.wikipedia.org/wiki/Stop_words

[nctap3]: http://nealcaren.web.unc.edu/an-introduction-to-text-analysis-with-python-part-3/
[nltk3-6]: http://www.nltk.org/book/ch06.html
