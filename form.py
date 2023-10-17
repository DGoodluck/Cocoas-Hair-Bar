from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length, Regexp

class Email(FlaskForm):
    f_name = StringField(label='First Name', render_kw={"placeholder": "First Name"}, validators=[DataRequired()])
    l_name = StringField(label='Last Name', render_kw={"placeholder": "Last Name"}, validators=[DataRequired()])
    email = StringField(label='Email', render_kw={"placeholder": "Email"}, validators=[DataRequired(), Email()])
    phone_number = StringField(label='Phone Number', render_kw={"placeholder": "Phone Number"}, validators=[DataRequired(), Regexp(regex="^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$", message="Invalid Phone Number")])
    message = TextAreaField(label="Write a message", render_kw={"placeholder": "Write a message"}, validators=[DataRequired()])
    submit = SubmitField(label="Send Message")
    
    