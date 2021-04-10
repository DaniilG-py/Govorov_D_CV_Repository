from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
                BaseView,
                RegistrationView,
                LoginView,
            )


urlpatterns = [
        path('', BaseView.as_view(), name='main-page'),
        path('registration/', RegistrationView.as_view(), name='registration'),
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    ]
