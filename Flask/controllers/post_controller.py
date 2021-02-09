from datetime import datetime

import data.repositories.web_repo as wr
from controllers.controller_functions import get_dicts_of_posts
from controllers.web_controller import get_post_from_huddle
import data.repositories.post_repo as pr


def get_posts_paginate(posts_id_list, page_num=1, items_per_page=3):
    posts = [wr.get_post_by_post_id(post_id) for post_id in posts_id_list]
    page_num -= 1
    posts = posts[page_num*items_per_page: page_num+items_per_page]
    return get_dicts_of_posts(posts)


def get_comments_on_post(post_id):
    return pr.get_comments_on_post(post_id)


def number_of_comments_on_posts(post_id):
    return pr.number_of_comments_on_posts(post_id)

  
def get_posts_id_for_feed(user_email):
    posts_from_huddle = get_post_from_huddle(user_email)
    user = wr.get_user_by_email(user_email)
    posts_from_user = wr.get_posts_by_user_id(user.id)

    posts_from_huddle.extend(posts_from_user)
    sorted_posts = sort_posts_by_date(posts_from_huddle)

    return [str(post.id) for post in sorted_posts]


def sort_posts_by_date(posts_list):
    return sorted(posts_list, key=lambda x: datetime.strftime(x.post_date, '%m/%d/%y %H:%M'), reverse=True)
