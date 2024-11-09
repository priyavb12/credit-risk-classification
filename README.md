# credit-risk-classification
### challenge 20

Machine learning techniques are used to analyze a dataset of historical lending activity from a peer-to-peer lending services company to build a model that can identify the creditworthiness of borrowers.

Overview of the Analysis
Factors considered in the analysis included data on:

- the size of the loan

- its interest rate

- the borrower's income

- the debt to income ratio

the number of accounts the borrower held
derogatory marks against the borrower
the total debt
The dataset (77,536 data points) was split into training and testing sets. 
The training set was used to build an initial logistic regression model (Logistic Regression Model 1) using the LogisticRegression module from scikit-learn. 
Logistic Regression Model 1 was then applied to the testing dataset. 
The purpose of the model was to determine whether a loan to the borrower in the testing set would be low- or high-risk 

### Results

Logistic Regression Model 1:

Precision: 93% (an average--in predicting low-risk loans, the model was 100% precise, though the model was only 87% precise in predicting high-risk loans)
Accuracy: 91%

Recall: 85% (an average--the model had 100% recall in predicting low-risk loans, but 89% recall in predicting high-risk loans)

