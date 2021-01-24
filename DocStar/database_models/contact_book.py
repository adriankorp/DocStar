from django.db.models import CharField, DateTimeField, ForeignKey, Model, DO_NOTHING, EmailField

from DocStar.database_models.profile import Profile


class ContactBook(Model):
    user_id = ForeignKey(User, on_delete=DO_NOTHING)
    name = CharField(max_length=128)
    surname = CharField(max_length=128)
    email = EmailField()



