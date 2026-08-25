import os
from pathlib import Path

import dj_database_url

# Load local env.py if it exists
if os.path.isfile('env.py'):
    import env

# -------------------
# BASE DIRECTORY
# -------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------
# SECURITY
# -------------------
SECRET_KEY = os.environ.get('SECRET_KEY', '')

DEBUG = os.environ.get("DEBUG", "True").lower() == "true"

ALLOWED_HOSTS = [
    'presentation-28tx.onrender.com',
    'localhost',
    '127.0.0.1',
]

# -------------------
# CSRF
# -------------------
CSRF_TRUSTED_ORIGINS = [
    'https://presentation-28tx.onrender.com/',
]

# -------------------
# APPLICATIONS
# -------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Cloudinary
    'cloudinary_storage',
    'cloudinary',
]
if DEBUG:
    INSTALLED_APPS += [
        'django_browser_reload',
    ]


# -------------------
# MIDDLEWARE
# -------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
if DEBUG:
    MIDDLEWARE += [
        'django_browser_reload.middleware.BrowserReloadMiddleware',
    ]

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

# -------------------
# URLS
# -------------------
ROOT_URLCONF = 'presentation.urls'
WSGI_APPLICATION = 'presentation.wsgi.application'

# -------------------
# TEMPLATES
# -------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# -------------------
# DATABASE
# -------------------
ENVIRONMENT = os.environ.get("ENVIRONMENT", "local")

if ENVIRONMENT == "local":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": dj_database_url.config(
            default=os.environ["DATABASE_URL"],
            conn_max_age=600,
            ssl_require=True,
        )
    }

# -------------------
# PASSWORD VALIDATION
# -------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------
# INTERNATIONALIZATION
# -------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# -------------------
# STATIC
# -------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# -------------------
# MEDIA (CLOUDINARY)
# -------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.environ.get("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.environ.get("CLOUDINARY_API_KEY"),
    "API_SECRET": os.environ.get("CLOUDINARY_API_SECRET"),
}


# -------------------
# DEFAULT AUTO FIELD
# -------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"