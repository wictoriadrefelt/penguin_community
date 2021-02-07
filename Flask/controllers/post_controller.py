import data.repositories.post_repo as pr
import data.repositories.web_repo as wr
from controllers.controller_functions import decode_picture, get_milliseconds_since_epoch


def get_posts_paginate(page_num=1, items_per_page=3):
    posts = pr.get_posts_paginate(page_num, items_per_page)

    return [{"first_name": post.user.first_name,
             "last_name": post.user.last_name,
             "description": post.description,
             "ms_since_post_date": get_milliseconds_since_epoch(post.post_date),
             "photo": decode_picture(post.photo),
             "profile_picture": decode_picture(post.user.profile_picture),
             "fishes": wr.number_of_fishes_on_post(post.id),
             "post_user_id": str(post.user.id)}
            for post in posts]
