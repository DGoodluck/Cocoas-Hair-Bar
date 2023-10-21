from email.message import EmailMessage
import os
import smtplib
import ssl
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from form import EmailForm, EmailFormFr

app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///insta-images.db"
db = SQLAlchemy()
db.init_app(app)

class Image(db.Model):
    """
    Database of placeholder images for website. (TO BE REPLACED)
    """
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(250), unique=True, nullable=False)

with app.app_context():
    db.create_all()

# Check if the script has been run before
with open('run_once.txt', 'r', encoding='utf-8') as f:
    has_run = f.read()

# If the script hasn't been run before
if not has_run:
    driver = webdriver.Chrome()
    driver.get("https://www.istockphoto.com/photos/black-woman-hair?servicecontext=srp-related")
    wait = WebDriverWait(driver, 5)

    images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "picture img")))
    image_list = [image.get_attribute('src') for image in images[:50]]
    driver.quit()

    with app.app_context():
        for image in image_list:
            existing_image = Image.query.filter_by(link=image).first()
            if existing_image is None:
                new_image = Image(link=image)
                db.session.add(new_image)
        db.session.commit()

    # Write to the file to indicate the script has been run
    with open('run_once.txt', 'w', encoding='utf-8') as f:
        f.write('DONE')

@app.route("/")
def home():
    """
    Handles the route for the home page. 
    Renders 'index.html' template when / endpoint is hit
    """
    with app.app_context():
        result = db.session.execute(db.select(Image).order_by(Image.id))
        photos = result.scalars()
        return render_template('index.html', photos=photos)
    
@app.route("/services")
def services():
    """
    Handles the route for the service page. 
    Renders 'services.html' template when /services endpoint is hit
    """
    return render_template('services.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    """
    This function handles the route for the contact page. 
    It renders the 'contact.html' template when the '/contact' endpoint is hit.
    If the request method is POST and the form is valid, it sends an email to a specified receiver.
    If the form is not valid, it flashes an error message for each field with errors.
    """
    form = EmailForm()
    if request.method == 'POST' and form.validate_on_submit():
        email_sender = os.getenv('EMAIL')
        email_receiver = 'goodluckdayshaun@gmail.com'
        email_password = os.getenv('PASSWORD')
        
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_receiver
        em["Subject"] = f"{request.form.get('f_name')} has a Question From your Website"
        em.set_content(f"{request.form.get('message')}\n\nWarm regards,\n\n{request.form.get('f_name')} {request.form.get('l_name')}\n{request.form.get('phone_number')}\n{request.form.get('email')}")
            
        context = ssl.create_default_context()
            
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        flash("Message Sent!")
    else:
        # Form has validation errors. Flash an error message for each field.
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{error}', 'error')

    return render_template('contact.html', form=form)

@app.route("/fr")
def fr_home():
    """
    Handles the route for the french home page. 
    Renders 'fr-index.html' template when /fr endpoint is hit
    """
    with app.app_context():
        result = db.session.execute(db.select(Image).order_by(Image.id))
        photos = result.scalars()
        return render_template('fr-index.html', photos=photos)

@app.route("/services/fr")
def fr_services():
    """
    Handles the route for the french service page. 
    Renders 'fr-services.html' template when /fr/services endpoint is hit
    """
    return render_template('fr-services.html')

@app.route("/contact/fr", methods=['GET', 'POST'])
def fr_contact():
    """
    This function handles the route for the french contact page. 
    It renders the 'fr-contact.html' template when the '/fr/contact' endpoint is hit.
    If the request method is POST and the form is valid, it sends an email to a specified receiver.
    If the form is not valid, it flashes an error message for each field with errors.
    """
    form = EmailFormFr()
    if request.method == 'POST' and form.validate_on_submit():
        email_sender = os.getenv('EMAIL')
        email_receiver = os.getenv('EMAIL_RECEIVER')
        email_password = os.getenv('PASSWORD')
        
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_receiver
        em["Subject"] = f"{request.form.get('f_name')} has a Question From your Website"
        em.set_content(f"{request.form.get('message')}\n\nWarm regards,\n\n{request.form.get('f_name')} {request.form.get('l_name')}\n{request.form.get('phone_number')}\n{request.form.get('email')}")
            
        context = ssl.create_default_context()
            
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        flash("Message Envoyé !")
    else:
        # Form has validation errors. Flash an error message for each field.
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{error}', 'error')

    return render_template('fr-contact.html', form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)