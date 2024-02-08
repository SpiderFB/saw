from django.db import models
import uuid
from products.models import productdb

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class NewUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):

        return self.create_user(email, password, **extra_fields)

class NewUser(AbstractBaseUser, PermissionsMixin):
    
    user_uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    email = models.EmailField('email address', unique=True)
    phone = models.IntegerField(blank = True, null = True)
    age = models.IntegerField(blank = True, null = True)
    # fav_product = models.ForeignKey(productdb, on_delete=models.CASCADE, blank=True, null=True)
    fav_product = models.ManyToManyField(productdb, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = NewUserManager()
    
    def __str__(self):
        return self.email