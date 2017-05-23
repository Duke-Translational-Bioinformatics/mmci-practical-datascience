# Features
From within [Azure Machine Learning Studio](https://studio.azureml.net/
), we will explore the titanic data set. 

## What is a feature?
We can broadly bifurcate any dataset's variables (columns) into two concepts:

#### Independent Variables
From wikipedia page on `dependent and independent variables`:
>Depending on the context, an **independent variable** is sometimes 
called a "predictor variable", "regressor", "controlled variable",
"manipulated variable", "explanatory variable", 
"exposure variable" (see reliability theory), "risk factor" 
(see medical statistics), **"feature"** (in machine learning and pattern recognition) 
or "input variable."

#### Dependent Variables
> Depending on the context, a dependent variable is sometimes 
called a "response variable", "regressand", "predicted variable", 
"measured variable", "explained variable", "experimental variable",
"responding variable", "outcome variable", "output variable" or 
"label".

So a feature is an independent variable and is used to help associate or
predict a dependent variable or response. Beacause this is a machine learning course, 
we will use the term feature when we talk about independent variables.  

## The Chicken or The Egg
Before diving in, we will first need to **think about the problem we want to solve**. *Depending on the problem,
a particular variable could belong to either the independent variable list or the dependent variable list*. Much like 
`the chicken or the egg` delima, it depends on your perspective. Let's work
through this with an example.

Consider the [Framingham 10-year risk of Cardiovascular Disease](https://www.framinghamheartstudy.org/risk-functions/cardiovascular-disease/10-year-risk.php). This
machine learning algorithm promises to estimate the 10-year risk of Cardiovasular Disease. To do this it uses several
indepedent variables (features). Among them are an indication of diabetes (yes or no). In the context of this problem,
diabetes (yes or no) is a feature. However, in a recent [kaggle competition](https://www.kaggle.com/c/pf2012-diabetes),
this variable (i.e. diabetes yes/no) belonged to the dependent variable list. The purpose of that project was to 
predict diabetes (yes/no) so it belonged to the dependent variable list.


## Defining our problem
Using the titanic dataset, we'd like to predict **survival**. At this time,
go ahead and log into [Azure Machine Learning Studio](https://studio.azureml.net/
). Now that we have our problem well defined, we'll start exploring which features
to use so we can accomplish our goal. Starting with [01_Feature_Exploration.md](01_Feature_Exploration.md), we'll 
walk through this process.

