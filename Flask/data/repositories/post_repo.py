from data.models.models import Posts


def get_posts_paginate(page_num=1, items_per_page=3):
    offset = (page_num - 1) * items_per_page
    return Posts.objects.skip(offset).limit(items_per_page)