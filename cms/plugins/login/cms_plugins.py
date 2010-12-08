from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings as django_settings

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from cms.plugins.login.models import LoginFormPlugin

import settings
from models import BOTH, USERNAME, REALNAME

class LoginPlugin(CMSPluginBase):
    model = LoginFormPlugin
    name = _("Login Form")
    module = _('authentication')
    render_template = "cms/plugins/login.html"
    text_enabled = False
    admin_preview = False
    
    def render(self, context, instance, placeholder):
        if not 'cms.plugins.login.middleware.LoginFormMiddleware'\
         in django_settings.MIDDLEWARE_CLASSES:
            raise ImproperlyConfigured(_('You need to put "cms.plugins.login.LoginFormMiddleware" in settings.MIDDLEWARE_CLASSES to have the login form plugin work properly!'))
        request = context['request']
        form = getattr(request, settings.REQUEST_ATTR)
        if request.user.is_authenticated():
            if instance.name == BOTH:
                user_name = "%s(%s)" % (request.user.get_full_name(),
                                         request.user.username)
            if instance.name == USERNAME:
                user_name = request.user.username
            if instance.name == REALNAME:
                user_name = request.user.get_full_name()
            context.update({'user_name': user_name})    
        context.update({
            'object': instance, 
            'form': form,
            'form_name': settings.FORM_NAME,
            'placeholder': placeholder
        })
        return context 
 
plugin_pool.register_plugin(LoginPlugin)