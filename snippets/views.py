from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from rest_framework import generics


from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer


# Create your views here.

class SnippetListView(generics.ListCreateAPIView):
    """
        List all code snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, update or delete a code snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
