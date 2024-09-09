import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    'django-insecure-(psu(!hh8#^xtlnt=%+p%(47n9ju*+8=xabgwfxtz-4lxkcx=_'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += ['users', 'conhecimento']

INSTALLED_APPS += [
    'crispy_forms',
    'crispy_bootstrap5',
    'rolepermissions',
    'ckeditor',
    'ckeditor_uploader',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BaseConhecimento.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'BaseConhecimento.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

THOUSAND_SEPARATOR = ('.',)
USE_THOUSAND_SEPARATOR = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.Users'

LOGIN_URL = 'auth/login/'

LOGIN_REDIRECT_URL = 'index'

LOGOUT_REDIRECT_URL = 'auth/login/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

####################################
##  CKEDITOR CONFIGURATION ##
####################################

CKEDITOR_JQUERY_URL = (
    'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
)


CKEDITOR_UPLOAD_PATH = 'media/uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_RESTRICT_BY_USER = False
CKEDITOR_ALLOW_NONIMAGE_FILES = True

CKEDITOR_CONFIGS_5 = {
    'default': {
        'toolbar': 'Full',
        'height': 900,
        'width': 'auto',
        'extraPlugins': ','.join(
            [
                'uploadimage',  # Upload de imagem
                'autogrow',  # Redimensionamento automático do editor
                'codesnippet',  # Blocos de código com destaque
                'youtube',  # Inserção de vídeos do YouTube
                'widget',  # Widgets customizados
                'dialog',  # Janelas de diálogo
                'lineutils',  # Ferramentas para manipular blocos/linhas
                'clipboard',  # Funções de copiar/colar
                'pastefromword',  # Cola conteúdo do Word com formatação
                'liststyle',  # Estilos para listas
                'contextmenu',  # Menu de contexto customizado
                'div',  # Divisores (DIV blocks)
                'font',  # Alteração de fontes
                'colorbutton',  # Seleção de cores
                'justify',  # Justificação de texto
                'indentblock',  # Indentação de blocos
                'image2',  # Plugin avançado de imagens
                'blockquote',  # Citações em bloco
                'find',  # Pesquisa dentro do texto
                'smiley',  # Inserção de emoticons
                'forms',  # Suporte a formulários
                'flash',  # Inserção de conteúdo Flash
                'iframe',  # Inserção de iframes
                'link',  # Inserção de links
                'table',  # Manipulação de tabelas
                'horizontalrule',  # Linha horizontal
                'templates',  # Templates predefinidos
                'specialchar',  # Inserção de caracteres especiais
            ]
        ),
        'toolbar_Full': [
            {
                'name': 'document',
                'items': [
                    'Source',
                    '-',
                    'NewPage',
                    'Preview',
                    'Print',
                    '-',
                    'Templates',
                ],
            },
            {
                'name': 'clipboard',
                'items': [
                    'Cut',
                    'Copy',
                    'Paste',
                    'PasteText',
                    'PasteFromWord',
                    '-',
                    'Undo',
                    'Redo',
                ],
            },
            {
                'name': 'editing',
                'items': ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt'],
            },
            {
                'name': 'forms',
                'items': [
                    'Form',
                    'Checkbox',
                    'Radio',
                    'TextField',
                    'Textarea',
                    'Select',
                    'Button',
                    'ImageButton',
                    'HiddenField',
                ],
            },
            '/',
            {
                'name': 'basicstyles',
                'items': [
                    'Bold',
                    'Italic',
                    'Underline',
                    'Strike',
                    'Subscript',
                    'Superscript',
                    '-',
                    'RemoveFormat',
                ],
            },
            {
                'name': 'paragraph',
                'items': [
                    'NumberedList',
                    'BulletedList',
                    '-',
                    'Outdent',
                    'Indent',
                    '-',
                    'Blockquote',
                    'CreateDiv',
                    '-',
                    'JustifyLeft',
                    'JustifyCenter',
                    'JustifyRight',
                    'JustifyBlock',
                    '-',
                    'BidiLtr',
                    'BidiRtl',
                ],
            },
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {
                'name': 'insert',
                'items': [
                    'Image',
                    'Flash',
                    'Table',
                    'HorizontalRule',
                    'Smiley',
                    'SpecialChar',
                    'PageBreak',
                    'Iframe',
                ],
            },
            '/',
            {
                'name': 'styles',
                'items': ['Styles', 'Format', 'Font', 'FontSize'],
            },
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
        ],
    }
}

###################################
