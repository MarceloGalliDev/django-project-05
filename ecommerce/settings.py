from pathlib import Path
from django.contrib.messages import constants


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-_n%n$d9&t2b3&j*hzvrg40os0nl@x-vxynh&^dgi*)2n1xa^ou'

DEBUG = True

ALLOWED_HOSTS: list[str] = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'produtos',
    'pedidos',
    'perfils',
    
    # TODO somente desenvolvimento, apagar no deploy
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # TODO somente desenvolvimento, apagar no deploy
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'base_templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# Incluir a barra antes do 'static/'
STATIC_URL = '/static/'
# Usado para pasta destino do collectstatic do Django
STATIC_ROOT = BASE_DIR / 'static'

# Aqui incluimos o caminho do global static para o Django é uma lista logo pode ter mais de uma pasta # noqa
STATICFILES_DIRS = [
    BASE_DIR / 'base_static',
]

# configurando imagens na parte static
MEDIA_URL = '/media/'
# Usado para pasta destino do collectstatic do Django
MEDIA_ROOT = BASE_DIR / 'media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Flash msgs, classes CSS a serem usadas
MESSAGE_TAGS = {
    constants.DEBUG: 'message-debug',
    constants.ERROR: 'message-error',
    constants.INFO: 'message-info',
    constants.SUCCESS: 'message-success',
    constants.WARNING: 'message-warning',
}

# Configurando os cookies
#tempo de duração: 60s * 60min * 24h * 1d
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7

# salvar a cada requisição
# como esta false teremos que salvar a session manualmente
SESSION_SAVE_EVERY_REQUEST = False

# serializer padrão JSON
# SESSION_SERIALIZER = 'django.contrib.session.serializer.PickleSerializer'


# TODO somente desenvolvimento, apagar no deploy
INTERNAL_IPS = [
    '127.0.0.1',
]