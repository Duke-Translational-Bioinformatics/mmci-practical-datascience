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
Is there any thoughts/questions that pop into your mind? If so, write them down. As we go though this exericise
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


