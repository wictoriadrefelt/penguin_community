import codecs
import data.repositories.web_repo as wr
import data.repositories.post_repo as pr


def decode_picture(picture):
    base64_data = codecs.encode(picture.read(), 'base64')
    return base64_data.decode('utf-8')


def convert_datetime_to_str(datetime_obj):
    return datetime_obj.strftime('%Y-%m-%d')


def get_milliseconds_since_epoch(datetime_obj):
    return int(datetime_obj.timestamp()) * 1000


def get_dicts_of_posts(post_list):
    return [{"first_name": post.user.first_name,
             "last_name": post.user.last_name,
             "description": post.description,
             "ms_since_post_date": get_milliseconds_since_epoch(post.post_date),
             "photo": decode_picture(post.photo),
             "profile_picture": decode_picture(post.user.profile_picture),
             "fishes": wr.number_of_fishes_on_post(post.id),
             "post_user_id": str(post.user.id),
             "comment": pr.number_of_comments_on_posts(post.id),
             "post_id": str(post.id)}
            for post in post_list]