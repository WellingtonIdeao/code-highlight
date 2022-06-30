from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Snippet
from .serializers import SnippetSerializer


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class SnippetListView(APIView):
    """
        List all code snippets, or create a new snippet.
    """
    def get(self, request, *args, **kwargs):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class SnippetDetailView(APIView):
    """
        Retrieve, update or delete a code snippet.
    """
    def get_object(self, pk=None):
        if pk is None:
            pk = self.kwargs.get('pk')
        obj = Snippet.objects.get(pk=pk)
        return obj

    def get(self, request, *args, **kwargs):
        try:
            snippet = self.get_object()
        except Snippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        try:
            snippet = self.get_object()
        except Snippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            snippet = self.get_object()
        except Snippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        snippet = self.get_object()
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
