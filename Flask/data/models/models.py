from data import db
from mongoengine import Document, StringField, ListField, ReferenceField, EmbeddedDocumentField, EmbeddedDocument
from app import login_manager
from flask_login import UserMixin



# https://www.javatpoint.com/javascript-form-validation


@login_manager.user_loader
def load_user(user_email):
    return Users.objects(user=user_email)


class Users(Document, UserMixin):
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
