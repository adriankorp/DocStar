from django.db.models import CharField, DateTimeField, ForeignKey, Model, DO_NOTHING

from DocStar.database_models.user import User


class Document(Model):
    doc_id = CharField(max_length=128)
    user_id = ForeignKey(User, on_delete=DO_NOTHING)
    status = CharField(max_length=128)
    create_date = DateTimeField(auto_now_add=True)
    submit_date = DateTimeField(auto_now_add=False)
    complete_date = DateTimeField(auto_now_add=False)
    subject = CharField(max_length=128)
    user_text = CharField(max_length=128)
    # TODO: check how to store pdf
    # pdf_address =
