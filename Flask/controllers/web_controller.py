import data.repositories.web_repo as wr
from app import bcrypt
from flask import jsonify
import random

def get_user_by_email(email):
    return wr.get_user_by_email(email)


def create_new_user(first_name, last_name, email, password, profile_picture):
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    return wr.create_new_user(first_name, last_name, email, hashed_password, profile_picture)


def create_new_post(email, description, photo):
    user = get_user_by_email(email)
    return wr.create_new_post(user, description, photo)


def create_new_comment(email, comment, post_id):
    user = get_user_by_email(email)
    wr.create_new_comment(user, comment, post_id)


def get_all_posts():
    return wr.get_all_posts()

  
def get_user_by_id(user_id):
    return wr.get_user_by_id(user_id)


def get_users_by_first_or_last_name(search_input):
    search_input = search_input.rstrip()

    if len(search_input.split()) == 2:
        f_input, l_input = search_input.split()
        users_first = wr.get_users_by_first_name(f_input)
        users_last = wr.get_users_by_last_name(l_input)
    else:
        users_first = wr.get_users_by_first_name(search_input)
        users_last = wr.get_users_by_last_name(search_input)
    users = set(users_first) | set(users_last)

    if users:
        return [
            {"first name": user.first_name.capitalize(),
             "last name": user.last_name.capitalize(),
             "user_id": str(user.id)}
            for user in users]
    else:
        return [{"empty": True}]


def get_post_by_post_id(post_id):
    return wr.get_post_by_post_id(post_id)


def delete_post_by_id(post_id):
    return wr.delete_post_by_id(post_id)


def get_posts_by_user_id(user_id):
    return wr.get_posts_by_user_id(user_id)

def add_to_huddle(huddle_id, email):
    user = get_user_by_email(email)
    return wr.add_to_huddle(huddle_id, user)

def add_fish_to_post(post_id, email):
    post = get_post_by_post_id(post_id)
    fish_giver = get_user_by_email(email)
    return wr.add_fish_to_post(post, fish_giver)


def number_of_fishes_on_post(post_id):
    return wr.number_of_fishes_on_post(post_id)


def get_huddlers_from_user(user):
    return wr.get_huddlers_from_user(user)



def get_post_from_huddle(email):
    user = get_user_by_email(email)
    huddle = get_huddlers_from_user(user)
    post_list = []
    for huddlers in huddle:
        posts = get_posts_by_user_id(huddlers)
        for post in posts:
            post_list.append(post)

    return post_list


def get_huddle_list(user_email):
    user = get_user_by_email(user_email)
    huddle = get_huddlers_from_user(user)
    users = [get_user_by_id(id) for id in huddle]
    return [
            {"first_name": user.first_name.capitalize(),
             "last_name": user.last_name.capitalize(),
             "user_id": str(user.id)}
            for user in users]


def update_user_profile(id, first_name, last_name):
    return wr.update_user_profile(id, first_name, last_name)


def get_random_user(current_email):
    email = current_email
    current_user = get_user_by_email(email)
    current_user_id = current_user.id
    users = wr.get_all_users()
    huddle_list = get_huddle_list(current_user.email)
    random_user = random.choice(users)
    deconstructed_random_user = {
            "first_name": random_user.first_name.capitalize(),
            "last_name": random_user.last_name.capitalize(),
            "user_id": str(random_user.id)}

    if deconstructed_random_user not in huddle_list or random_user.id == current_user_id:
        return deconstructed_random_user

    else:
        print(deconstructed_random_user)
        print(current_email)
        get_random_user(email)


