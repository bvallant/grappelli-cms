from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

import settings

class LoginFormMiddleware(object):

    def process_request(self, request):
        if request.method == 'POST' and settings.FORM_NAME in request.POST:
            if 'logout' in request.POST:
                form = AuthenticationForm(request)
                setattr(request, settings.REQUEST_ATTR, form)
                logout(request)
                return
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
        else:
            form = AuthenticationForm(request)

        setattr(request, settings.REQUEST_ATTR, form)