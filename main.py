from flask import Flask, render_template, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from form import Email
import smtplib, ssl
from email.message import EmailMessage
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///insta-images.db"
db = SQLAlchemy()
db.init_app(app)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(250), unique=True, nullable=False)

with app.app_context():
    db.create_all()

# Check if the script has been run before
with open('run_once.txt', 'r') as f:
    has_run = f.read()

# If the script hasn't been run before
if not has_run:
    driver = webdriver.Chrome()
    driver.get("https://greatfon.com/v/cocoashairbar")
    wait = WebDriverWait(driver, 5)

    images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".content__img-wrap a img")))
    image_list = [image.get_attribute('src') for image in images]
    driver.quit()

    with app.app_context():
        for image in image_list:
            existing_image = Image.query.filter_by(link=image).first()
            if existing_image is None:
                new_image = Image(link=image)
                db.session.add(new_image)
        db.session.commit()

    # Write to the file to indicate the script has been run
    with open('run_once.txt', 'w') as f:
        f.write('DONE')

@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Image).order_by(Image.id))
        images = result.scalars()
        return render_template('index.html', images=images)
    
@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/book-appointment")
def book():
    return render_template('book.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = Email()
    if request.method == 'POST' and form.validate_on_submit():
        
        EMAIL_SENDER = os.getenv('EMAIL')
        EMAIL_RECEIVER = 'goodluckdayshaun@gmail.com'
        EMAIL_PASSWORD = os.getenv('PASSWORD')
        
        em = EmailMessage()
        em["From"] = EMAIL_SENDER
        em["To"] = EMAIL_RECEIVER
        em["Subject"] = f"{request.form.get('f_name')} has a Question From your Websites"
        em.set_content(f"{request.form.get('message')}\n\nWarm regards,\n\n{request.form.get('f_name')} {request.form.get('l_name')}\n{request.form.get('phone_number')}\n{request.form.get('email')}")
            
        context = ssl.create_default_context()
            
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, em.as_string())
        flash("Message Sent!")
    else:
        # Form has validation errors. Flash an error message for each field.
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{error}', 'error')

    return render_template('contact.html', form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)