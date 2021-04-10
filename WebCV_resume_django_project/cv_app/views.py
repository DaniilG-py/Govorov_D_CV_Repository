from django.db import transaction
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from .forms import RegistrationForm, LoginForm, AnonymousUserForm, AnonymousMessageForm

from .models import WorkingExperience, EducationExperience, CustomUser, AnonymousUser, AnonymousMessage


class BaseView(View):

    def get(self, request, *args, **kwargs):
        work_exp = WorkingExperience.objects.all()
        educ_exp = EducationExperience.objects.all()
        form_user = AnonymousUserForm
        form_mess = AnonymousMessageForm

        context = {
                'work_exp': work_exp,
                'educ_exp': educ_exp,
                'form_user': form_user,
                'form_mess': form_mess,
            }
        return render(request, 'index.html', context)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form_user = AnonymousUserForm(request.POST or None)
        form_mess = AnonymousMessageForm(request.POST or None)

        if form_user.is_valid():
            new_anonymous_user = form_user.save(commit=False)

            new_anonymous_user.email = form_user.cleaned_data['email']
            new_anonymous_user.company = form_user.cleaned_data['company']
            new_anonymous_user.save()

        if form_mess.is_valid():
            new_anonymous_message = form_mess.save(commit=False)
            anonymous_user = AnonymousUser.objects.get(id=new_anonymous_user.id)
            new_anonymous_message.sender = anonymous_user
            new_anonymous_message.subject = form_mess.cleaned_data['subject']
            new_anonymous_message.message_text = form_mess.cleaned_data['message_text']
            new_anonymous_message.save()

            anonymous_message = AnonymousMessage.objects.get(sender=new_anonymous_message.sender)
            new_anonymous_user.message = anonymous_message
            new_anonymous_user.save()

            messages.add_message(request, messages.INFO, 'Сообщение отправлено! Большое спасибо!')

            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/')


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

        return render(request, 'auth_to_write_mess.html', context)
