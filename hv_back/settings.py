"""
Django settings for hv_back project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)6cv^nunnw2f864i*#i7g1la@%vshwx8k4z9^dt(fsy+_)e-b!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#배포 변경 추후 우리 도메인만 
ALLOWED_HOSTS = ['https://main.jinttoteam.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'mainpage',
    'landing',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'core',
    'storages'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hv_back.urls'

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

WSGI_APPLICATION = 'hv_back.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "jintto",
        "USER":"jintto",
        "PASSWORD":"jintto1130",
        "HOST":"database-new-backenddb.ctcha5snygzq.us-east-1.rds.amazonaws.com",
        "PORT":"3306"
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
CORS_ALLOWED_ORIGINS = [
    "https://front.jinttoteam.com"  # React 앱이 실행되는 주소
]

CORS_ALLOW_CREDENTIALS = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    'JWT_SECRET_KEY': 'Lw5Syaog9lZb32MpP4G117_e1AXKCOZyrr9MtHj40Cs',  # 생성된 비밀 키로 교체
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',  # 필요에 따라 변경 가능
    },
}

MEDIA_ROOT = BASE_DIR/"media"
MEDIA_URL = "/media/"

AWS_ACCESS_KEY_ID = 'AKIA3235CPNMLA462M5E'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'jintto-s3-backend'
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_REGION = 'ap-northeast-2'
# PROGRAM_OBJECT_KEY = 'data/asset_df.csv'

# # 정적 파일을 서빙할 URL(prefix) 설정
STATIC_URL = '/static/'
import os
# 정적 파일이 위치한 디렉토리 설정
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# 정적 파일 설정
# STATIC_LOCATION = 'jintto-s3-backend'
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'