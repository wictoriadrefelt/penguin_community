from mongoengine import connect, Document, StringField


class Customer(Document):
    first_name = StringField(max_length=100)
    last_name = StringField()
    email = StringField()


def main():
    a = connect(db='mongo-penguin', host='localhost', port=27016, username='root', password='penguin',
            authentication_source='admin')
    # customer1 = Customer(first_name="Anders", last_name="Andersson", email='anders@email.com')
    # customer1.save()
    users = Users.objects()
    for user in users:
        print(user.name)
class Users(Document):
    name = StringField()

main()