from django.db.models import CharField, DateTimeField, ForeignKey, Model, DO_NOTHING

from DocStar.database_models.document import Document


class Signature(Model):
    doc_id = ForeignKey(Document, on_delete=DO_NOTHING)
    signature_id = CharField(max_length=128)
    signer_email = CharField(max_length=128)
    signed_on = DateTimeField(auto_now_add=False)
    status = CharField(max_length=20)

