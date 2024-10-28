# create some standard users and passwords for easy testing

# from django.contrib.auth.models import User
from users.models import User

user1 = User.objects.create_user('alice', password='apple',
                                 email='tom.sheffler+alice@gmail.com',
                                 first_name='Alice',
                                 last_name='Wonder',
                                 )
user1.is_superuser=False
user1.is_staff=False
user1.save()

user2 = User.objects.create_user('bob', password='berry',
                                 email='tom.sheffler+bob@gmail.com',
                                 first_name='Bob',
                                 last_name='Plumber',
                                 )
user2.is_superuser=False
user2.is_staff=False
user2.save()

