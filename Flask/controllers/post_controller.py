import data.repositories.web_repo as wr
from controllers.controller_functions import get_dicts_of_posts
from controllers.web_controller import get_post_from_huddle


def get_posts_paginate(posts_id_list, page_num=1, items_per_page=3):
    posts = [wr.get_post_by_post_id(post_id) for post_id in posts_id_list]
    page_num -= 1
    posts = posts[page_num*items_per_page: page_num+items_per_page]
    return get_dicts_of_posts(posts)


def get_comments_on_post(post_id):
    return pr.get_comments_on_post(post_id)


def number_of_comments_on_posts(post_id):
    return pr.number_of_comments_on_posts(post_id)

  
def get_posts_id_from_user_huddle_list(user_email):
    return [str(post.id) for post in get_post_from_huddle(user_email)]

