# Week 7 Lesson 1 #
## Introduction to Text Analysis ##

In this lesson, you will be introduced to basic concepts in text
analysis, starting with the conversion of a sequence of characters that
make up a text document into numerical data that can be computationally
processed. By parsing textual data into tokens, we can create a count of
word occurrences within a document, which when normalized by the total
number of words int he document, can provide word frequencies. The
collection of words in a document is more formally known as a _bag of
words_, and is a standard technique for text analysis. For multiple
documents, or subsections within a single document, we can turn this bag
of words into a matrix, where each row is a new document (or text item,
like a tweet, email, or web page) and each column is a count (or
frequency) of a specific word. Given the number of words, a _document
matrix_ can quickly become large, which introduces important computational
issues that must be addressed in text analysis.

###Objectives ###

By the end of this lesson, you will be able to:

- Understand the concepts of parsing a text document into a sequence of tokens, or words.
- Understand the bag of words model
- Understand the document matrix concept.
- Be able to create a bag of words from a text document by using Python.
- Be able to create a document matrix by using scikit learn.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to Text Analysis][l1nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Introduction to [Natural Language Processing][inlp]
- Wikipedia article on [Bag of Words][wbow] model
- Wikipedia article on [Document Term Matrix][wdtm]
- Gentle Introduction (in Python 2) to text analysis with Python, [part 1][nctap1] and [part 2][nctap2]

## Optional Readings ##

- NY Times [article on NLP][nytnlp]
- Wikipedia article on [Natural Language Processing][wnlp]
- Kaggle tutorial on [Bag of Words][kbow]
- Sections 2, 3, 5, and 6 from Chapter 1 of the free [NLTK version 3.0][nltk3] book

_Safari Online Books_

- **Chapter 1: Language Processing and Python** from _Natural Language Processing with Python_, by Steven Bird, Ewan Klein, and Edward Loper
- **Chapter 2: Accessing Text Corpora and Lexical Resources** from _Natural Language Processing with Python_, by Steven Bird, Ewan Klein, and Edward Loper
- **Chapter 3: Processing Raw Text** from _Natural Language Processing with Python_, by Steven Bird, Ewan Klein, and Edward Loper
- **Chapter 1: Tokenizing Text and WordNet Basics** from _Python 3 Text Processing with NLTK 3 Cookbook_, by Jacob Perkins


### Assessment ###

When you have completed and worked through the above readings, please take the [Week 7 Lesson 1 Assessment][la]

[l1nb]: notebooks/intro2ta.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325299

[inlp]: https://blog.monkeylearn.com/the-definitive-guide-to-natural-language-processing/

[wnlp]: https://en.wikipedia.org/wiki/Natural_language_processing
[wbow]: https://en.wikipedia.org/wiki/Bag-of-words_model
[wdtm]: https://en.wikipedia.org/wiki/Document-term_matrix


[nytnlp]: http://www.nytimes.com/2003/10/16/technology/circuits/16mine.html?pagewanted=print
[nltk3]: http://www.nltk.org/book/ch01.html

[nctap1]: http://nealcaren.web.unc.edu/an-introduction-to-text-analysis-with-python-part-1/
[nctap2]: http://nealcaren.web.unc.edu/an-introduction-to-text-analysis-with-python-part-2/

[kbow]: https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-1-for-beginners-bag-of-words
