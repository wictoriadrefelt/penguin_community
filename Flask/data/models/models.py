from data import db
from mongoengine import Document, StringField, ListField, ReferenceField, EmbeddedDocumentField, EmbeddedDocument, FileField, IntField, DateTimeField
from app import login_manager
from flask_login import UserMixin
from flask import session, redirect, url_for
from functools import wraps
from data.db import request
import datetime


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
    profile_picture = FileField(default="/static/images/img_avatar1.png")
    huddle = ListField(StringField())

    def __repr__(self):
        return f"User({self.first_name}, {self.last_name}, {self.email})"


class Comment(EmbeddedDocument):
    user = ReferenceField(Users)
    comment = StringField()
    comment_date = DateTimeField(default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Comment({self.comment})"


class Posts(Document):
    user = ReferenceField(Users)
    description = StringField(max_length=280)
    photo = FileField()
    fishes = ListField(StringField())
    post_date = DateTimeField(default=datetime.datetime.utcnow)
    comments = ListField(EmbeddedDocumentField(Comment))

    def __repr__(self):
        return f"Post({self.user}, {self.description})"



