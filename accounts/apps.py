from django.apps import AppConfig
from django.contrib.auth.apps import AuthConfig
from django.contrib.auth.management import create_permissions
from django.db.models.signals import post_migrate


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        post_migrate.disconnect(
            create_permissions,
            dispatch_uid="django.contrib.auth.management.create_permissions"
        )
