import data.repositories.web_repo as wr
from app import bcrypt
from bson import ObjectId


# def create_new_post(location, fishes, image, description, time_stamp):
#    return wr.create_new_post(location, fishes, image, description, time_stamp)


def get_user_by_email(email):
    return wr.get_user_by_email(email)


def create_new_user(first_name, last_name, email, password):
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    return wr.create_new_user(first_name, last_name, email, hashed_password)


def create_new_post(email, description, photo):
    user = get_user_by_email(email)
    return wr.create_new_post(user, description, photo)

def get_all_posts():
    return wr.get_all_posts()


# def add_comment_to_post(post_id, comment_id):
#    return wr.add_comment_to_post(post_id, comment_id)


# def create_new_comment(user_id, first_name, last_name, text, time_stamp):
#    return wr.create_new_comment(user_id, first_name, last_name, text, time_stamp)

"""def like_post():
    return"""

def get_users_by_first_or_last_name(search_input):
    users_first = wr.get_users_by_first_name(search_input)
    users_last = wr.get_users_by_last_name(search_input)
    users = set(users_first) | set(users_last)

    return [
        {"first name": user.first_name.capitalize(),
         "last name": user.last_name.capitalize()}
        for user in users]
