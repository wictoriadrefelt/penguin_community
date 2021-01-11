from mongoengine import connect

connect(
    db='mongo-penguin',
    host='localhost',
    port=27016,
    username='root',
    password='penguin',
    authentication_source='admin'
)
