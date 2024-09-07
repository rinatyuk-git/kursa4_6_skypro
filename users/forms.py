from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models import BooleanField

from users.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
            "password1",
            "password2",
        )


class UserProfileForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = (
            "email",
            "phone",
            "country",
        )
