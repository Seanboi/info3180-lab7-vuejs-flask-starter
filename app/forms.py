from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,FileField,SubmitField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('description', validators=[InputRequired()])
    poster = FileField('poster', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Add Movie')
    
    
    

    
