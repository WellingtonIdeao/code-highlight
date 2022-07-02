from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.

class SnippetListView(generics.ListCreateAPIView):
    """
        List all code snippets. Only authenticated user can also create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve a code snippet. Only an authenticated user can also Update or delete a code snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class UserListView(generics.ListAPIView):
    """
         List all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """
        Retrieve a user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
