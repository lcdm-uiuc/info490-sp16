# Week 8 Lesson 2 #
## Introduction to Social Media: Twitter ##

In this lesson, you will be introduced to twitter data. Twitter is one
of the most popular social media data types due to the wealth of data,
the amount of metadata associate with each tweet, and the ease of
obtaining twitter data. To access twitter data, we will use a Python
library that wraps the official twitter application programming
interface (or API). First you will learn how to authenticate by using
OAUTH via the twitter API. Next, we will use the twitter API to find
specific tweets, analyze the tweet metadata, and to extract a set of
tweets. Finally, we will perform a sentiment analysis on twitter data to
classify tweets as positive or negative.

###Objectives ###

By the end of this lesson, you will be able to:

- Understand how to authenticate by using OAUTH 
- Understand the data and metadata contents of a tweet.
- Understand how to search for users and their tweets
- Be able to create an application that analyzes twitter data.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to Social Media: Twitter][l2nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Wikipedia article on [twitter][wt]
- Map of a [twitter status object][mtso]
- [Tweepy][twd]: Python Twitter client documentation (Getting Started and Authentication Tutorial).
- [Using nltk][unt] with twitter (note uses a different twitter client library)

## Optional Readings ##

- Wikipedia article on [Social Media][wsm]
- Twitter, [official documentation][tod]
- Blog demonstrating [twitter access via URLs][tu]
- Blog article on collecting tweets by using [streaming api][tsa]
- **Chapter 1: Mining Twitter** from _Mining the Social Web_, [IPython Notebook][msw1]
- **Chapter 9: Twitter Cookbook** from _Mining the Social Web_, [IPython Notebook][msw1]

_Safari Online Books_

- **Chapter 1: Mining Twitter** from _Mining the Social Web , 2nd Edition_, by Matthew A. Russell
- **Chapter 9: Twitter Cookbook** from _Mining the Social Web , 2nd Edition_, by Matthew A. Russell
- **Chapter 6: Social Media Insight Using Naive Bayes** from _Learning Data Mining with Python_, by Robert Layton


### Assessment ###

When you have completed and worked through the above readings, please take the [Week 8 Lesson 2 Assessment][la]

[l2nb]: notebooks/intro2smt.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325314

[wt]: https://en.wikipedia.org/wiki/Twitter
[wsm]: https://en.wikipedia.org/wiki/Social_media

[twd]: http://tweepy.readthedocs.org/en/
[tod]: https://dev.twitter.com/overview/documentation

[unt]: http://www.nltk.org/howto/twitter.html

[tsa]: http://badhessian.org/2012/10/collecting-real-time-twitter-data-with-the-streaming-api/
[tu]: http://nealcaren.web.unc.edu/pizza-twitter-and-apis/

[msw1]: https://github.com/ptwobrussell/Mining-the-Social-Web-2nd-Edition/blob/master/ipynb/Chapter%201%20-%20Mining%20Twitter.ipynb
[msw9]: https://github.com/ptwobrussell/Mining-the-Social-Web-2nd-Edition/blob/master/ipynb/Chapter%209%20-%20Twitter%20Cookbook.ipynb
[mtso]: http://online.wsj.com/public/resources/documents/TweetMetadata.pdf
