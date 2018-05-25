from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

"""
    Extending User Model Using a Custom Model Extending AbstractBaseUser
"""


# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, first_name, last_name, password=None):
        """
            Creates and saves a User with the given email, date of
            birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, first_name, last_name, password):
        """
            Creates and saves a superuser with the given email, date of
            birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    # used as username
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    # date_of_birth
    date_of_birth = models.DateField()

    # first_name
    first_name = models.CharField(
        'first_name',
        max_length=100
    )

    # last_name
    last_name = models.CharField(
        'last_name',
        max_length=100
    )

    # activate user
    is_active = models.BooleanField(
        default=True
    )

    # admin permission
    is_admin = models.BooleanField(
        default=False
    )

    # customize Manager
    objects = MyUserManager()

    # username field
    USERNAME_FIELD = 'email'

    # required field
    REQUIRED_FIELDS = ['date_of_birth', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email

    def __unicode__(self):
        return str(self)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
