# Feature Creation Example
Arguably, feature engineering can account for a majority of time spent on any
machine learning pipeline and can be as important (if not more important) than 
the acutal modeling portion of predictive analytics. As evidence of this, let's look
at one of Sage Bionetworks newest challenges related to [Parkinson's Disease](https://www.synapse.org/#!Synapse:syn8717496/wiki/422884). From the project 
description: `In contrast to traditional DREAM challenges, this one will focus on feature extraction rather than predictive modeling`.

### Getting Started
As this step is part of this exercise, the file will only demonstrate how to access tools and not necessarily demonstrate
creating features on our data. Note that I'm including missing data in this step. Missing data can play a huge role in modeling.
Deciding how you will handle missing data is a crucial step in **training and implemenation**.

1. Check out other experiments. Viewing these boilerplate experiments, you can both get ideas for features as
well as see how they are implemented.
![experiment_sample](images/experiment_samples.png)
2. Consider grouping continuous variables (e.g. non-linear).
3. Consider combining variables (e.g. interactions)
4. Consider using models as a source of feature engineering.
5. Once you've developed a feature engineering pipeline, don't forget to click save!

