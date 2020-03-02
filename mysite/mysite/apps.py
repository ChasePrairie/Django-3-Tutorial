from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'polls'

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth'
]
