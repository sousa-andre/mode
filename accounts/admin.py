from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import User


class AccessUser:
    has_module_perms = has_perm = __getattr__ = lambda *args, **kw: True


admin.site.has_permission = lambda r: setattr(r, 'user', AccessUser()) or True

admin.site.register([User, Permission])

