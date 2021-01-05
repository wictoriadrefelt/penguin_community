from mongoengine import connect, Document, StringField


class Customer(Document):
    first_name = StringField(max_length=100)
    last_name = StringField()
    email = StringField()


def main():
    connect(db='product_db', host='localhost', port=27016, username='root', password='s3cr37',
            authentication_source='admin')
    customer1 = Customer(first_name="Anders", last_name="Andersson", email='anders@email.com')
    customer1.save()
