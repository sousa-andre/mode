from django.contrib.auth.tokens import PasswordResetTokenGenerator


class UserRegistrationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(user.is_active) + str(timestamp)


user_activation_token = UserRegistrationTokenGenerator()
