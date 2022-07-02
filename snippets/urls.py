from django.urls import path
from .views import SnippetListView, SnippetDetailView, UserListView, UserDetailView, api_root,\
    SnippetHighlightView
from rest_framework.urlpatterns import format_suffix_patterns
app_name = 'snippets'

urlpatterns = [
    path('', api_root),
    path('snippets/', SnippetListView.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', SnippetDetailView.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', SnippetHighlightView.as_view(), name='snippet-highlight'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),


]

urlpatterns = format_suffix_patterns(urlpatterns)