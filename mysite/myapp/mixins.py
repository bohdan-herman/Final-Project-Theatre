from django.contrib.auth.mixins import UserPassesTestMixin


class AdminPassTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class RequestToFormKwargsMixin:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class PkToFormKwargsMixin:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["pk"] = self.kwargs.get("pk")
        return kwargs