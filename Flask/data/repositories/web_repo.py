import mongoengine
from datetime import datetime
from data.models.models import Users
db = mongoengine

"""
def create_new_post(location, fishes, image, description, time_stamp):
    post = ({
        'Location': location,
        'Fishes': fishes,
        'Image': image,
        'Description': description,
        'Tags': [],
        'Timestamp': time_stamp,
        'Comments': []

    })

    db.users.insert_one(user)
"""


def get_user_by_email(email):
    return Users.objects(email=email).first()



def create_new_user(first_name, last_name, email, password):
    new_user = Users(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )
    new_user.save()


def create_new_post(title, description, tags, photo):
    new_post = Posts(
        title=title,
        description=description,
        tags=tags,
        photo=photo
    )

    new_post.save()


