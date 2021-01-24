from django.db import models

# Create your models here.
from django.db.models import Model, CharField, ForeignKey, DO_NOTHING, DateTimeField

from app_accounts.models import Profile


class Document(Model):
    doc_id = CharField(max_length=128)
    user_id = ForeignKey(Profile, on_delete=DO_NOTHING)
    status = CharField(max_length=128)
    create_date = DateTimeField(auto_now_add=True)
    submit_date = DateTimeField(auto_now_add=False)
    complete_date = DateTimeField(auto_now_add=False)
    subject = CharField(max_length=128)
    user_text = CharField(max_length=128)
    # TODO: check how to store pdf
    # pdf_address =


class Signature(Model):
    doc_id = ForeignKey(Document, on_delete=DO_NOTHING)
    signature_id = CharField(max_length=128)
    signer_email = CharField(max_length=128)
    signed_on = DateTimeField(auto_now_add=False)
    status = CharField(max_length=20)