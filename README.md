# Recommendation System(RecSys) Modelling
## Overview
Given the datasets of clicks of merchants on Shopback Korea between January - March 2021, you are required to :
1. Build a prediction model to predict what is the next merchant a user will click.
2. Serve the model in a web service.

PS: you will not be assessed for the accuracy of the model, instead for the thoughts and engineering process while performing this exercise.

## Schema
### Clicks
`data/clicks.parquet`

| Column Name  | Description |
| ------------- | ------------- |
| id | Click Identifier |
| user_id  | User Identifier  |
| store_id  | Store Identifier  |
| device  | User Device |
| platform | Platform that user makes the click from |
| channel | Channel that contributes the click |
| created_at | Timestamp of the click is made |

### Stores
`data/stores.parquet`
| Column Name  | Description |
| ------------- | ------------- |
| id  | Store Identifier  |
| merchant_id | Corresponding merchant identifier for the store |
| start_at | Store Start Date |
| end_at | Store End Date |
| display_text | Text Displayed for the Store |
| is_searchable | Where Store is Searchable from App |

*  Multiple stores might map to the same merchant

### Users
`data/users.parquet`
| Column Name  | Description |
| ------------- | ------------- |
| id  | User Identifier  |
| signup_datetime | Timestamp of User Sign Up |
| lifetime_first_merchant | The first merchant that user purchase with Shopback |
| lifetime_first_purchase_datetime | Datetime of first purchase |
| account_referral | Referral of the account, usually refers to campaigns |

## EDA 
> Estimate time to spend : 1-3 Hours

Explore the given datasets, derive any interesting findings and visualize it using any tool of your choice. Example questions to answer are :
* What are the most clicked merchant for month January 2021?
* What are the distribution of clicks of merchant for month March 2021?
* On average, what are the number of clicks user make in 1 month?

## Model Building
> Estimate time to spend : 2-5 Hours

Construct the prediction model using any algorithm(s) of your choice. You are required to:
1. Perform Train-Test split for the datasets
2. Measure the performance of the Test Dataset using any RecSys metrics.

## Model Serving
> Estimate time to spend : 2-3 Hours

Encapsulate the final model in form of a web service. The web framework can be written only in Python (most preferred) or Golang (2nd most preferred). 

### Must have:
1. The web service should have an endpoint called `/predict`, that takes in user-defined input as return a `merchant_id` as its prediction output. 
2. Document clearly the steps to run the web service locally.

### Nice to have:
1. Any additional endpoints, e.g. `/batch_predict`, for completeness.
2. Dockerization of the service(s)
3. Good Code Style (e.g. PEP 8 for python)
4. Unit Testing

## Submission
Organize your files and folder like how you would organize in a proper Git Repository. Include the notebooks or scripts used during the exercise.
Please attach a `README.md` file in your root directory that documents:
1. Your file directories
2. Notebooks Path for the corresponding task.
3. Steps to run the Model Web Service
4. and any that would help the interviewers navigate through the repository

Zip the whole repository and send them back to Shopback Talent Acquisition Team.