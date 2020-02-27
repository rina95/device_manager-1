from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from lib.utils import AtomicMixin

from apps.accounts.models import User
from apps.accounts.serializers import UserRegistrationSerializer, UserSerializer

class UserRegisterView(AtomicMixin, CreateModelMixin, GenericAPIView):
  serializer_class = UserRegistrationSerializer
  authentication_classes = ()

  def post(self, request):
    """User registration view."""
    return self.create(request)
