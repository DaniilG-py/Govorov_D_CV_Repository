from django.db import transaction
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from .forms import RegistrationForm, LoginForm, SendMessageForm

from .models import CustomUser, UserMessage


class RegistrationView(View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {'form': form}

        return render(request, 'registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)

        if form.is_valid():

            CustomUser.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    # password=form.check_password(),
                    phone=form.cleaned_data['phone'],
                    company_name=form.cleaned_data['company_name'],
                    first_name=form.cleaned_data['first_name'],
                )

            user = authenticate(
                    username = form.cleaned_data['username'],
                    password = form.cleaned_data['password'],
                )
            login(request, user)

            return HttpResponseRedirect('/')

        context = {'form': form}

        return render(request, 'registration.html', context)


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {'form': form}

        return render(request, 'login.html', context)


    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)

                return HttpResponseRedirect('/')

        context = {'form': form}

        return render(request, 'index.html', context)


class WriteMessageView(View):
    """
    View for message sending.
    """

    def get(self, request, *args, **kwargs):
        form = SendMessageForm(request.POST or None)
        context = {'form': form}
        return render(request, 'send_message.html', context)


class SendMessageView(View):

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = SendMessageForm(request.POST or None)
        user = CustomUser.objects.get(username=request.user)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender_name = user
            new_message.title = form.cleaned_data['title']
            new_message.text = form.cleaned_data['text']

            new_message.save()

            messages.add_message(request, messages.INFO, 'Сообщение отправлено! Большое спасибо!')

            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/write_message/')


class AuthToWriteView(View):

    def get(self, request, *args, **kwargs):
        return render(request , 'auth_to_write_mess.html')
