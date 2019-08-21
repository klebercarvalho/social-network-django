from django.db import models

# Create your models here.

class Profile(object):

    def __init__(self, name='', email='', phone='', company_name=''):
        self.name = name
        self.email = email
        self.phone = phone
        self.company_name = company_name
