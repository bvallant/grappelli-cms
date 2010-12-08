from django.conf import settings

REQUEST_ATTR = getattr(settings, 'LOGIN_FORM_REQUEST_ATTR', 'login_form')
FORM_NAME = getattr(settings, 'LOGIN_FORM_NAME', 'cms_login_form_plugin')