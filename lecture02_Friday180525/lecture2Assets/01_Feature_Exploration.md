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


