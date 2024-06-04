import os
from datetime import timedelta

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'drf_spectacular',
    'drf_spectacular_sidecar',

]

LOCAL_APPS = [
    'apps.users',
    'apps.farpost',
]


INSTALLED_APPS += LOCAL_APPS

LOCAL_MIGRATIONS = [app_path.split('.')[1] for app_path in LOCAL_APPS]


MIGRATION_PATH = 'config.migrations.'

MIGRATION_MODULES = {app_name: MIGRATION_PATH + app_name for app_name in LOCAL_MIGRATIONS}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'IT-Solutions API',
    'DESCRIPTION': 'API for retrieving adverts from farpost',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    'SERVERS': [
        {
            'url': 'https://localhost:8000',
            'description': 'Dev server'
        },
        {
            'url': 'https://localhost',
            'description': 'Prod (nginx) server'
        },
    ]
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": True,
}

DJOSER = {
    'SERIALIZERS': {
        'user': 'apps.users.serializers.UserSerializer',
        'user_create': 'apps.users.serializers.UserSerializer',
        'current_user': 'apps.users.serializers.UserSerializer',
    },
    'TOKEN_MODEL': None,
}
