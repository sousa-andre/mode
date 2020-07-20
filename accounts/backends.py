from django.contrib.auth.backends import ModelBackend


class Backend(ModelBackend):
    def get_all_permissions(self, user_obj, obj=None):
        if not user_obj.is_active or user_obj.is_anonymous or obj is not None:
            return set()
        if not hasattr(user_obj, '_perm_cache'):
            user_obj._perm_cache = super().get_group_permissions(user_obj)
        return user_obj._perm_cache
