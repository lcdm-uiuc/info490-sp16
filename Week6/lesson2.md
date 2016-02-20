# Week 6 Lesson 2 #
## Machine Learning: Introduction to Anomaly Detection ##

In this lesson, you will be introduced to the concept of anomaly
detection. An anomaly is simple something that is unexpected or that
does not conform to an expected pattern. Anomaly detection is the search
for these events or observations in a (potentially) large data set.
Anomaly detection is important in many fields, and is used to identify
fraudulent transactions, imposters in social communities, errors in
textual data, issues in medical data (e.g., images), or intrusions in
network data. In some cases, we simple want to identify and remove
outliers to improve the accuracy of a model. In other cases, we are
actually interested in the outliers themselves. As a result, anomaly
detection is a rich field with a number of different approaches
available for use, including within the scikit learn library.

###Objectives ###

By the end of this lesson, you will be able to:

- Understand the basic concept of an anomaly.
- Understand the different types of anomalies, including outliers, novelties, or noise.
- Be able to apply scikit learn to detect anomalies.

### Time Estimate ###

Approximately 2 hours.

### Readings ####

_Course Notebook_

- Explore the course [Introduction to Anomaly Detection][l2nb]
IPython Notebook on the course JupyterHub server.

_Other Material_

- Wikipedia article on [Anomaly Detection][wad]
- An overview of statistical approaches to the [Detection of Outliers][doo] by NIST
- Through Section 1.2 of the [Anomaly Detection: A Survey][ads] (note you need to be on the campus network to access).

## Optional Readings ##

- Blog article from Sift Science on including [Decision Forests][df] in their fraud detection pipeline
- The full text of [Anomaly Detection: A Survey][ads] (note you need to be on the campus network to access).
- A recent book, **[Outlier Analysis][odb]** by Charu Aggarwal

_Safari Online Books_

- **Chapter 16: Detecting Outliers in Data** from _Python for Data Science For Dummies_, by John Paul Mueller and Luca Massaron.
- **Chapter 12: Outlier Detection** from _Data Mining: Concepts and Techniques_, 3rd Edition by Jiawei Han, Micheline Kamber, and Jian Pei.
- The _The detection and treatment of outliers_ section in **Chapter 3: The Data Science Pipeline** from _Python Data Science Essentials_, by Luca Massaron and Alberto Boschetti

### Assessment ###

When you have completed and worked through the above readings, please take the [Week 6 Lesson 2 Assessment][la]

[l2nb]: notebooks/intro2ad.ipynb
[la]: https://learn.illinois.edu/mod/quiz/view.php?id=1325290

[doo]: http://www.itl.nist.gov/div898/handbook/eda/section3/eda35h.htm

[ads]: http://dl.acm.org/ft_gateway.cfm?id=1541882&ftid=666427&dwn=1&CFID=753590370&CFTOKEN=66322093

[odb]: http://www.charuaggarwal.net/outlierbook.pdf

[df]: http://blog.siftscience.com/blog/2015/large-scale-decision-forests-lessons-learned
[wad]: https://en.wikipedia.org/wiki/Anomaly_detection
