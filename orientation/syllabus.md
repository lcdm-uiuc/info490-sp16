# INFO 490: Foundations of Data Science #

INFO 490: Foundations of Data Science uses an project-based approach to
indoctrinate students into the tools and technologies necessary for
working with large data.

## Course Goals ##

Upon completion of this course, students will be expected to understand
the basic concepts of data science. Students will learn how to work at a
Unix prompt, how to use the Python programming language to process,
visualize, and persist large data sets, and how to use database
technologies including SQL.

## Prerequisites ##

There are no pre-requisites for this course, except for an interest in
learning the basic skills necessary for being a data scientist and
access to a computer to participate in the course lectures, and to
complete the required course assignments. 

Note: At present, students are required to use their own computer system
to perform many of the requirements for this course. We hope to
eventually enable at least soem students to use a cloud computing
approach to interacting with the course material. Until that time,
however, we recommend the following process to prepare your computer for
this course:

1. We have made a Docker image for this course (this is similar to what
we have done previously when we have taught this course). To use this
course image, you need to download and install Docker Machine. To use
Docker, which will provide a Unix shell with all of our required course
software for nearly all modern computing platforms, you should go to the
[Docker website](https://www.docker.com) and click the _Get Started with
Docker_ button. This will give you instructions for downloading and
installing Docker machine on your computer. Note that this will only
work for ‘fairly’ modern computers that support hardware virtualization.
On some computers, hardware virtualization must be enabled in your
computer BIOS. If you have questions about this process, including BIOS
changes, please consult the course assistants or instructor. Once the
course opens, you will have more details instructions on how to pull our
course Docker image, start the image to have a running container, and
how to download and install the course github repository in your running
Docker container.

2. If your computer is unable to support hardware virtualization, you
will (most likely) be unable to run Docker. Your options depend on the
type of computer you are using:

  2a. If you are running Mac OSX or Linux you can instead use a free
  Python package manager to install required software (more information
  will be forthcoming). You can download Anaconda, you *need* the
  version that supports Python 3.4, from [Continuum
  Analytics](http://continuum.io/downloads#py34). In this case, you will
  simply use a BASH shell on your computer to learn the Unix commands.
  If possible, however, you should still use Docker to (a) have an
  isolated environment where you can’t accidentally delete or change
  important system files and (b) learn about virtualization technologies.

  2b. If you have an older Windows laptop, you have several,
  unsatisfactory options. This is because Windows is not Unix. We can
  offer only limited support for these options since they are beyond the
  context of this course.

   - You can install and use Cygwin. It will create a Unix like
   environment, but there will be differences.

   - You could use (potentially free) cloud resources from Google,
   Amazon, Microsoft, Backspace, Cloudier, etc., to complete the course
   material.

Once you have downloaded Docker machine, you will need to pull our
course Docker image in order to have an effective working environment.
Instructions for doing this are included in [Lesson 2 for Week
1](../Week1/Lesson2.md) of the course (on virtualization and Dockers).
Once your have the course Docker container running, you will need to use
git to clone the course repository. At this point you will have a full
working course setup. You will also be instructed how to do this in
Lesson 2 of Week 1.

## Texts ##

There are no required textbooks for this course. Instead, we will
utilize internet accessible websites and documentation as supplemental
material to the lesson content.

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

Each week there will be at least one video that will offer a broader
context for the new week, explain key concepts, and demonstrate
important tasks. To view them, you will need to login to the Illinois
Mediaspace (links are embedded in the relevant weekly overview (and
occasionally a lesson). By viewing all videos for a week, you will be
given twenty points. In case you are wondering, Illinois Mediaspace tracks
the viewing of course videos.

### Readings ###

Readings will consist of articles and excerpts from books and Web sites,
and in some cases IPython Notebooks that can be viewed statically on the
Github website, or (via the preferred approach) by interacting with them
via the course JupyterHUb server. You will be required to read and be
familiar with the content of these documents. Readings are
contextualized as part of the weekly lesson content and are located in
the "Readings" section of each lesson.

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
given week. 

You will submit assignments by using the Moodle Assignment tool. Each
week you will be given instructions on how to complete the assignment,
as well as directions on exactly what you must submit to the course
Moodle site. This single submission will be used for the instructor
grading (which uses automatic grading scripts) and peer evaluation.
To receive full credit from instructor grading, your assignment must be
submitted prior to the deadline. There will be a 24-hour grace period,
in which an assignment can be submitted, albeit with an automatic 50%
reduction in the maximum possible score. After this grace period, no
assignments will be accepted. The full credit assignment deadline is
6:00 PM Central on Saturday of the relevant week.

### Peer Review ###

Weekly assignments will be reviewed by your course peers, as well as
automatic instructor grading. 40% of the grade for each weekly
assignment submission will derive from peer review, 60% from instructor
review. You will receive 50 pts each week for simply viewing and grading
your peers' assignments. Note that you can (and should) still grade your
peers even if you miss an assignment submission. Peer review of an
assignment must be completed by 6:00 PM Central on Tuesday of the
following week (i.e., you submit your assignment on a Saturday and then
must peer assess other students assignments by the following Tuesday).
You will be assigned assignments to grade approximately one hour after
the late assignment deadline, thus around 7:00 pm Sunday evening of each
week.

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

### Missed Weeks ###

While you are still strongly encouraged to complete all activities in
the course, we will drop your three lowest weekly grades from any week in the course.
<!--second to the fourteenth weeks. -->
Since later topics build on earlier topics,
however, it is in your best interest to still complete all readings,
even if after the relevant deadline.

### Grading Distribution ###
|Assignment | Points| Occurrences| Total Points |
|-----------|-----|-----|-----|
|Pre-Class Activity: Introduce Yourself| 60|1|60|
|Orientation Quiz|70|1|70|
|Lesson Assessments|60|14 (Week 15 is only 20 points)|860|
|Weekly Quizzes|70|14 (No quiz in Week 15)|980|
|Weekly Videos|20|16 (including the Orientation Week video)|320|
|Assignments (Weeks 2-14)|150|13 |1950|
|***Total***|||***4240***|

Note, after the lowest three weekly scores are dropped from weeks 2-14, 
the maximum total score for the class is **3340**.

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
