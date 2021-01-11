from mongoengine import connect, Document, StringField


class Customer(Document):
    first_name = StringField(max_length=100)
    last_name = StringField()
    email = StringField()


class Users(Document):
    name = StringField()
    username = StringField()


def main():
    a = connect(db='mongo-penguin', host='localhost', port=27016, username='root', password='penguin',
            authentication_source='admin')
    customer1 = Customer(first_name="Anders", last_name="Andersson", email='anders@email.com')



    customers = Customer.objects()
    for customer in customers:
        print("first name:", customer.first_name, customer.last_name, customer.email)


    users = Users.objects()
    for user in users:
        print("user:", user.name)

class Users(Document):
    name = StringField()
    username = StringField()

main()