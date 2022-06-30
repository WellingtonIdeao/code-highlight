from django.urls import path
from .views import SnippetListView, SnippetDetailView
from rest_framework.urlpatterns import format_suffix_patterns
app_name = 'snippets'

urlpatterns = [
    path('snippets/', SnippetListView.as_view(), name='list'),
    path('snippets/<int:pk>/', SnippetDetailView.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)