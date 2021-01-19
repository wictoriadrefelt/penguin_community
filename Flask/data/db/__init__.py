from mongoengine import connect

connect(
    db='mongo_penguin',
    host='localhost',
    port=27015,
    username='root',
    password='penguin',
    authentication_source='admin'
)
