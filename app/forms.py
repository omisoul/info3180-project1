from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import StringField, TextAreaField, IntegerField, DecimalField, SelectField
from wtforms.validators import InputRequired


class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    photoFileName = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Invalid file type, please try again'])
    ])
    noBedrooms = IntegerField('No. of Bedrooms', validators=[InputRequired()])
    noBathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    price = DecimalField('Price', validators=[InputRequired()])
    propertyType = SelectField('Property Type',
                                choices=[
                                    ('House', 'House'),
                                    ('Apartment', 'Apartment')
                                ])
