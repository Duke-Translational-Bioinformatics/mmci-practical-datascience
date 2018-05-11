# Lecture 4 Readings
___

### Papers Lecture 4 Assignment
```
Stevey's Google Platforms Rant I was at Amazon for about six and a half year...
https://plus.google.com/+RipRowan/posts/eVeouesvaVX.

Steve Yegge.

Stevey's Google Platforms Rant I was at Amazon for about six and a half years, and now I've been at Google for that long. One thing that struck me imme... - Rip Rowan - Google+
```
https://plus.google.com/+RipRowan/posts/eVeouesvaVX

```
A Conversation with Werner Vogels.
https://queue.acm.org/detail.cfm?id=1142065.

Werner Vogels and Jim Gray.

queue.acm.org.
```
https://queue.acm.org/detail.cfm?id=1142065

```
The Untapped Potential of Health Care APIs.

Robert S Huckman and Maya Uppaluru.

More data could benefit both patients and providers.

www.hbr.org, 2015.
```
https://hbr.org/2015/12/the-untapped-potential-of-health-care-apis
___
### Discussion Questions
1. What is a 'service'?
2. What are the advantages of such 'services'?
3. What are the disadvantages of 'services'?

___
### Case Study: Machine Learning in the Cloud
```
Systematic analysis of challenge-driven improvements in molecular prognostic models for breast cancer.

Adam A Margolin, Erhan Bilal, Erich Huang, Thea C Norman, Lars Ottestad, Brigham H Mecham, Ben Sauerwine, Michael R Kellen, Lara M Mangravite, Matthew D Furia, Hans Kristian Moen Vollan, Oscar M Rueda, Justin Guinney, Nicole A Deflaux, Bruce Hoff, Xavier Schildwachter, Hege G Russnes, Daehoon Park, Veronica O Vang, Tyler Pirtle, Lamia Youseff, Craig Citro, Christina Curtis, Vessela N Kristensen, Joseph Hellerstein, Stephen H Friend, Gustavo Stolovitzky, Samuel Aparicio, Carlos Caldas, and Anne-Lise Borresen-Dale.

Although molecular prognostics in breast cancer are among the most successful examples of translating genomic analysis to clinical applications, optimal approaches to breast cancer clinical risk prediction remain controversial. The Sage Bionetworks-DREAM Breast Cancer Prognosis Challenge (BCC) is a crowdsourced research study for breast cancer prognostic modeling using genome-scale data. The BCC provided a community of data analysts with a common platform for data access and blinded evaluation of model accuracy in predicting breast cancer survival on the basis of gene expression data, copy number data, and clinical covariates. This approach offered the opportunity to assess whether a crowdsourced community Challenge would generate models of breast cancer prognosis commensurate with or exceeding current best-in-class approaches. The BCC comprised multiple rounds of blinded evaluations on held-out portions of data on 1981 patients, resulting in more than 1400 models submitted as open source code. Participants then retrained their models on the full data set of 1981 samples and submitted up to five models for validation in a newly generated data set of 184 breast cancer patients. Analysis of the BCC results suggests that the best-performing modeling strategy outperformed previously reported methods in blinded evaluations; model performance was consistent across several independent evaluations; and aggregating community-developed models achieved performance on par with the best-performing individual models.

Sci Transl Med, 2013 vol. 5 (181) pp. 181re1-181re1.
```
http://stm.sciencemag.org/cgi/doi/10.1126/scitranslmed.3006112


```
Microservices.
https://martinfowler.com/articles/microservices.html.

Martin Fowler and James Lewis.

An in-depth description of the microservice style of architecture. Applications designed as suites of independently deployable services, governed in a decentralized manner.

martinfowler.com.
```
https://martinfowler.com/articles/microservices.html

___
### Discussion Questions
1. *Margolin, et. al* describes an Open Challenge for building predictive models for breast cancer, to host an arbitrary number of researchers or participants for contending with a data science problem, what are the things you need? What is a good way to think about each individual predictive model that was submitted for the Challenge—with this in mind, what is another way of thinking about how a participant could have "submitted" a predictive model (since we're talking about services)?
2. How does Martin Fowler define an "application". Going by this definition, if we think of the Breast Cancer Challenge being an application, how might it be broken down?
3. What are good examples of 'monolithic' applications?
4. Martin Fowler notes that "Remote calls are more expensive than in-process calls". What does he mean?
5. What is Conway's Law?
6. What implication does a Microservices Architecture have for a software team's responsibilities?
