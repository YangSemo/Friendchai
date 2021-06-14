from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class CaseInsensitiveModelBackend(ModelBackend):
    """
        커스텀 유저 인증 백엔드
    """
    def authenticate(self, request, username=None, password=None, **kwargs):

        user_model = get_user_model()
        if username is None:
            username = kwargs.get(user_model.USERNAME_FIELD)

        try:
            case_insensitive_username_field = '{}__iexact'.format(user_model.USERNAME_FIELD)
            user = user_model._default_manager.get(**{case_insensitive_username_field: username})
        except user_model.DoesNotExist:
            user_model().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
