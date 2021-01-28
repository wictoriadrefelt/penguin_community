import mongoengine
from datetime import datetime
from data.models.models import Users, Posts, Comment
db = mongoengine
import bson


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


def add_to_huddle(huddle_id, user):

    huddle_id_string = str(huddle_id)
    if huddle_id_string not in user.huddle:
        user.huddle.append(huddle_id_string)
        user.save()
        return True

    else:
        user.huddle.remove(huddle_id_string)
        user.save()
        return False

def add_fish_to_post(post, fish_giver):

    fish_giver_id = str(fish_giver.id)
    if fish_giver_id not in post.fishes:
        post.fishes.append(fish_giver_id)
        post.save()
        print(post.fishes, len(post.fishes))
        return True

    else:
        post.fishes.remove(fish_giver_id)
        post.save()
        return False


def number_of_fishes_on_post(post_id):
    post = get_post_by_post_id(post_id)
    return len(post.fishes)


def get_huddlers_from_user(user):
    return user.huddle


def get_post_from_huddle(email):
    return get_post_from_huddle(email)