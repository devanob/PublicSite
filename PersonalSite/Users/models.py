# Create your models here.
from django.contrib.auth.models import AbstractUser,PermissionsMixin
import uuid
from django.db import models

class User(AbstractUser): 
    email = models.EmailField(unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)