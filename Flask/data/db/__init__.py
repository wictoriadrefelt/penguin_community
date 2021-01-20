from mongoengine import connect

db = connect(
    db='mongo-penguin',
    host='localhost',
    port=27016,
    username='root',
    password='penguin',
    authentication_source='admin'
)
