# Create your models here.
from django.contrib.auth.models import AbstractUser,PermissionsMixin
import uuid
from django.db import models
from wagtail.snippets.models import register_snippet
##Register Model As Snippet So We Can Use The Snippet Chooser
@register_snippet
class User(AbstractUser): 
    email = models.EmailField(unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    git_hub_account = models.TextField(blank=True, null=True)
    git_api_key = models.TextField(blank=True, null=True)
