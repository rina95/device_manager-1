from rest_framework import serializers
from apps.accounts.models import User
from lib.validators import *
from django.utils.translation import gettext_lazy as _

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'code', 'name', 'created_at', 'updated_at')

class UserRegistrationSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('code', 'name', 'password', 'created_at', 'updated_at')
    extra_kwargs =  {
                      'password': {'write_only': True},
                    }

  def create(self, validated_data):
    """
    Create the object.
    :param validated_data: string
    """
    user = User.objects.create(**validated_data)
    user.set_password(validated_data['password'])
    user.save()
    return user
