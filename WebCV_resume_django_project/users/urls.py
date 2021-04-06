from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
                    RegistrationView,
                    LoginView,
                    WriteMessageView,
                    SendMessageView,
                    AuthToWriteView,
                )

urlpatterns = [
        path('registration/', RegistrationView.as_view(), name='registration'),
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
        path('write_message/', WriteMessageView.as_view(), name='write_message'),
        path('send_message/', SendMessageView.as_view(), name='send_message'),
        path('need_auth/', AuthToWriteView.as_view(), name='auth_to_write_mess'),
    ]
