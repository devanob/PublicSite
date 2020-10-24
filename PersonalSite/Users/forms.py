from django.contrib import admin

from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm



class CustomUserEditForm(UserEditForm):
    git_hub_account = forms.CharField(required=True, label=_("Git Hub Handle"))


class CustomUserCreationForm(UserCreationForm):
    git_hub_account = forms.CharField(required=True, label=_("Git Hub Handle"))
