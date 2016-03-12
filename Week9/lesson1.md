# Week 9 Lesson 1 #
## Introduction to NLP: Basic Concepts ##

In this lesson, we will build on the lessons in Week 7 to learn several
basic concepts in natural language processing (NLP). First, we will
learn, in more detail, the concepts of tokenization, specifically beyond
just word level tokens, and how associations between tokens can be
important for NLP. We also will learn how to parse larger sections of
text such as a sentence or paragraph, including the removal of
punctuation. Next, we will learn about tagging text to identify the
different grammatical components such as a noun, verb, adjective, or
adverb. Finally, we will learn about entities and how to perform named
entity recognition. 

###Objectives ###

By the end of this lesson, you will be able to:

- Understand how to token text by paragraph, sentence, or word.
- Be familiar with the basic concepts of part of speech (POS) tagging
- Be familiar with the basic concepts of named entity recognition (NER)
- Be able to apply and use part of speech tagging and named entity
recognition in a Python application.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to NLP: Basic Concepts][l1nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Wikipedia article on [Part of Speech][wpos]
- Wikipedia article on [Named Entity Recognition][wner]
- [Online demo][dsp] of parsing text data

## Optional Readings ##

- Wikipedia article on [Treebanks][wtb]
- The [Penn Treebank][ptb] project
- Wikipedia article on [Garden Path Sentences][wgps]
- Sections 1, 2, and 4-7 from Chapter 5 of the free [NLTK version 3.0][nltk3-5] book
- Sections 5 and 6 from Chapter 7 of the free [NLTK version 3.0][nltk3-7] book
- [Spacy][sp], a new natural language processing library.
- Blog entry on using spacy to [mark adverbs][bma]
- Blog entry on [Named Entity Recognition][yner]

_Safari Online Books_

- **Chapter 4: Part-of-speech Tagging** from _Python 3 Text Processing with NLTK 3 Cookbook_, by Jacob Perkins
- **Chapter 3: Part of Speech Tagging** from _NLTK Essentials_, by Nitin Hardeniya

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 9 Lesson 1 Assessment][la]

[l1nb]: notebooks/intro2nlp-bc.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325323

[wner]: https://en.wikipedia.org/wiki/Named-entity_recognition
[wpos]: https://en.wikipedia.org/wiki/Part-of-speech_tagging
[wtb]: https://en.wikipedia.org/wiki/Treebank
[wgps]: https://en.wikipedia.org/wiki/Garden_path_sentence

[yner]: http://blog.yhat.com/posts/named-entities-in-law-and-order-using-nlp.html

[nltk3-5]: http://www.nltk.org/book/ch05.html
[nltk3-7]: http://www.nltk.org/book/ch07.html

[bma]: https://spacy.io/tutorials/mark-adverbs
[dsp]: https://api.spacy.io/displacy/index.html
[sp]: https://spacy.io
[ptb]: http://www.cis.upenn.edu/~treebank/
