from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm  # Базовая форма, позволяющая создать пользователя (в ней реализованы
# все валидации и проверки)
from django.contrib.auth.models import Group


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)  # Вызываем метод класса-родителя, чтобы были выполнены необходимые проверки и
        # сохранение в модель User
        normal_users = Group.objects.get(name='normal users')  # Получаем объект модели группы normal users
        # normal_users.user_set.add(user)  # через атрибут user_set, возвращающий список всех пользователей этой группы
        # и добавляем нового пользователя в эту группу
        user.groups.add(normal_users)  # Добавляем нового пользователя в эту группу
        return user  # Обязательным требованием метода save() является возвращение объекта модели User по итогу
        # выполнения функции


# class SignUpForm(UserCreationForm):
#     # Стандартные поля формы
#     email = forms.EmailField(label="Email")
#     first_name = forms.CharField(label="Имя")
#     last_name = forms.CharField(label="Фамилия")
#
#     # Расширение стандартных форм
#     class Meta:
#         model = User
#         fields = (
#             "username",
#             "first_name",
#             "last_name",
#             "email",
#             "password1",
#             "password2",
#         )