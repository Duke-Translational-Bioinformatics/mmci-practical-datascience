# Getting on to Microsoft Azure's Machine Learning Lab
- Logging in
  - Navigate your browser to https://studio.azureml.net
  - You should be able to use your Duke account and enter via Duke's SSO
- We are going to start with the classic Titanic dataset
  - Located [here](https://gallery.cortanaintelligence.com/Experiment/Tutorial-Building-a-classification-model-in-Azure-ML-18)
  - Click the ```Open in Studio``` button on the right
  - You should now see something like this: ![AzureML Screenshot](https://github.com/Duke-Translational-Bioinformatics/mmci-practical-datascience/blob/master/lecture02_Friday180525/lecture2Assets/azureTitanicScreenshot.png)
- Exploring the data
  - The Data Dictionary for these data is [here](https://www.kaggle.com/c/titanic/data)
  - At the top of this flow diagram, click on the 1st block 'Titanic Dataset', right-click and select 'dataset' > 'visualize'
  - A window should now pop up showing the Titanic data in tabular form

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
predict a dependent variable or response. Because this is a machine learning course, 
we will use the term feature when we talk about independent variables.  

## The Chicken or The Egg
Before diving in, we will first need to **think about the problem we want to solve**. *Depending on the problem,
a particular variable could belong to either the independent variable list or the dependent variable list*. Much like 
`the chicken or the egg` dilemma, it depends on your perspective. Let's work
through this with an example.

Consider the [Framingham 10-year risk of Cardiovascular Disease](https://www.framinghamheartstudy.org/risk-functions/cardiovascular-disease/10-year-risk.php). This
machine learning algorithm promises to estimate the 10-year risk of Cardiovasular Disease. To do this it uses several
indepedent variables (features). Among them are an indication of diabetes (yes or no). In the context of this problem,
diabetes (yes or no) is a feature. However, in a recent [kaggle competition](https://www.kaggle.com/c/pf2012-diabetes),
this variable (i.e. diabetes yes/no) belonged to the dependent variable list. The purpose of that project was to 
predict diabetes (yes/no) so it belonged to the dependent variable list.


## Defining our problem
Using the Titanic dataset, we'd like to predict **survival**. At this time,
go ahead and log into [Azure Machine Learning Studio](https://studio.azureml.net/
). Now that we have our problem well defined, we'll start exploring which features
to use so we can accomplish our goal. Starting with [01_Feature_Exploration.md](01_Feature_Exploration.md), we'll 
walk through this process.

# Feature Exploration
Once logged into AMLS (Azure Machine Learning Studio), go to **Experiments**. There should be 
a default experiment provided titled `Tutorial: Building a classification model...`. Click on 
the title of that experiment. If all goes well, you will be presented with a 
machine learning pipeline already created for you.

#### Visualize
> The purpose of visualization is insight, not pictures.
-Ben Shneiderman

At the top of the pipeline, the first node is titled `Titanic Dataset`, this is where
the data is loaded for processing. Remeber our goal is to explore features (independent variables) that 
will help us accomplish our goal of predicting survial. Now is the time to be curious! Here are a couple
of questions/thoughts that poped into my mind when I first looked at this pipeline:

    - How many people are in this data set
    - How many variables (both dependent and independent) are available?
    - Is survival one of those variable? Or, will I need to construct it?
    - I hope age is available, that (naively) seems like a potentially important feature.  
Are there any thoughts/questions that pop into your mind? If so, write them down. As we go though this exercise
you should be introduced to the tools needed to help you answer questions related to feature exploration.
 
Thankfully, many of the nodes available in AMLS offer a visualize attribute that is accessible
through right-clicking on the node. In the first node `Titanic Dataset`, right click and then select 
`dataset > Visualize`. You should be presented with a modal that helps provide insights to the dataset.
You can even click on a particular variable and additional information will be displayed. For instance, try 
clicking on `age`. You should be presented summary statistics and a histogram.

Interestingly, all of the previously stated questions can be answered with this one tool. See if you can answer these
questions now. How about any additional questions / comments? Are you able to answer them with this tool? 


#### Variable Selection
> Variable selection in regression – identifying the best subset among many variables to include in a model – is arguably the hardest part of model building.  
-Bruce Ratner

Some datasets can contain thousands or even tens of thousands of possible features. Many of these features have the potential 
to be correlated with other features leading to a phenomenon known as `multicollinearity`. In some machine learning 
tools (e.g. regression) this can cause problems. Also, we need to think about the tool we are building. Are we building
a prediction model to be used `in the field` where computers may not be availble? If so finding the most parsimonious features
is important. There are sophisicated techniques to do this, but for now, we'll use our intutition to select a subset of
variables for our feature set.

Left-click the second node **Select Columns in Dataset**. Notice the `Properties` pane on the right. If we click on the 
launch column selector, a modal tool will appear which will allow us to either `include` or `exclude` features.
In this pipeline, the variables `PassengerId`, `Name`, `Cabin`, and `Ticket` are removed
from the pipeline (meaning they will not be part of the model). Intuitively, does this make sense? Go back to the first
node and visualize the variables. Do you think they hold information related to predicting `survial`. Are there other
variables that you would have removed? There is no wrong or right answer.

#### Variable Metadata
>Metadata liberates us, liberates knowledge
-David Weinberger  

By default, many machine learning algorithms look to metadata to determine how to "treat" variables. For instance, in 
the titanic dataset age was read in as a numeric feature. Sex, on the other hand, was read in (and understood) as a 
string feature. What about the variable Pclass? It seems this variable was read in as a numeric feature, but does this make
sense? A general `rule of thumb` is that mathematical operations should make sense on numeric features. Therfore, if we 
were to add 1 to an age of 37 (resulting in 38) - does that make sense? Yes. Let's try that with Pclass. If we add 1 to 
3 (resulting in 4) - does that make sense? Well, we probably need more information. Pclass stands for Passenger Class and
if you're up on your titanic history, you know that there were only 3 classes of passengers on the titanic, so 4 does not
make any sense. Therefore Pclass (or passenger class) should not be treated as a numeric feature. All of this higher level
information about our data is known as `metadata`. The better we understand and represent the metadata, the
better we can model quantities of interest. Therefore, we need to somehow change the metadata about Pclass and other similar
features. To do this, note the 3rd node titled `Edit Metadata`. This node represents changing the metadata of serveral variables
so that the names of the variables are more easily understood and the variable types represent how we want the machine to 
understand their values.
