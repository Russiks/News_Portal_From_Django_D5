"""
Django settings for NewsPortal project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vlj7e#ksmj5v$$67l_9ufyfkhzr+&%8k2u%-hi(rm8^l%#vx=9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',  # Приложение поддержки авторизации
    'django.contrib.contenttypes',
    'django.contrib.sessions',  # Управление сессиями. В обработке каждого запроса (переменная request) вы можете
    # получить доступ к данным сессии (которые хранятся на сервере) и каким-то образом манипулировать ими.
    'django.contrib.messages',
    'django.contrib.staticfiles',  # Приложение для работы с "статическими файлами"(CSS, Java и т.д)

    # Список пользовательских приложений, создается разработчиком
    'django.contrib.sites',
    'django.contrib.flatpages',
    'newsapp',  # newsapp - основное приложение новостного портала
    'django_filters',  # Приложение для подключения фильтров
    # Подключение приложений из "allauth"
    'allauth',  # Обязательное приложение allauth
    'allauth.account',  # Обязательное приложение allauth
    'allauth.socialaccount',  # Обязательное приложение allauth
    'allauth.socialaccount.providers.yandex',  # Необходимо для реализации регистрации через провайдер "Yandex"
]

SITE_ID = 1  # Идентификатор (целое число) текущего сайта в таблице базы данных django_site. Может использоваться
# приложениями для связывания своих данных с определенными сайтами и, таким образом, для управления контентом
# нескольких сайтов в единой базе данных.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'NewsPortal.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Задаем путь к папке с шаблонами, где Django будет их искать
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` обязательно нужен этот процессор
                'django.template.context_processors.request',  # контекстный процессор, нужен для allauth.
            ],
        },
    },
]

# Добавляем бэкенды аутентификации:
AUTHENTICATION_BACKENDS = [
    # Необходимо войти в систему под именем пользователя в админке Django, независимо от `allauth`:
    'django.contrib.auth.backends.ModelBackend',  # Встроенный бэкенд Django, реализующий аутентификацию по username

    # Специальные методы аутентификации `allauth`, такие, как вход по электронной почте:
    'allauth.account.auth_backends.AuthenticationBackend',  # Бэкенд аутентификации, предоставленный пакетом allauth:
    # нам нужно «включить» аутентификацию как по username, так и специфичную по email или сервис-провайдеру.
]

WSGI_APPLICATION = 'NewsPortal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройка STATICFILES_DIRS указывает каталоги, которые проверяются на наличие статических файлов.
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# LOGIN_URL = '/error_create/'
LOGIN_REDIRECT_URL = '/post'  # страница, на которую перенаправляется пользователь после успешного входа на сайт,

ACCOUNT_EMAIL_REQUIRED = True  # Регистрация по электронной почте обязательно
ACCOUNT_UNIQUE_EMAIL = True  # Регистрация по уникальной электронной почте
ACCOUNT_USERNAME_REQUIRED = False  # Регистрация по username не обязательна
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # Аутентификация будет происходить посредством электронной почты
ACCOUNT_EMAIL_VERIFICATION = 'none'  # Верификация электронной почты отсутствует.
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}  # Чтобы allauth распознал нашу форму как ту,
# что должна выполняться вместо формы по умолчанию