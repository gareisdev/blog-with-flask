from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField, TextAreaField
from wtforms.validators import Required

class PostForm(FlaskForm):
    title = StringField("Title", validators=[Required("Please, insert a Title")])
    description = StringField("Description", validators=[Required("Please, insert a Description")])
    content = TextAreaField("Content", validators=[Required("Please, insert a Content")])
    image = StringField("Image", validators=[Required("Please, insert a URL Image")])
    
    submit = SubmitField("CREATE")