This is a web application a Hair Salon Page. The application is built using Flask, HTML, CSS.

Link to Page: https://www.cocoashairbar.com/

Features
Home Page: Displays a collection of placeholder WEBM images and GIFs retrieved locally.

Services Page: Provides information about the services offered by the website.

Contact Page: Allows users to send messages to the website owner. The messages are sent via email using the Gmail SMTP server from a form using Flask-WTF Forms.

French Version: The application also includes a French version of the home, services, and contact pages.

Setup
Install the required dependencies by running the following command:

pip install -r requirements.txt
Create a .env file in the root directory and add the following environment variables:

python app.py
Access the application in your web browser by visiting http://localhost:5000.
File Structure
app.py: The main Flask application file.
form.py: Contains the form classes for the contact pages.
.env: Contains the environment variables for the application.
insta-images.db: SQLite database file.
templates/: Directory containing the HTML templates for the application.
static/: Directory containing static files (CSS, JS, images) for the application.
Dependencies
Flask: Framework for building web applications in Python.
Flask-SQLAlchemy: Integration of SQLAlchemy with Flask.
python-dotenv: Library for reading environment variables from a .env file.
Flask-WTF: Extension for handling HTML forms in Flask.
emailmessage: Package for creating and sending email messages.
smtplib: Library for sending emails using the SMTP protocol.
openssl: Library for creating SSL/TLS certificates and key pairs.
