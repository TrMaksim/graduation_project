### Project "System for distributing expenses for meetings with friends"
# Project description.
The project "System for distributing expenses for meetings with friends" is designed to automate the distribution of expenses between meeting participants. Every week, a group of friends meets in a cafe to drink tea and chat. The software solution helps to automatically calculate how much each participant should contribute to equalize the total cost.

# Main functionalities:

User registration: Users can register their accounts by providing their email, password, phone number, and username.
User authorization: Registered users can log in with their email and password.
Creating appointments: Users can create new meetings by specifying a meeting location and date.
Adding participants to a meeting: Users can add other users to their meetings by specifying their IDs.
Creating purchases: During the meeting, users can create purchase records by specifying the amount, description, and participants who jointly paid for this purchase.
Debt calculation: The system automatically calculates how much each meeting participant owes to other participants to equalize the total costs.
Comments on expenses: Users can add comments to each purchase to indicate what exactly the expense was for.
Data protection: The project ensures the security of user data using authentication and authorization, as well as password encryption.

## Installation and startup instructions
# Upload your project repository from GitHub:
```
git clone https://github.com/your-repository.git
cd your-repository
```
# Install the necessary dependencies using pip:
```
pip install -r requirements.txt
```
# Start the server using uvicorn:
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
# After launching, your web application will be available at the following address:
```
http://localhost:8000
```
# Technologies used
Python and the FastAPI framework for developing a web application.
SQLAlchemy for working with the database.
JWT for user authentication and authorization.
Database for storing user data, appointments, purchases, and debts.
[Database model]![Blank diagram (3)](https://github.com/TrMaksim/graduation_project/assets/127137829/db2c3b0e-3188-428f-a6f6-afbd7d752db3)

# Author
Trachuk Maksym for suggestions contact the author by e-mail `tracukmaksim@gmail.com`.

# License
This project is distributed under the license [MIT]([[ссылка-на-лицензию](https://opensource.org/licenses/MIT)](https://opensource.org/license/mit/)).

This project was created for convenient and fair distribution of expenses during meetings with friends and can be used to account for shared expenses between any group of people. Enjoy your meetings and let this system make your life easier!
