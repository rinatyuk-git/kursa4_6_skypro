from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models import BooleanField
from django.forms import ModelForm

from users.models import User


# class StyleFormMixin:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             if isinstance(field, BooleanField):
#                 field.widget.attrs["class"] = "form-check-input"
#             else:
#                 field.widget.attrs["class"] = "form-control"


class StyleFormMixin:

    def add_bootstrap_classes(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({"class": "form-control"})
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({"class": "form-control"})
            elif isinstance(field.widget, forms.FileInput):
                field.widget.attrs.update({"class": "form-control-file"})
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({"class": "form-control"})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({"class": "form-check-input"})
            elif isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs.update({"class": "form-check-input"})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_bootstrap_classes()


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


class UserModeratorForm(StyleFormMixin, ModelForm):

    class Meta:
        model = User
        fields = ('email', 'is_active',)
