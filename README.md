# Fetch-Rewards-Coding-Exercise
## Project Description
### The Task
https://fetch-hiring.s3.us-east-1.amazonaws.com/points.pdf
### Dependencies Used
`flask` - Our Restful API Framework

`flask-sqlalchemy` - Database Used To Store Data Such as Users and Transactions.
## Get Started
Download Requirements
```
pip install -r requirements.txt
```
Run Flask App
```
flask run
```

## API Calls
Perform theses using Postman.
When calling this API the root is `http://127.0.0.1:5000`
### Get Requests
`/` - Short Description of The Project.

`/checkUsers` - Get All IDs of Users. Mainly Used For Testing Purposes Since There Is Only 1 User So Far.

`/account` - Get User's Current Points

`/account/transactions` - Get All Transactions

`/account/add` - Get Instructions of How to Add

`/account/spend` - Get Instructions of How to Spend
### Post Requests

`/account/add` - Add Transaction Into Current User

`/account/spend` - Spend Current User Points

## Moving Forward
This API is scalable by increasing the amount of users and changing the API so it accepts multiple users using an ID for each user.