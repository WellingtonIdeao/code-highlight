from django.urls import path
from .views import SnippetListView, SnippetDetailView
app_name = 'snippets'

urlpatterns = [
    path('snippets/', SnippetListView.as_view(), name='list'),
    path('snippets/<int:pk>/', SnippetDetailView.as_view(), name='detail'),
]