import data.repositories.web_repo as wr

from bson import ObjectId


#  please remove
# def create_new_post(location, fishes, image, description, time_stamp):
#    return wr.create_new_post(location, fishes, image, description, time_stamp)


def create_new_user(first_name, last_name, email, password):
    return wr.create_new_user(first_name, last_name, email, password)




#def add_comment_to_post(post_id, comment_id):
#    return wr.add_comment_to_post(post_id, comment_id)


#def create_new_comment(user_id, first_name, last_name, text, time_stamp):
#    return wr.create_new_comment(user_id, first_name, last_name, text, time_stamp)

"""def like_post():
    return"""