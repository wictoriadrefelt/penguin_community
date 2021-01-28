import data.repositories.web_repo as wr
from app import bcrypt


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

def add_friend(email, follow_id):
    user = get_user_by_email(email)
    return wr.add_friend(user, follow_id)

def add_fish_to_post(post_id, email):
    post = get_post_by_post_id(post_id)
    fish_giver = get_user_by_email(email)
    return wr.add_fish_to_post(post, fish_giver)

