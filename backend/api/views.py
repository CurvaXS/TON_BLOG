from django.shortcuts import render

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]


# class TestViewSet(viewsets.ViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = {
#         'test': 'test',
#         'test2': 'test2',
#         'test3': 'test3',
#         'test4': 'test4',
#     }
#     # serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]