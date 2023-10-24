from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Regexp
from flask_wtf import FlaskForm

class EmailForm(FlaskForm):
    """
    Form class for collecting email information from user.
    Inherits from FlaskForm
    """
    f_name = StringField(label='First Name', render_kw={"placeholder": "First Name"}, validators=[DataRequired()])
    l_name = StringField(label='Last Name', render_kw={"placeholder": "Last Name"}, validators=[DataRequired()])
    email = StringField(label='Email', render_kw={"placeholder": "Email"}, validators=[DataRequired(), Email()])
    phone_number = StringField(label='Phone Number', render_kw={"placeholder": "Phone Number"}, validators=[DataRequired(), Regexp(regex="^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$", message="Invalid Phone Number")])
    message = TextAreaField(label="Write a message", render_kw={"placeholder": "Write a message"}, validators=[DataRequired()])
    submit = SubmitField(label="Send Message")
    
class EmailFormFr(FlaskForm):
    """
    Form class for collecting email information from user.
    Inherits from FlaskForm
    
    Translated to French
    """
    f_name = StringField(label='Prénom', render_kw={"placeholder": "Prénom"}, validators=[DataRequired(message="Ce champ est requis")])
    l_name = StringField(label='Nom', render_kw={"placeholder": "Nom"}, validators=[DataRequired(message="Ce champ est requis")])
    email = StringField(label='Email', render_kw={"placeholder": "Email"}, validators=[DataRequired(message="Ce champ est requis"), Email(message="Email invalide")])
    phone_number = StringField(label='Numéro de téléphone', render_kw={"placeholder": "Numéro de téléphone"}, validators=[DataRequired(message="Ce champ est requis"), Regexp(regex="^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$", message="Numéro de téléphone invalide")])
    message = TextAreaField(label="Écrire un message", render_kw={"placeholder": "Écrire un message"}, validators=[DataRequired(message="Ce champ est requis")])
    submit = SubmitField(label="Envoyer le message") 
    
    