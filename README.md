README
This is a web application a Hair Salon Page. The application is built using Flask, SQLAlchemy, and Selenium.
Link to Page: https://dg716.pythonanywhere.com/

Features
Home Page: Displays a collection of placeholder images retrieved from the iStockphoto website. The images are stored in a SQLite database.

Services Page: Provides information about the services offered by the website.

Contact Page: Allows users to send messages to the website owner. The messages are sent via email using the Gmail SMTP server from a form using Flask-WTF Forms.

French Version: The application also includes a French version of the home, services, and contact pages.

Setup
Install the required dependencies by running the following command:


pip install -r requirements.txt
Create a .env file in the root directory and add the following environment variables:


SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///insta-images.db
EMAIL=your_email_address
EMAIL_RECEIVER=receiver_email_address
PASSWORD=your_email_password
Run the application using the following command:


python app.py
Access the application in your web browser by visiting http://localhost:5000.

The first time the application is run, it will retrieve a collection of placeholder images from the iStockphoto website and store them in the database. The images are only retrieved once using the run_once.txt file to keep track of whether the script has been run before.

File Structure
app.py: The main Flask application file.
form.py: Contains the form classes for the contact pages.
.env: Contains the environment variables for the application.
insta-images.db: SQLite database file.
templates/: Directory containing the HTML templates for the application.
static/: Directory containing static files (CSS, JS, images) for the application.
Dependencies
Flask: Framework for building web applications in Python.
SQLAlchemy: Toolkit for working with databases in Python.
Selenium: Library for automating browser activities.
Flask-SQLAlchemy: Integration of SQLAlchemy with Flask.
python-dotenv: Library for reading environment variables from a .env file.
Flask-WTF: Extension for handling HTML forms in Flask.
emailmessage: Package for creating and sending email messages.
smtplib: Library for sending emails using the SMTP protocol.
openssl: Library for creating SSL/TLS certificates and key pairs.
