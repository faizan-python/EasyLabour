from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.validators import RegexValidator
from django.db import models

from django.utils import timezone
from enum import Enum


class UserManager(BaseUserManager):

    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The given phone number must be set')

        now = timezone.now()
        user = self.model(phone_number=phone_number,
                          is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        superuser = self.create_user(phone_number, password, **extra_fields)
        superuser.is_staff = True
        superuser.is_active = True
        superuser.is_superuser = True
        superuser.is_verified = True
        superuser.role = "Super User"
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):

    class UserTypes(Enum):
        AGENT = 'Agent'
        NORMAL_USER = 'Normal User'
        SUPER_USER = 'Super User'

        @classmethod
        def as_tuple(cls):
            return ((item.value, item.name.replace('_', ' ')) for item in cls)

    email = models.EmailField(blank=True, null=True)

    first_name = models.CharField(max_length=80, blank=True, null=True)
    middle_name = models.CharField(max_length=80, blank=True, null=True)
    last_name = models.CharField(max_length=80, blank=True, null=True)

    full_name = models.CharField(max_length=80, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    username = models.CharField(max_length=50, blank=True, null=True)
    date_joined = models.DateTimeField(
        auto_now_add=True,
        null=False,
        editable=True,
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format:' \
        ' '+999999999'. Up to 15 digits allowed.")

    phone_number = models.CharField(validators=[phone_regex], max_length=15,
                                    null=True, unique=True, blank=True)
    country_code = models.CharField(max_length=6,
                                    null=True, blank=True)
    role = models.CharField(
        null=True, max_length=50,
        choices=UserTypes.as_tuple(),
        default=UserTypes.NORMAL_USER.value
    )

    USERNAME_FIELD = 'phone_number'

    objects = UserManager()

    # Returns full name of user
    def get_full_name(self):
        return self.full_name

    # Returns short name of user.
    def get_short_name(self):
        return self.full_name
