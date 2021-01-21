from data import db
from mongoengine import Document, StringField, ListField, ReferenceField, EmbeddedDocumentField, EmbeddedDocument, FileField
from app import login_manager
from flask_login import UserMixin
from flask import session, redirect, url_for
from functools import wraps
from data.db import request



# https://www.javatpoint.com/javascript-form-validation
def login_required(default_page):
    def decorator(route):
        @wraps(route)
        def wrapper(*args, **kwargs):
            if is_authenticated():
                return route(*args, **kwargs)
            return redirect(url_for(default_page, next=request.url))
        return wrapper
    return decorator


def is_authenticated():
    return 'email' in session


@login_manager.user_loader
def load_user(user_email):
    return Users.objects(email=user_email).first()


class Users(Document, UserMixin):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    email = StringField(required=True)
    password = StringField()


class Posts(Document):
    user = StringField(required=True)
    description = StringField(max_length=280)
    photo = FileField()


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