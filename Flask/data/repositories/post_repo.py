from data.models.models import Posts
from data.repositories.web_repo import get_post_by_post_id

def get_posts_paginate(page_num=1, items_per_page=3):
    offset = (page_num - 1) * items_per_page
    return Posts.objects.order_by('-post_date').skip(offset).limit(items_per_page)


def number_of_comments_on_posts(post_id):
    post = get_post_by_post_id(post_id)
    return len(post.comments)
