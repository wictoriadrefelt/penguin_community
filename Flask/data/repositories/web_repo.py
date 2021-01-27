import mongoengine
from datetime import datetime
from data.models.models import Users, Posts, Comment
db = mongoengine
import bson

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


def get_posts_by_user_id(user_id):
    print(user_id)
    return Posts.objects(user=bson.objectid.ObjectId(user_id))


def get_user_by_email(email):
    return Users.objects(email=email).first()


def get_user_by_id(user_id):
    return Users.objects.get(id=bson.objectid.ObjectId(user_id))


def get_all_posts():

    return Posts.objects.all()


def create_new_user(first_name, last_name, email, password, profile_picture):
    new_user = Users(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )

    new_user.profile_picture.put(profile_picture, content_type='image/jpeg')
    print(new_user)

    new_user.save()


def create_new_post(user, description, new_photo):
    new_post = Posts(
        user=user,
        description=description
    )

    new_post.photo.put(new_photo, content_type='image/jpeg')
    print(new_post)

    new_post.save()


def create_new_comment(user, comment, post_id):
    comment_obj = Comment(
        user=user,
        comment=comment
    )
    post = get_post_by_post_id(post_id)

    post.comments.append(comment_obj)
    post.save()


def get_users_by_first_name(first_name):
    return Users.objects(first_name__icontains=first_name)

  
def get_users_by_last_name(last_name):
    return Users.objects(last_name__icontains=last_name)

  
def delete_post_by_id(post_id):
    post = Posts.objects.get(id=bson.objectid.ObjectId(post_id))
    post.delete()


def get_post_by_post_id(post_id):
    return Posts.objects.get(id=bson.objectid.ObjectId(post_id))


def add_friend(user, follow_id):

    if follow_id not in user.following:
        user.following.append(follow_id)

def add_fish_to_post(post_id):
    post = Posts.objects.get(id=bson.objectid.ObjectId(post_id))
    post.fishes.append




