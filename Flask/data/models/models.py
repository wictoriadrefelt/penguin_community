from data import db
from mongoengine import Document, StringField, ListField, ReferenceField, EmbeddedDocumentField, EmbeddedDocument
from flask import Flask

# https://www.javatpoint.com/javascript-form-validation



class Users(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    email = StringField(required=True)
    password = StringField()


"""
class Content(EmbeddedDocument):
    text = StringField()
    lang = StringField(max_length=3)

class Post(Document):
    title = StringField(max_length=120, required=True, validators=[validators.InputRequired(message='Missing title.'),])
    author = ReferenceField(User)
    tags = ListField(StringField(max_length=30))
    content = EmbeddedDocumentField(Content)

PostForm = model_form(Post)

def add_post(request):
    form = PostForm(request.POST)
    if request.method == 'POST' and form.validate():
        # do something
        redirect('done')
    return render_template('add_post.html', form=form)"""
