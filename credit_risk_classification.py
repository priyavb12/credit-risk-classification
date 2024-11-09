#!/usr/bin/env python
# coding: utf-8

# In[40]:


# Import the modules
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.metrics import confusion_matrix, classification_report


# ---

# ## Split the Data into Training and Testing Sets

# ### Step 1: Read the `lending_data.csv` data from the `Resources` folder into a Pandas DataFrame.

# In[45]:


# Read the CSV file from the Resources folder into a Pandas DataFrame
# YOUR CODE HERE!
lending_data_df = pd.read_csv('lending_data.csv')
# Review the DataFrame
# YOUR CODE HERE!
lending_data_df


# ### Step 2: Create the labels set (`y`)  from the “loan_status” column, and then create the features (`X`) DataFrame from the remaining columns.

# In[48]:


# Separate the data into labels and features

# Separate the y variable, the labels
# YOUR CODE HERE!]
y = lending_data_df['loan_status']
# Separate the X variable, the features
# YOUR CODE HERE!
X = lending_data_df.drop(columns='loan_status')


# In[50]:


# Review the y variable Series
# YOUR CODE HERE!
y.head()


# In[52]:


# Review the X variable DataFrame
# YOUR CODE HERE!
X.head()


# ### Step 3: Split the data into training and testing datasets by using `train_test_split`.

# In[55]:


# Import the train_test_learn module
from sklearn.model_selection import train_test_split

# Split the data using train_test_split
# Assign a random_state of 1 to the function
# YOUR CODE HERE!
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


# ---

# ## Create a Logistic Regression Model with the Original Data

# ###  Step 1: Fit a logistic regression model by using the training data (`X_train` and `y_train`).

# In[60]:


# Import the LogisticRegression module from SKLearn
from sklearn.linear_model import LogisticRegression

# Instantiate the Logistic Regression model
# Assign a random_state parameter of 1 to the model
# YOUR CODE HERE!
lr_model = LogisticRegression(random_state=1)
# Fit the model using training data
# YOUR CODE HERE!
lr_model.fit(X_train, y_train)


# ### Step 2: Save the predictions on the testing data labels by using the testing feature data (`X_test`) and the fitted model.

# In[63]:


# Make a prediction using the testing data
# YOUR CODE HERE!
y_predictions = lr_model.predict(X_test)
y_predictions


# ### Step 3: Evaluate the model’s performance by doing the following:
# 
# * Generate a confusion matrix.
# 
# * Print the classification report.

# In[66]:


# Generate a confusion matrix for the model
# YOUR CODE HERE!
pd.DataFrame(confusion_matrix(y_test, y_predictions))


# In[68]:


# Print the classification report for the model
# YOUR CODE HERE!
print(classification_report(y_test, y_predictions))


# ### Step 4: Answer the following question.

# **Question:** How well does the logistic regression model predict both the `0` (healthy loan) and `1` (high-risk loan) labels?
# 
# **Answer:**The logistic regression model using the original data does good job of predicting values for the 0 class health loans data. The precision for class 0 it gets 1.00
# meaning tge model correctly made the positive prediction virtually everytime.
# the logistic regression did not do quiet as good job the values for 1 high risk loans 85%.recall is a 91% overall the logistic regression model generated pretty good results.

# ---

# In[ ]:




