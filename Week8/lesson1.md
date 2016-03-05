# Week 8 Lesson 1 #
## Introduction to Social Media: Email ##

In this lesson, you will be introduced to social media data, which are a
popular source of data for analytics projects. In particular, this
lesson focuses on email, which are a rich sort of data based on both
overall content as well as the social connections they imply. First, we
will review the basic components of an email message: header, body, and
(optional) footer. Next, we will discus how to parse an email message to
extract the body and possibly useful metadata. Finally, we will look at
applying text analytics to emails, specifically to  classify emails as
either spam or ham (i.e., bad or good messages).


###Objectives ###

By the end of this lesson, you will be able to:

- Understand the different components of an email.
- Understand the different components of an email header and the extra information they convey.
- Understand how to parse an email message to extract useful data.
- Be able to apply text analytics, like classification, to an email corpus.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to Social Media: Email][l1nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Wikipedia article on [email][we].
- Wikipedia article on [mbox][wmbox], file format for storing email messages.
- Recent blog article on [classifying email][bce] text documents.

## Optional Readings ##

- Wikipedia article on [smtp][wsmtp], protocol for sending and receiving emails.
- **Chapter 6: Mining Mailboxes** from _Mining the Social Web_, [IPython Notebook][msw6]
- [Configuring SMTP][cstmp] on Linux.
- Github repository for accessing [Hillary Clinton's][hrc] emails.
- Public [email repository for classification][sac].
- Public [Enron email][ene] repository.

_Safari Online Books_

- **Chapter 6: Mining Mailboxes** from _Mining the Social Web , 2nd Edition_, by Matthew A. Russell
- **Chapter 9: Authorship Attribution** from _Learning Data Mining with Python_, by Robert Layton

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 8 Lesson 1 Assessment][la]

[l1nb]: notebooks/intro2sme.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325311

[we]: https://en.wikipedia.org/wiki/Email
[wmbox]: https://en.wikipedia.org/wiki/Mbox
[wsmtp]: https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol

[hrc]: https://github.com/wsjdata/clinton-email-cruncher
[sac]: https://spamassassin.apache.org/publiccorpus/
[ene]: http://www.aueb.gr/users/ion/data/enron-spam/

[bce]: http://zacstewart.com/2015/04/28/document-classification-with-scikit-learn.html

[cstmp]: http://www.linuxhomenetworking.com/wiki/index.php/Quick_HOWTO_:_Ch21_:_Configuring_Linux_Mail_Servers#Configuring_Sendmail
[msw6]: https://github.com/ptwobrussell/Mining-the-Social-Web-2nd-Edition/blob/master/ipynb/Chapter%206%20-%20Mining%20Mailboxes.ipynb
