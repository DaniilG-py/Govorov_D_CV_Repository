from django.urls import path

from .views import LoginAPIView, UserViewSet


urlpatterns = [
        path('users/api-token-auth/', LoginAPIView.as_view(), name='api-token-auth'),
        path('users/<str:pk>/', UserViewSet.as_view(), name='users_edit'),
        path('users/', UserViewSet.as_view(), name='users'),

    ]
