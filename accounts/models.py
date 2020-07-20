from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def create_user(self, email, password, **kwargs):
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first name'), max_length=45)
    last_name = models.CharField(_('last name'), max_length=45)
    email = models.EmailField(_('e-mail'), unique=True)
    picture = models.ImageField(_('picture'), upload_to='accounts/', default='default_profile.png')
    is_active = models.BooleanField(_('is active'), default=False)
    is_superuser = models.BooleanField(_('is superuser'), default=False)
    user_permissions = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
    ]
    objects = UserManager()

    def __str__(self):
        return f'{self.get_full_name()} - {self.email}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def latest_class(self):
        classes = self.classes.all().order_by('-year')
        return classes[0] if classes.count() > 0 else None

    def is_director(self):
        return True if self.groups.filter(key=1).count() > 0 else False
