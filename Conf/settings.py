
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p2t9^r$0v!szpa5qae9ck-uwkme=k7!e)@c_o!%b2t^8*38b6h'

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

    # django apps
    'jazzmin',
    'rest_framework',
    'rest_framework_simplejwt',
    'modeltranslation',

    # my apps
    'users.apps.UsersConfig',
    'outher.apps.OutherConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'allauth.account.middleware.AccountMiddleware',  # Add this line if missing
]

ROOT_URLCONF = 'Conf.urls'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 25,

    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {
    "site_title": "Foydali Havolalar",
    "site_brand": "Fanlar Akademiyasi",
    "site_logo": "Бабочка.jpg",
    "welcome_sign": "Xush Kelibsiz",
    "copyright": "Archaeology",
    # "search_model": ["app.model_name"],

    "topmenu_links": [
        {"model": "auth.User"},
        # {"model": "auth.Group"},

        # {"name": "Foydali Havolalar", "url": "foydali_havolalar"},
        # {"name": "Hikmatli Sozlar", "url": "hikmatli_sozlar"},
        # {"name": "Hujjatlar", "url": "hujjatlar"},
        # {"name": "Ishtirokchilar", "url": "ishtirokchilar"},
        # {"name": "Jadidlar", "url": "jadidlar"},
        # {"name": "Manbalar", "url": "manbalar"},
        # {"name": "Sahifalar", "url": "sahifalar"},
        # {"name": "Slayder", "url": "slayder"},
        # {"name": "Tadbirlar", "url": "tadbirlar"},
        # {"name": "Tanlovlar", "url": "tanlovlar"},
    ],

    "navigation_expanded": False,

    "hide_apps": ['auth'],

    "show_ui_builder": True,

    "changeform_format": "collapsible",

    # "usermenu_links": [
    # {"name": "Profile", "url": "profile"},
    # {"name": "Logout", "url": "logout"},
    # {"name": "Login", "url": "login"},
    # {"name": "Signup", "url": "signup"},

    #     ]

}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}

AUTH_USER_MODEL = "users.CustomUser"


LANGUAGES = [
    ('uz', ('Uzbek')),
    ('en', ('English')),
    ('ru', ('Russian')),
]


MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'



#? pip install phonenumbers
#? pip install django-phonenumber-field  KERAK BOLIB QOLADI!

