---
layout: single
title: Project
permalink: /project
---

# Project

## Teams

*   Teams of size 3 or 4.
*   See below for data rules.
*   When you have a team you're happy with, choose one member to email me
    (Matthew), with the information below.

I will consider smaller team sizes, and even team sizes of 1, but your email
should give convincing justification (see below).  In particular, you need to
convince me you have done the best you can to form a larger team.

## Team request

Email me (Matthew) with your request to form a team.

One team member should email, with a Cc to the other members.

Your email should have:

* a list of the team members;
* point to the data you are going to use.  You must point to some initial data.
  If the data is not public, give me some way to verify that it exists, and is
  suitable;
* sketch your plan for the initial analysis, and the final results that you
  hope for.

## Data

See [data for projects](projects/data)

## Workload

This term is 10 credits.  Each credit corresponds to 10 hours work, of which
one hour is the lecture.  Unlike other courses, there is no exam to revise for,
so the rest of the time is for the project.

You will find that, at the beginning of the project, this amount of work can
seem daunting.  Please don't worry; if you work steadily, you will find things
fall into place.  On the other hand, you must plan to work steadily.

This is a write-up of a previous data science course we ran: {% cite
millman2018rcsds %}.

In answer to "What advice would you give to another student who is considering taking this course?":

> Unlike most group projects (which last for maybe a few weeks
> tops or could conceivably be pulled off by one very dedicated
> person), this one will dominate the entire semester. . . . Try
> to stay organized for the project and create lots of little
> goals and checkpoints. You should always be working on something
> for the project, whether that's coding, reviewing, writing, etc.
> Ask lots of questions and ask them early!

## Getting help

We (your instructors) are very happy to help with advice on your project.  We
can't write any project code for you, but we will give you advice.  Please do
not wait to ask us; if you are stuck, we need to know as soon as possible.

## Scope

We only expect you to use the techniques that we have shown you in the
lectures.  You should not use any techniques that you do not understand.  We
would far prefer that you do simple, clear analyses using basic techniques than
complex analyses that you do not fully understand.  Your job as a data
scientist is to draw clear conclusions from data.  Often this will just involve
selecting and plotting relevant data, and making an argument from the results.

## Suggested structure

See the [rubric](projects/rubric) for the requirements of your project files.
This specifies that you must have a `README` file in some format, as the main
instructions to reproduce your analysis.

We also recommend that you:

* Download the data you are working on, and save it with your project files.
  Leave instructions on how we (your instructors) can get the original data
  that you downloaded.
* Consider using a `setup` file, such as a Notebook, that runs once, to set up
  the project.  For example, it might install any libraries that you will use.
  It may download the data from a URL and save it to your project directory.

## Process

In summary:

*   Analysis and collaboration will be public (using
    [CoCalc](https://cocalc.com/) or [Github](https://github.com) service).
*   Analysis should be reproducible.
*   Final report should be in the form of a Notebook, or similar
    executable document.

See: [project workflow](projects/workflow)

## Plagiarism

See: [plagiarism rules](projects/plagiarism)

## Using Python libraries

You can use any part of the Numpy, Pandas, and Matplotlib libraries with no
further explanation.

If you use other libraries, you should explain in your write-up why you are
using the library, rather than building the analysis yourself.  You must
persuade us, in your write-up, that you fully understand the parts of the
library that you are using.  If in doubt, speak to me (Matthew), or one of the
TAs.

## Marking

See [the full grading rubric](projects/rubric).

In summary:

*   Project marked for clarity, depth, validity and reproducibility (70% of
    project grade);
*   Each member of the project submits a summary of their own contribution,
    with evidence from the public record of collaboration (30% of project
    grade).

## Dates

These are provisional, except for the "Projects due" deadline.

| Week | Date       | Class                     |
| ---- | ---------- | ------------------------- |
| 1    | 13 Jan     | Start to form teams       |
| 2    | 20 Jan     | Data pitches 1            |
| 3    | 27 Jan     | Data pitches 2            |
| 4    |  3 Feb     | Teams finalized           |
| 8    |  2 Mar     | Progress reports          |
| 10   | 16 Mar     | Presentations             |
| 11   | 29 Mar     | Projects due              |

## Progress report

See: [progress report](projects/progress)

## Presentations

See: [project presentations](projects/presentation)

## Previous topics

In a previous version of this class, the data topics included:

* An analysis of UK and European public data on immigration to assess if the UK
  government was, [despite
  assurances](https://en.wikipedia.org/wiki/Windrush_scandal), continuing to
  deport residents from the West Indies who had settled in the UK legally
  before 1973.
* Looking for a link between UK school performance and local pollution data.
* Trying to relate Birmingham voting patterns to local levels of homelessness.
  Do people in areas with more homelessness tend to vote Conservative, Labour
  or Lib Dem?
* Global environmental and demographic factors associated with inflammatory
  bowel disease.
* An attempt to work out, with data, the algorithm that YouTube uses when
  recommending videos;
* Using historical data to predict the future National (American) Football
  League performance of a very successful college American football player.
* Predicting future stock prices using historical stock price data.
* Analyzing public NASA data to identify nearby habitable planets.
* Analysis of train timetable and departure / arrivals data for evidence of
  poor performance of particular train companies or lines.
