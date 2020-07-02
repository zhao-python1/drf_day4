from django.db import models

# Create your models here.

from  django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=10,unique=True)
    class Meta:
        db_table = "new_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name
    def __str__(self):
            return self.username

