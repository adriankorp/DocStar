from django.db.models import CharField, Model, BooleanField, AutoField, OneToOneField, DO_NOTHING
from django.contrib.auth.models import User


class Profile(Model):
    user = OneToOneField(User, on_delete=DO_NOTHING, primary_key=True)
    password = CharField(max_length=128)
    is_pro = BooleanField(default=False)
    name = CharField(max_length=128)
    surname = CharField(max_length=128)
    user_id = AutoField(primary_key=True)
