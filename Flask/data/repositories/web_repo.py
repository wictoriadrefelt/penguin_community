import mongoengine
from datetime import datetime
from data.models.models import Users, Posts
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

def get_all_posts():

    return Posts.objects.all()



def create_new_user(first_name, last_name, email, password):
    new_user = Users(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )
    new_user.save()


def create_new_post(user, description, new_photo):
    print(new_photo.filename)
    new_post = Posts(
        user=user,
        description=description
    )

    new_post.photo.put(new_photo, content_type='image/jpeg')
    print(new_post)

    new_post.save()


