# Diploma-Thesis

Here is hosted the source code of the thesis "Study of Causal Machine Learning Techniques on Data from IoT Applications" https://hdl.handle.net/10889/25228. For writing the thesis, the IDEAL Household Energy Dataset was used https://doi.org/10.7488/ds/2836.

The rapid increase in computing power and the ability to store Big Data in the infrastructure has given
humanity the opportunity to model a large portion of its everyday problems using Artificial
Intelligence technology and especially the subsector of Machine Learning, with the dominant goal of
predicting future events. However, in many cases, solving the question with existing Machine
Learning tools is considered insufficient or incorrect, since they are unable to relate the data to causal
inference logic, applying only probabilistic dependencies. Causal Machine Learning methods seem to
close this logical gap, promising accurate predictions based on causal associations instead of
probabilistic correlations. In the paper which accompanies the code in this repository we analyze the two most prevalent tools based on Causal
Machine Learning methods, Microsoft's PyWhy (formerly known as DoWhy) and Uber's CausalML
libraries, in Python, as well as the mathematical underpinnings of the methods they implement.
Finally, the operation of the tools is demonstrated by examining the response to 18 queries, based on
the IDEAL Household Energy Dataset, published by the University of Edinburgh.

As described in thesis, the file structure is as follows:
In the Data Preprocessing folder, the dataset is processed (mean calculation based on time criteria, zero values removal, alphanumeric values to numeric values convertion etc.)
Each query folder contains the source code for the tools used, PyWhy and CausalML, as well as the code needed for further per-query preprocessing. The queries as well as the interpretation of the results can be found in thesis https://hdl.handle.net/10889/25228, chapter "Implementation".

