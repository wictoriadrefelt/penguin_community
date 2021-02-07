import codecs


def decode_picture(picture):
    base64_data = codecs.encode(picture.read(), 'base64')
    return base64_data.decode('utf-8')


def convert_datetime_to_str(datetime_obj):
    return datetime_obj.strftime('%Y-%m-%d')


def get_milliseconds_since_epoch(datetime_obj):
    return int(datetime_obj.timestamp()) * 1000
