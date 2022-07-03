from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.


class SnippetViewSet(viewsets.ModelViewSet):
    """
       This viewset automatically provides `list`, `create`, `retrieve`,
       `update` and `destroy` actions.

       Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
        This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
