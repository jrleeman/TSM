from flask_wtf import Form
from wtforms import SubmitField, TextField, TextAreaField, validators

class CreateDatasetForm(Form):
    name = TextField('name', validators=[validators.DataRequired()])

    path = TextField('path', validators=[validators.DataRequired()])

    metadata = TextAreaField('metadata', validators=[validators.DataRequired()])

    submit = SubmitField('submit')