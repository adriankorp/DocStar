from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, UserCreationForm
)
from django.db.transaction import atomic
from django.forms import CharField, Form, Textarea
from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['email', 'first_name', 'last_name']

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        profile = Profile(user=result)
        if commit:
            profile.save()
        return result
