import data.repositories.post_repo as pr
import data.repositories.web_repo as wr
import codecs


def get_posts_paginate(page_num=1, items_per_page=3):
    posts = pr.get_posts_paginate(page_num, items_per_page)

    return [{"first_name": post.user.first_name,
             "last_name": post.user.last_name,
             "description": post.description,
             "photo": convert_picture(post.photo),
             "profile_picture": convert_picture(post.user.profile_picture),
             "fishes": wr.number_of_fishes_on_post(post.id),
             "post_user_id": str(post.user.id)}
            for post in posts]


def convert_picture(picture):
    base64_data = codecs.encode(picture.read(), 'base64')
    return base64_data.decode('utf-8')
