from django.urls import path
from .views import SnippetListView
app_name = 'snippets'

urlpatterns = [
    path('snippets/', SnippetListView.as_view(), name='list'),
]