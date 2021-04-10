from django import forms
from django.forms import ModelForm, ValidationError

from .models import CustomUser, AnonymousUser, AnonymousMessage


class RegistrationForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = [
                'username',
                'password',
                'confirm_password',
                'email',
                'company_name',
                'phone',
                'first_name',
                'last_name',
            ]

    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Логин'
        self.fields['company_name'].label = 'Название компании'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия (Можно оставить пустым)'
        self.fields['email'].label = 'Электронный адресс'
        self.fields['phone'].label = 'Номер телефона (Можно оставить пустым)'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите Пароль'

    def clean_email(self):
        email = self.cleaned_data['email']

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Пользователь с такой почтой ({email} уже существует!)')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']

        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с таким логином ({username}) существует!')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 8:
            raise forms.ValidationError('Пароль должен быть не короче 8 символов!')

        return password


class LoginForm(ModelForm):

    class Meta:

        model = CustomUser
        fields = [
                'username',
                'password',
            ]

    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с логином "{username}" не найден в системе.')

        user = CustomUser.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')

        return self.cleaned_data


class AnonymousUserForm(ModelForm):
    class Meta:
        model = AnonymousUser
        fields = [
                'name',
                'email',
                'phone',
                'company',
            ]

    def clean(self):
        name = self.cleaned_data['name']
        if not name:
            msg = 'Необходимо указать Ваше имя'
            raise forms.ValidationError(msg)
        return self.cleaned_data


class AnonymousMessageForm(ModelForm):
    class Meta:
        model = AnonymousMessage
        fields = [
                'subject',
                'message_text',
            ]

    def clean(self):
        message_text = self.cleaned_data['message_text']
        if not message_text:
            msg = 'Введите текст сообщения'
            raise forms.ValidationError(msg)
        return self.cleaned_data
