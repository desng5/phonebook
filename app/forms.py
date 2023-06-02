from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, EqualTo


class Entry(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    phone_num = StringField('Phone Number', validators=[InputRequired()])
    address = StringField('Address')
    submit = SubmitField('Submit')
