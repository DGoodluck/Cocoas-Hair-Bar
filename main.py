from email.message import EmailMessage
import os
import smtplib
import ssl
from flask import Flask, render_template, request, flash
from dotenv import load_dotenv
from form import EmailForm, EmailFormFr

app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

def send_email(form):
    """
    If the request method is POST and the form is valid, 
    it sends an email to a specified receiver.
    """
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


@app.route("/")
def home():
    """
    Handles the route for the home page. 
    Renders 'index.html' template when / endpoint is hit
    """
    folder_dir = "static/index-images"
    photos = []
    for filename in os.listdir(folder_dir):
        if filename.endswith('.webm'):
            photos.append({'is_video': True, 'filename': filename})
        else:
            photos.append({'is_video': False, 'filename': filename})
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
    If the form is not valid, it flashes an error message for each field with errors.
    """
    form = EmailForm()
    if request.method == 'POST' and form.validate_on_submit():
        send_email(request.form)
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
    folder_dir = "static/index-images"
    photos = []
    for filename in os.listdir(folder_dir):
        if filename.endswith('.webm'):
            photos.append({'is_video': True, 'filename': filename})
        else:
            photos.append({'is_video': False, 'filename': filename})
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
    If the form is not valid, it flashes an error message for each field with errors.
    """
    form = EmailFormFr()
    if request.method == 'POST' and form.validate_on_submit():
        send_email(request.form)
        flash("Message Envoyé !")
    else:
        # Form has validation errors. Flash an error message for each field.
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{error}', 'error')

    return render_template('fr-contact.html', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)