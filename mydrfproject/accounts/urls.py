# accounts/urls.py

from django.urls import path, include

from .views import register_user, user_login, ParagraphViewSet, get_all_users


urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('users/', get_all_users, name='get-all-users'),  # Add URL for retrieving all users
    
    path('paragraphs/', ParagraphViewSet.as_view({'post': 'create'}), name='create-paragraph'),
    path('search-paragraphs/', ParagraphViewSet.as_view({'get': 'search_paragraphs'}), name='search-paragraphs'),
]