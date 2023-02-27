from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    """Custom User Manager for User Model"""

    def create_user(self, email, first_name, last_name, phone_no, password=None):
        """Create, save and return a new user"""
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_no=phone_no,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, phone_no, password):
        """Create, save and return a new super user"""
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_no=phone_no,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Defines custom user model"""

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    objects = UserManager()
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_no"]
    USERNAME_FIELD = "email"

    class Meta:
        ordering = ["-updated_on", "-created_on"]

    def __str__(self):
        return self.email
