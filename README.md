<h1>Project "System for distributing expenses for meetings with friends"</h1>
<h2>Project description</h2>
The project "System for distributing expenses for meetings with friends" is designed to automate the distribution of expenses between meeting participants. Every week, a group of friends meets in a cafe to drink tea and chat. The software solution helps to automatically calculate how much each participant should contribute to equalize the total cost.

<h2>Main functionalities:</h2>

<h3>User registration:</h3> Users can register their accounts by providing their email, password, phone number, and username.

<h3>User authorization:</h3> Registered users can log in with their email and password.

<h3>Creating appointments:</h3> Users can create new meetings by specifying a meeting location and date.

<h3>Adding participants to a meeting:</h3> Users can add other users to their meetings by specifying their IDs.

<h3>Creating purchases:</h3> During the meeting, users can create purchase records by specifying the amount, description, and participants who jointly paid for this purchase.

<h3>Debt calculation:</h3> The system automatically calculates how much each meeting participant owes to other participants to equalize the total costs.

<h3>Comments on expenses:</h3> Users can add comments to each purchase to indicate what exactly the expense was for.

<h3>Data protection:</h3> The project ensures the security of user data using authentication and authorization, as well as password encryption.


<h2>Installation and startup instructions</h2>

Upload your project repository from GitHub:
```
git clone https://github.com/your-repository.git
cd your-repository
```
Install the necessary dependencies using pip:
```
pip install -r requirements.txt
```
Start the server using uvicorn:
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
After launching, your web application will be available at the following address:
```
http://localhost:8000
```
# Technologies used

1.Python and the FastAPI framework for developing a web application.

2.SQLAlchemy for working with the database.

3.JWT for user authentication and authorization.

4.Database for storing user data, appointments, purchases, and debts.

[Database model]![Blank diagram (3)](https://github.com/TrMaksim/graduation_project/assets/127137829/db2c3b0e-3188-428f-a6f6-afbd7d752db3)

# Author
Trachuk Maksym for suggestions contact the author by e-mail `tracukmaksim@gmail.com`.

# License
This project is distributed under the license [MIT]([[ссылка-на-лицензию](https://opensource.org/licenses/MIT)](https://opensource.org/license/mit/)).

This project was created for convenient and fair distribution of expenses during meetings with friends and can be used to account for shared expenses between any group of people. Enjoy your meetings and let this system make your life easier!
