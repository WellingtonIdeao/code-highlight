from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'users': reverse('user-list', request=request, format=format),
            'snippets': reverse('snippet-list', request=request, format=format)
        }
    )


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


class SnippetHighlightView(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
