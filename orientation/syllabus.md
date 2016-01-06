# INFO 490: Advanced Data Science #

INFO 490: Advanced Data Science uses an project-based approach to
indoctrinate students into the tools and technologies necessary for
working with large data.

## Course Goals ##

Upon completion of this course, students will be expected to understand
advanced data science concepts. Students will learn the practical
aspects of applying machine and statistical learning in a variety of
contexts, as well as different aspects of cloud computing. Specific
concepts that will be covered including supervised and unsupervised
learning, dimensional reduction, clustering, probabilistic programming,
text mining, graph analysis, network analysis, Hadoop, NoSQL data
stores, Spark, and streaming data analysis.

## Prerequisites ##

As a pre-requisite for this course, you must have mastered the material
in *INFO 490: Foundations of Data Science*. Generally, this is
demonstrated by having taken this previous course. However, instructor
approval can also be granted for those who can demonstrate proficiency
in the required topics.

Note: At present, we are using the CS department's cluster to run a
course JupyterHub server. Each student is running a Dockerized version
of the course software stack. This provides many advantages including
robustness against crashes, simplicity of deploying software updates,
reduced requirements for students (simply a modern web browser, we have
used tablets and smart phones), and simplifying assignment submission.
You can also run a Docker container locally, as in previous courses, but
this approach is not recommended. In addition, if you work locally,
since assignments are automatically collected from your cloud-based
Docker container, you must ensure that you push local changes to your
course cloud Docker container prior to the deadline.

## Texts ##

There are no required textbooks for this course. Instead, we will
utilize Internet accessible websites, videos, and documentation as
supplemental material to the lesson content. We also will include links,
as relevant, to readings from books that are freely available to
University of Illinois students, staff and faculty via the University's
Safari subscription.

## Course Outline ##

| **Week** | **Topics**| **Assignments**|
|----------|-----------|----------------|
|*Orientation Week*| Course Overview & Syllabus Review| [Pre-Class Activity: Introduce Yourself](Pre-Class_Activity.md) <br /> [Github Registration and Introduction](notebooks/intro2github.ipynb)<br /> Orientation Quiz|
|*Week 1*| Introduction to Data Science| [Week 1 Lesson 1: Intro to Data Science](../Week1/lesson1.md) <br /> [Week 1 Lesson 2: Virtualization/Dockers](../Week1/lesson2.md)<br /> [Week 1 Lesson 3: JupyterHub/The Unix Shell](../Week1/lesson3.md) <br /> Week 1 Assignment <br/> Week 1 Quiz|
|*Week 2*| Introduction to Unix, Python, and iPython | [Week 2 Lesson 1: Basic Unix Concepts](../Week2/lesson1.md)<br /> [Week 2 Lesson 2: Intro to iPython](../Week2/lesson2.md)<br /> [Week 2 Lesson 3: Intro to Python](../Week2/lesson3.md)<br /> Week 2 Assignment<br /> Week 2 Quiz|
| *Week 3*| Introduction to the Python Programming Language| [Week 3 Lesson 1: Unix File System & Processes](../Week3/lesson1.md)<br /> [Week 3 Lesson 2: Python: Functions](../Week3/lesson2.md)<br /> [Week 3 Lesson 3: Python: Conditional Statements & Iteration](../Week3/lesson3.md)<br /> Week 3 Assignment<br /> Week 3 Quiz|
| *Week 4*| Advanced Python Programming Language|[Week 4 Lesson 1: Unix: Working with Data](../Week4/lesson1.md)<br /> [Week 4 Lesson 2: Python: Strings & Lists](../Week4/lesson2.md)<br /> [Week 4 Lesson 3: Python: Tuples & Dictionaries](../Week4/lesson3.md)<br /> Week 4 Assignment<br /> Week 4 Quiz|
|*Week 5*| Networking and File Input/Output|[Week 5 Lesson 1: Unix: Networking & Basic Commands](../Week5/lesson1.md)<br /> [Week 5 Lesson 2: Python: File I/O](../Week5/lesson2.md)<br /> [Week 5 Lesson 3: Python: Network Communication](../Week5/lesson3.md)<br /> Week 5 Assignment<br /> Week 5 Quiz |
|*Week 6*| Introduction to Regular Expressions|[Week 6 Lesson 1: Unix: Regular Expressions & Commands](../Week6/lesson1.md)<br /> [Week 6 Lesson 2: Python: Regular Expressions](../Week6/lesson2.md)<br /> [Week 6 Lesson 3: Regular Expressions](../Week6/lesson3.md)<br /> Week 6 Assignment<br /> Week 6 Quiz |
|*Week 7*| Introduction to Data Visualizations |[Week 7 Lesson 1: Introduction to Data Visualizations](../Week7/lesson1.md)<br /> [Week 7 Lesson 2: Python: Plotting](../Week7/lesson2.md)<br /> [Week 7 Lesson 3: Python: Data Plotting](../Week7/lesson3.md)<br /> Week 7 Assignment<br /> Week 7 Quiz |
|*Week 8*| Introduction to Numpy and Pandas|[Week 8 Lesson 1: Python: Introduction to Numpy](../Week8/lesson1.md)<br /> [Week 8 Lesson 2: Python: Introduction to Pandas](../Week8/lesson2.md)<br /> [Week 8 Lesson 3: Python: Pandas DataFrame](../Week8/lesson3.md)<br /> Week 8 Assignment<br /> Week 8 Quiz |
|*Week 9*| Introduction to Data Formats|[Week 9 Lesson 1: Data Format: Text](../Week9/lesson1.md)<br /> [Week 9 Lesson 2: Data Format: XML](../Week9/lesson2.md)<br /> [Week 9 Lesson 3: Data Format: JSON](../Week9/lesson3.md)<br /> Week 9 Assignment<br /> Week 9 Quiz |
|*Week 10*| Introduction to Statistics|[Week 10 Lesson 1: Statistics: Summary Measures](../Week10/lesson1.md)<br /> [Week 10 Lesson 2: Statistics: Distributions](../Week10/lesson2.md)<br /> [Week 10 Lesson 3: Statistics: Visualization](../Week10/lesson3.md)<br /> Week 10 Assignment<br /> Week 10 Quiz |
|*Week 11*| Functional Programming | [Week 11 Lesson 1: Functional Programming](../Week11/lesson1.md)<br /> [Week 11 Lesson 2: Python: Comprehensions](../Week11/lesson2.md)<br /> [Week 11 Lesson 3: Python: Functional Programming](../Week11/lesson3.md)<br /> Week 11 Assignment<br /> Week 11 Quiz |
|*Week 12*| Introduction to SQL and Relational Databases|[Week 12 Lesson 1: Relational Databases](../Week12/lesson1.md)<br /> [Week 12 Lesson 2: SQL: Schema Manipulation](../Week12/lesson2.md)<br /> [Week 12 Lesson 3: SQL: Data Manipulation](../Week12/lesson3.md)<br /> Week 12 Assignment<br /> Week 12 Quiz |
|*Week 13*| Introduction to OOP|[Week 13 Lesson 1: Object Oriented Programming](../Week13/lesson1.md)<br /> [Week 13 Lesson 2: Python: Introduction to OOP](../Week13/lesson2.md)<br /> [Week 13 Lesson 3: Python: OOP](../Week13/lesson3.md)<br /> Week 13 Assignment<br /> Week 13 Quiz |
|*Week 14*| Extracting Large Amounts of Data using Python|[Week 14 Lesson 1: Python: Database Programming](../Week14/lesson1.md)<br /> [Week 14 Lesson 2: Python: Web Scraping](../Week14/lesson2.md)<br /> [Week 14 Lesson 3: Python: Stream Processing](../Week14/lesson3.md)<br /> Week 14 Assignment<br /> Week 14 Quiz |
|*Week 15*| Introduction to Data Mining|[Week 15 Lesson 1: Python: Introduction to Data Mining(scikit learn)](../Week15/lesson1.md)<br /> Week 15 Assignment<br /> Week 15 Quiz |


## Weekly Format ##

Each week will provide learning objectives and an outline of the
activities for that week with a list of all deadlines and corresponding
point values for assignments.

### Videos ###

Each week there will be at least one instructor created video that will
offer a broader context for the new week, explain key concepts, and
demonstrate important tasks. To view the instructor videos, you will
need to login to the Illinois Mediaspace (links are embedded in the
relevant weekly overview, and as necessary in the appropriate lesson).
You will be given twenty points for viewing each weekly instructor
overview video, and ten points for viewing any instructor video that is
part of a weekly lesson. In case you are wondering, Illinois Mediaspace
tracks the viewing of course videos, so we know not only if you load a
video, but how much of the video you actually watched.

### Readings ###

Readings will consist of articles and excerpts from books and Web sites,
internet-accessible videos demonstrating a concept, and, in some cases,
IPython Notebooks that can be viewed statically on the Github website,
or (via the preferred approach) by interacting with them via the course
JupyterHub server. You will be required to read and be familiar with the
content of these documents. Readings are contextualized as part of the
weekly lesson content and are located in the "Readings" section of each
lesson.

### Lessons ###

Lessons will expand upon, or clarify key concepts in the reading
assignments or supplement or add to the reading. All lessons for a given
week must be completed by 6:00 PM Central on Thursday of that week.

### Lesson Assessments ###

Each week will contain three lesson modules (except for the last week,
which will contain only one). A lesson module will will include a Moodle
quiz designed to be taken after completing the readings and carefully
reviewing the lesson material. Lesson quizzes will allow two attempts,
to ensure students have mastered the relevant material before advancing
to the next lesson module. The lessons assessments must all be completed
by 6:00 PM Central on Thursday of that week.

### Assignments ###

Every week but the first and last will contain an assignment that will
involve one or more computational tasks related to the focus for that
given week. Your assignment will be automatically collected at the
deadline from the course server for instructor grading. However, you
must submit your assignment for peer grading by using the Moodle
Assignment tool. (Note we are exploring ways to do this within the
course server and may update this process during the course).

Each week you will be given instructions on how to complete the
assignment, as well as directions on exactly what you must submit to the
course Moodle site. Generally this will be in the form of an IPython
notebook. To receive full credit from instructor grading, your
assignment must be submitted prior to the deadline. There will be a
18-hour grace period, in which an assignment can be submitted, albeit
with an automatic 50% reduction in the maximum possible score. After
this grace period, no assignments will be accepted. The full credit
assignment deadline is 6:00 PM Central on the Monday following the
relevant week.

### Peer Review ###

Weekly assignments will be reviewed by your course peers, as well as
automatic instructor grading. 70 points (out of the maximum 150 points
for each assignment) for each weekly assignment submission
will derive from peer review, 80 points (out of the maximum 150 points
for each assignment) are assigned from automated instructor review. You will
receive 30 pts each week for simply viewing and grading your peers'
assignments. Note that you can (and should) still grade your peers even
if you miss an assignment submission. Peer review of an assignment must
be completed by 6:00 PM Central on Saturday of the following week (i.e.,
you submit your assignment on a Monday and you must peer assess other
students assignments by the following Saturday). You will be assigned
assignments to grade approximately one hour after the late assignment
deadline, thus around 1:00 pm Tuesday afternoon of each week.

| **Item** | **Grade** | 
|--|--| 
| Instructor Assessment | 80 points |  
| Peer Grading | 30 points | 
|Peer Assessments | 40 points| 

### Weekly Quizzes ###

In addition to the lesson quizzes, each week will conclude with a weekly
quiz. The weekly quiz is designed to test your overall mastery of the
content for each given week. Unlike the lesson quizzes, weekly quizzes
will be timed and will not allow multiple attempts. The quiz must be
completed by 6:00 PM Central on Friday of that week.

### Exams ###

This course is project-based in its use of assignments that build
progressively on content mastery, application, and peer review; there
are no exams in this course.

## Grading ##

### Grading Distribution ###
|Assignment | Points| Occurrences| Total Points |
|-----------|-----|-----|-----|
|Pre-Class Activity: Introduce Yourself| 60|1|60|
|Orientation Quiz|70|1|70|
|Lesson Assessments|60|14 (Week 15 is only 20 points)|860|
|Weekly Quizzes|70|14 (No quiz in Week 15)|980|
|Weekly Overview Videos|20|16 (including the Orientation Week video)|320|
|Assignments (Weeks 2-14)|150|13 |1950|
|***Total***|||***4240***|

Note that this total does not include any lesson videos, which will
increase the total points for that specific week, and the overall total.
Finally, unlike past courses, we do not plan on dropping any weekly scores.

### Grading Scale ###

Final grades will be graded on a curve, if necessary. The letter grade
cutoffs will be set at the traditional 90%, 80%, and 70% limits, and
plus/minus will be added if you are within two points of the traditional
cutoffs (so 100–98 is an A+ and 90–92 is an A-).

|Percentage|Letter Grade|
|--------|---------|
|98-100|A+|
|92-98|A|
|90-92|A-|
|88-90|B+|
|82-88|B|
|80-82|B-|
|78-80|C+|
|72-78|C|
|70-72|C-|
|68-70|D+|
|62-68|D|
|60-62|D-|
|Below 60|F|

### Point Reductions ###

This is a large, online course with only one instructor and one teaching
assistant. Thus we require that students read the syllabus and search
online forums before either emailing us directly or posting a new
question in the moodle forums. Failure to abide by this request may, at
the sole discretion of the instructor, result in a loss of five points
per **obvious** infraction. Please note that we are not trying to stifle
questions (such as why is the FAA server down?). We simply need to
minimize the number of such emails/questions we receive.

### Extra Credit ###

There is a course Wiki hosted on the course github repository. If you
have a problem and obtain a solution (either through your own efforts or
in partnership with an instructor), consider writing your problem and
solution up as a FAQ post in the github wiki. You get extra credit for
doing this and also help your classmates!

To get credit for your wiki entry you must contact the course assistant,
Samantha Thrush. She will review your post and indicate how many points
you will receive, and if she would be willing to review an edited post
for additional information. You can submit multiple Wiki entries.

## Sample Weekly Schedule ##

The following table summarizes the typical weekly schedule, where the
assignments are collected the Monday following the Friday when quizzes
are due.

| Task | Days into *Week* | Date/Time |
| ---  | ---  | ---     |
| Week Opens | 0 | Monday, 12:00 am |
| Lessons Completed | 3 | Thursday, 6:00 pm |
| Lesson Assessments |  3 | Thursday, 6:00 pm |
| Weekly Quiz  |  4 | Friday, 6:00 pm |
| Assignment Collected  | 7 |  Monday, 6:00 pm |
| Late Assignments Collected  | 8 |  Tuesday, 12:00 pm |
| Assignments uploaded for Peer Assessment  | 8 |  Tuesday, 12:00 pm |
| Assignments distributed for Peer Assessment  | 8 |  Tuesday, 1:00 pm |
| Peer Assessment Deadline  | 12 |  Saturday, 6:00 pm |