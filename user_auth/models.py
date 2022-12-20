from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

class User(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=120, null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=150, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # Usually this field is a ForeignKey with master data of country
    country = models.CharField(max_length=150, null=True, blank=True)
    role = models.ForeignKey(
        'UserRole', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.username}"
    
    
    
    
class UserRole(models.Model):
    """
    Model for storing user roles.
    """

    name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.name
