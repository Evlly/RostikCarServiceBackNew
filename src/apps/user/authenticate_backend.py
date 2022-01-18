from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q  # noqa: WPS347

User = get_user_model()


class MultipleFieldsAuthBackend(ModelBackend):
    def authenticate(self, request, password=None, username=None, **kwargs):
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
        if username is None or password is None:
            return

        user = User.objects.filter(Q(username=username) | Q(email=username) | Q(phone=username)).first()

        if not user:
            return
        if not self.user_can_authenticate(user):
            return
        if user.check_password(password):
            return user
