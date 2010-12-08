from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

USERNAME = 'username'
REALNAME = 'name'
BOTH = 'both'
NAME_CHOICES = ((USERNAME, _("Username")),
                (REALNAME, _("Real Name")),
                (BOTH, _("Both")))

class LoginFormPlugin(CMSPlugin):
    title = models.CharField(_("title"), max_length=255, blank=True)
    welcome = models.BooleanField(_("Show welcome message"), default=True)
    name = models.CharField(_("show real name, user name or both"), 
                            choices=NAME_CHOICES, default=USERNAME,
                            max_length=10, blank=True, null=True)
    logout = models.BooleanField(_("show logout button"), default=True)
    forget_password = models.BooleanField(_("show forget password link"), 
                                          default=False)
        
    class Meta:
        verbose_name = _("login form")
        verbose_name_plural = _("login forms")
        
    def __unicode__(self):
        return unicode(_('login form'))
    
