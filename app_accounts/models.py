from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Model, OneToOneField, DO_NOTHING, CharField, BooleanField, AutoField, ForeignKey, \
    EmailField


class Profile(Model):
    user = OneToOneField(User, on_delete=DO_NOTHING)
    is_pro = BooleanField(default=False)
    name = CharField(max_length=128)
    surname = CharField(max_length=128)


class ContactBook(Model):
    user_id = ForeignKey(Profile, on_delete=DO_NOTHING)
    name = CharField(max_length=128)
    surname = CharField(max_length=128)
    email = EmailField()


