from data.models.models import Posts
from data.repositories.web_repo import get_post_by_post_id


def get_posts_paginate(page_num=1, items_per_page=3):
    offset = (page_num - 1) * items_per_page
    return Posts.objects.order_by('-post_date').skip(offset).limit(items_per_page)


def get_comments_on_post(post_id):
    post = get_post_by_post_id(post_id)
    com = post.comments
    return com


def number_of_comments_on_posts(post_id):
    post = get_comments_on_post(post_id)
    return len(post)
