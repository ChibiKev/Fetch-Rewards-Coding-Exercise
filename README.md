# Fetch-Rewards-Coding-Exercise
## Project Description
### The Task
The following task can be found using this [link](https://fetch-hiring.s3.us-east-1.amazonaws.com/points.pdf).
It can also be viewed [here](points.pdf) if the link can't be accessed.
### Dependencies Used
`flask` - Our Restful API Framework

`flask-sqlalchemy` - Database Used To Store Data Such as Users and Transactions.
## Getting Started
### Requirements
1. Git
2. Python
### Steps
1. Clone This Repository:
```
git clone https://github.com/ChibiKev/Fetch-Rewards-Coding-Exercise.git
```
2. Using The Terminal/Command Prompt, Access The Folder Directory:
```
cd Fetch-Rewards-Coding-Exercise
```
3. Download The Requirements Needed To Run This Project:
```
pip install -r requirements.txt
```
4. Run The Flask App:
```
flask run
```

## Following The Example
From Postman Call Theses Following Requests:

**Note:** For POST requests make sure your body accepts JSON. To do this, select the body tab, select the radio button that says raw. A dropdown should appear on the right, select JSON.
| Step # | Request | URL | Body |
|-------|-------- |-----|------|
| 1 | POST | http://127.0.0.1:5000/account/add | { "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" } |
| 2 | POST | http://127.0.0.1:5000/account/add | { "payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z" } |
| 3 | POST | http://127.0.0.1:5000/account/add | { "payer": "DANNON", "points": -200, "timestamp": "2020-10-31T15:00:00Z" } |
| 4 | POST | http://127.0.0.1:5000/account/add | { "payer": "MILLER COORS", "points": 10000, "timestamp": "2020-11-01T14:00:00Z" } |
| 5 | POST | http://127.0.0.1:5000/account/add | { "payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z" } |
| 6 | POST | http://127.0.0.1:5000/account/spend | { "points": 5000 } |
| 7 | GET | http://127.0.0.1:5000/account/balance | |

## API Calls
Perform theses using Postman.
When calling this API the URL is `http://127.0.0.1:5000`
### Get Requests
`/` - Short Description of The Project.

`/checkUsers` - Get All IDs of Users. Mainly Used For Testing Purposes Since There Is Only 1 User So Far.

`/account` - Get User's Current Points

`/account/balance` - Get Total Amount of Points For Each Payer

`/account/transactions` - Get All Transactions

`/account/add` - Get Instructions of How to Add

`/account/spend` - Get Instructions of How to Spend
### Post Requests
**Note:** For POST requests make sure your body accepts JSON. To do this, select the body tab, select the radio button that says raw. A dropdown should appear on the right, select JSON.

`/account/add` - Add Transaction Into Current User

`/account/spend` - Spend Current User Points

## Moving Forward
- There are still a few BUGs that needs to be fixed to work in production.
- This API is scalable by:
  - Increasing the amount of users. A user model has already been created so we're able to modify our API to work for multiple users.
  - Marking which transaction is already used to improve efficiency.