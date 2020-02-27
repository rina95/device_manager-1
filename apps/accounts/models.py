import uuid

from datetime import timedelta
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinLengthValidator
from lib.validators import *
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from lib.validators import validate_user_code_in_list

class MyUserManager(BaseUserManager):
  def _create_user(self, name, code, password, is_staff, is_superuser, **extra_fields):
    """
    Create and save an User with the given name, code, password.
    :param password: string
    :param user_name: string
    :param code: string
    :param is_staff: boolean
    :param is_superuser: boolean
    :param extra_fields:
    :return: User
    """
    now = timezone.now()
    user = self.model(name=name,
                      code=code,
                      last_login=now,
                      is_staff=is_staff,
                      is_active=True,
                      is_superuser=is_superuser,
                      updated_at=now,
                      created_at=now, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, name, code, password, **extra_fields):
    """
    Create and save an User with the given name, password and code.
    :param name: string
    :param code: string
    :param password: string
    :param extra_fields:
    :return: User
    """

    return self._create_user(name, code, password, is_staff=False, is_superuser=False, **extra_fields)

  def create_superuser(self, name, code, password=None, **extra_fields):
      """
      Create a super user.
      :param name: string
      :param code: string
      :param password: string
      :param extra_fields:
      :return: User
      """
      return self._create_user(name, code, password, is_staff=True, is_superuser=True, **extra_fields)

class User(AbstractBaseUser):
  """
  Model that represents an user.
  To be active, the user must register.
  """
  # we want primary key to be called id so need to ignore pytlint
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # pylint: disable=invalid-name

  name = models.CharField(_('full name'), max_length=50)
  code = models.CharField(_('employee code'),
                          unique=True,
                          max_length=50,
                          validators=[validate_user_code_in_list])

  password = models.CharField(_('password'),
                              max_length=128,
                              validators=[MinLengthValidator(8)])
  is_staff = models.BooleanField(_('staff status'), default=False)
  is_superuser = models.BooleanField(_('superuser status'), default=False)
  is_active = models.BooleanField(_('active'), default=True)

  created_at = models.DateTimeField(_('date created'), auto_now_add=True)
  updated_at = models.DateTimeField(_('date updated'), auto_now=True)

  USERNAME_FIELD = 'code'
  REQUIRED_FIELDS = ['name']

  # objects = MyUserManager()
  class Meta:
    ordering = ['name']

  def __str__(self):
    """
    Unicode representation for an user model.
    :return: string
    """
    return self.name
  
  # def clean(self):
  #   self.code = validate_user_code_in_list(self.code)

  # def save(self):
  #   self.full_clean() # calls self.clean() as well cleans other fields
  #   return super(User, self).save(*args, **kwargs)

  def get_full_information(self):
    """
    Return the first_name plus the last_name, with a space in between.
    :return: string
    """
    return "{0} - {1}".format(self.name, self.code)

  def get_code(self):
    """
    Return the employee code.
    :return: string
    """
    return self.code
