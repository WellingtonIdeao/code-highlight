from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from .models import Snippet
from .serializers import SnippetSerializer


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class SnippetListView(View):
    """
        List all code snippets, or create a new snippet.
    """
    def get(self, request, *args, **kwargs):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class SnippetDetailView(View):

    def get(self, request, *args, **kwargs):
        snippet = get_object_or_404(Snippet, pk=kwargs['pk'])
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    def put(self, request, *args, **kwargs):
        snippet = get_object_or_404(Snippet, pk=kwargs['pk'])
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        snippet = get_object_or_404(Snippet, pk=kwargs['pk'])
        snippet.delete()
        return HttpResponse(status=204)







