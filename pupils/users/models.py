from django.db import models
from django.contrib.auth.models import User

class Progenitor(models.Model):
    user = models.ForeignKey(User, unique=True)
