from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework import generics


from .models import Snippet
from .serializers import SnippetSerializer


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class SnippetListView(generics.ListCreateAPIView):
    """
        List all code snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


@method_decorator(csrf_exempt, name='dispatch')
class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, update or delete a code snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
